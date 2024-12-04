def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global wireA
    global wireB
    wireA = [i for i in inputs[0].strip().split(",")]
    wireB = [i for i in inputs[1].strip().split(",")]

def wire_crossing():
    posA = (0, 0)
    posB = (0, 0)
    wA = {posA}
    wB = {posB}
    for ins in wireA:
        d = ins[0]
        step = int(ins[1:])
        for i in range(step):
            newpos = tuple(map(lambda a,b: a+b, posA, direct[d]))
            posA = newpos
            wA.add(newpos)
    for ins in wireB:
        d = ins[0]
        step = int(ins[1:])
        for i in range(step):
            newpos = tuple(map(lambda a,b: a+b, posB, direct[d]))
            posB = newpos
            wB.add(newpos)
    cross = []
    for coord in wB:
        if coord == (0, 0):
            continue
        if coord in wA:
            cross.append(coord)
    dist = []
    for coord in cross:
        d = abs(coord[0]) + abs(coord[1])
        dist.append(d)
    return min(dist), cross
  
def dist_to_wire_crossing(cross):
    posA = (0, 0)
    posB = (0, 0)
    crossA = {}
    crossB = {}
    iA = 0
    iB = 0
    for ins in wireA:
        d = ins[0]
        step = int(ins[1:])
        for i in range(step):
            newpos = tuple(map(lambda a,b: a+b, posA, direct[d]))
            iA += 1
            posA = newpos
            if newpos in cross:
                crossA[newpos] = iA
    for ins in wireB:
        d = ins[0]
        step = int(ins[1:])
        for i in range(step):
            newpos = tuple(map(lambda a,b: a+b, posB, direct[d]))
            iB += 1
            posB = newpos
            if newpos in cross:
                crossB[newpos] = iB
    dist = []
    for coord in cross:
        stepA = crossA[coord]
        stepB = crossB[coord]
        totalsteps = stepA + stepB
        dist.append(totalsteps)
    return min(dist)
  
day = 3
inputs = open_file()

direct = {"R":[1,0], "U":[0,1], "L":[-1,0], "D":[0,-1]}

formatdata(inputs)
dist, cross = wire_crossing()
print(dist)
print(dist_to_wire_crossing(cross))