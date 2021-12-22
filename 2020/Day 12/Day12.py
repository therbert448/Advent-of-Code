
def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global instructs
    instructs = []
    for i in inputs:
        direct = i[0]
        value = int(i[1:])
        instructs.append([direct, value])
    return

def add_vector(p, xy, val):
    p += xy * val
    return p

def go():
    face = "E"
    com = compass.index(face)
    pos = [0, 0]
    for command in instructs:
        d = command[0]
        val = command[1]
        f = lambda p, xy: add_vector(p, xy, val)
        if d in xydict:
            vec = xydict[d]
            pos = list(map(f, pos, vec))
        elif d in turn:
            val = val//90
            if d == "L":
                val *= -1
            com = (com + val) % 4
            face = compass[com]
        elif d == "F":
            vec = xydict[face]
            pos = list(map(f, pos, vec))
        else:
            print("Error with input")
            return 0
    
    dist = sum(abs(coord) for coord in pos)            
    return dist

def turn_vector(vector, turns):
    x = vector[0]
    y = vector[1]
    if turns == 0:
        print("Turning 0 degrees?")
        return vector
    elif turns == 2:
        vector = [-v for v in vector]
    elif turns == 1:
        vector = [y, -x]
    elif turns == 3:
        vector = [-y, x]
    else:
        print("Turns must be integer number")
        return vector
    return vector
            
def go2():
    vec = [10, 1]
    pos = [0, 0]
    for command in instructs:
        d = command[0]
        val = command[1]
        f = lambda p, xy: add_vector(p, xy, val)
        if d in xydict:
            addvec = xydict[d]
            vec = list(map(f, vec, addvec))
        elif d in turn:
            val = val//90 % 4
            if d == "L":
                val = 4 - val
            vec = turn_vector(vec, val)
        elif d == "F":
            pos = list(map(f, pos, vec))
        else:
            print("Error with input")
            return 0

    dist = sum(abs(coord) for coord in pos)            
    return dist
    
day = 12
inputs = open_file()

formatdata(inputs)

xydict = {"E": [1, 0], "N": [0, 1], "W": [-1, 0], "S": [0, -1]}
compass = ["N", "E", "S", "W"]
turn = ["R", "L"]

print(go())
print(go2())
