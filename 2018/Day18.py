def open_file():
    #file = open("test.txt")
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global grid
    grid = {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            pos = (x, y)
            grid[pos] = char
    global xdim, ydim
    xdim = x+1
    ydim = y+1

def neighbours(pos):
    x, y = pos
    neighs = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            n = (x + dx, y + dy)
            neighs.append(n)
    return neighs

def run_GOL(grid):
    newgrid = {}
    for x in range(xdim):
        for y in range(ydim):
            pos = (x, y)
            current = grid[pos]
            neighs = neighbours(pos)
            opencount = 0
            treecount = 0
            yardcount = 0
            for n in neighs:
                if n not in grid:
                    continue
                state = grid[n]
                if state == ".":
                    opencount += 1
                elif state == "|":
                    treecount += 1
                else:
                    yardcount +=1
            if current == "." and treecount >= 3:
                current = "|"
            elif current == "|" and yardcount >= 3:
                current = "#"
            elif current == "#" and (yardcount == 0 or treecount == 0):
                current = "."
            newgrid[pos] = current
    return newgrid

def print_grid(grid):
    string = ""
    for y in range(ydim):
        for x in range(xdim):
            pos = (x, y)
            string += grid[pos]
        string += "\n"
    return string

def run_mins(n):
    newgrid = dict(grid)
    loop = 0
    string = print_grid(grid) #revert the grid to a string
    stringdict = {string: 0} #keep a record of every layout
    for i in range(n): #run the game of life until a loop is found
        newgrid = run_GOL(newgrid)
        string = print_grid(newgrid)
        if string in stringdict: #if this layout has already appeared
            start = stringdict[string] #the loop started here
            repeat = i+1 #and restarted here
            loop = 1
            break
        else:
            stringdict[string] = i+1
    if loop:
        #start = 410 => After 410 mins the area starts a loop
        #repeat = 494 => 84 mins later the loop restarts
        minsafterloop = n - start
        looplen = repeat - start
        offset = minsafterloop % looplen
        minsneeded = start + offset #412
        #After 1000000000 mins the resource val will be the same as minute 412
        stringidx = list(stringdict.values()).index(minsneeded)
        string = list(stringdict.keys())[stringidx]
        wood, lumbyard = [string.count("|"), string.count("#")]
    else:
        gridvals = list(newgrid.values())
        wood, lumbyard = [gridvals.count("|"), gridvals.count("#")]
    resourceval = wood * lumbyard
    if n == 10:
        print("Part One:", resourceval)
    else:
        print("Part Two:", resourceval)
    
day = 18
open_file()

format_data()

run_mins(10)
run_mins(1000000000)