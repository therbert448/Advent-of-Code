def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line for line in file.readlines()]
    file.close()

def format_data():
    global tracks, carts, cartints, xdim, ydim
    tracks = {}
    carts = {}
    cartints = {}
    xdim, ydim = [len(inputs[0]), len(inputs)]
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            pos = (x, y)
            if char in ("<", ">", "^", "v"):
                carts[pos] = directs[char]
                cartints[pos] = 0
                tracks[pos] = "."
            elif char in ("/", "\\", "+"):
                tracks[pos] = char
            elif char not in (" ", "\n"):
                tracks[pos] = "."

def move_carts(carts, cartints, part):
    dirlist = list(directs.values())
    newcarts = {}
    newcartints = {}
    crashed = []
    for y in range(ydim):
        for x in range(xdim):
            pos = (x, y)
            if pos not in carts:
                continue
            velx, vely = carts[pos]
            newpos = (pos[0] + velx, pos[1] + vely)
            if newpos in newcarts or newpos in carts:
                if part == 1:
                    print("Crash at", newpos)
                    return -1, -1
                else:
                    crashed.append(newpos)
                    if newpos in carts:
                        del carts[newpos]
                    continue
            if tracks[newpos] == "/":
                newvel = (-vely, -velx)
            elif tracks[newpos] == "\\":
                newvel = (vely, velx)
            elif tracks[newpos] == "+":
                count = cartints[pos] % 3
                idx = dirlist.index(carts[pos])
                idx = (idx + count - 1) % 4
                newvel = dirlist[idx]
                cartints[pos] += 1
            else:
                newvel = carts[pos]
            newcarts[newpos] = newvel
            newcartints[newpos] = cartints[pos]
            del carts[pos]
    if part == 2:
        for cart in crashed:
            del newcarts[cart]
    return newcarts, newcartints

def run_carts():
    part = 1
    newcarts = dict(carts)
    newcartints = dict(cartints)
    crash = 0
    while not crash:
        newcarts, newcartints = move_carts(newcarts, newcartints, part)
        if newcarts == -1:
            crash = 1
            break

def run_carts2():
    part = 2
    newcarts = dict(carts)
    newcartints = dict(cartints)
    cartsleft = len(carts) - 1
    while cartsleft:
        newcarts, newcartints = move_carts(newcarts, newcartints, part)
        cartsleft = len(newcarts) - 1
    print("Last Cart = ", *newcarts.keys())
    
day = 13
open_file()

directs = {">": (1,0), "v": (0,1), "<": (-1,0), "^": (0,-1)}

format_data()

run_carts()
run_carts2()