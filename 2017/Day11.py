def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.read().strip().split(",")
    file.close()

def move_in_dir(pos, direct, n): #move in the given direction n times
    f = lambda a, b: a + (b * n)
    if direct == "sw":
        direct, n = ["ne", -1]
    elif direct == "se":
        direct, n = ["nw", -1]
    elif direct == "s":
        direct, n = ["n", -1]
    d = compass[direct]
    pos = tuple(map(f, pos, d))
    return pos
    
def follow_steps(): #follow each instruction
    global pos
    counts = {}
    pos = (0, 0)
    for d in directions:
        counts[d] = inputs.count(d)
    nesw = counts["ne"] - counts["sw"]
    #A step north east then a step south west leaves you in the same place
    ns = counts["n"] - counts["s"] #Same for n and s
    nwse = counts["nw"] - counts["se"] #And for nw and se
    directs = [nesw, ns, nwse] #number of steps in each direction
    for i, d in enumerate(compass.keys()):
        pos = move_in_dir(pos, d, directs[i])

def part_one():
    follow_steps()
    x, y = pos
    if (x <= 0 and y >=0) or (x >=0 and y <= 0 ):
        totalsteps = max([abs(x), abs(y)])
    else:
        totalsteps = sum([abs(x), abs(y)])
    print("Part One:", totalsteps)

def part_two():
    pos = (0, 0)
    maxsteps = 0
    for step in inputs:
        pos = move_in_dir(pos, step, 1)
        x, y = pos
        if (x <= 0 and y >=0) or (x >=0 and y <= 0 ):
            totalsteps = max([abs(x), abs(y)])
        else:
            totalsteps = sum([abs(x), abs(y)])
        if totalsteps > maxsteps:
            maxsteps = totalsteps
    print("Part Two:", maxsteps)

day = 11
open_file()

directions = ["ne", "se", "s", "sw", "nw", "n"] #all 6 directions

compass = {"ne": (1, 0), "n": (0, 1), "nw": (-1, 1)} #3 axes of directions

part_one()
part_two()