
def open_file(day):
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

def go():
    facing = "E"
    com = compass.index(facing)
    pos = [0, 0]
    for command in instructs:
        direct = command[0]
        value = command[1]
        if direct in xydict:
            pos[0] += value * xydict[direct][0]
            pos[1] += value * xydict[direct][1]
        elif direct in turn:
            value = int(value/90)
            if direct == "L":
                value *= -1
            com = (com + value) % 4
            facing = compass[com]
        elif direct == "F":
            pos[0] += value * xydict[facing][0]
            pos[1] += value * xydict[facing][1]
        else:
            print("Error with input")
            return 0
    dist = sum(abs(a) for a in pos)            
    return dist

def turn_vector(vector, turns):
    if turns == 0:
        print("Turning 0 degrees?")
        return vector
    elif turns == 2:
        for i in range(len(vector)):
            vector[i] *= -1
    elif turns == 1:
        newx = vector[1]
        newy = vector[0] * -1
        vector = [newx, newy]
    elif turns == 3:
        newx = vector[1] * -1
        newy = vector[0]
        vector = [newx, newy]
    else:
        print("Turns must be integer number")
        return vector
    return vector
            
def go2():
    vector = [10, 1]
    pos = [0, 0]
    
    for command in instructs:
        direct = command[0]
        value = command[1]
        if direct in xydict:
            vector[0] += value * xydict[direct][0]
            vector[1] += value * xydict[direct][1]
        elif direct in turn:
            value = int(value/90)
            if direct == "L":
                value = 4 - value
            vector = turn_vector(vector, value)
        elif direct == "F":
            pos[0] += value * vector[0]
            pos[1] += value * vector[1]
        else:
            print("Error with input")
            return 0

    dist = sum(abs(a) for a in pos)            
    return dist
    

day = 12
inputs = open_file(day)

formatdata(inputs)

xydict = {"E": [1, 0], "N": [0, 1], "W": [-1, 0], "S": [0, -1]}
compass = ["N", "E", "S", "W"]
turn = ["R", "L"]

print(go())
print(go2())






