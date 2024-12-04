def open_file():
    file = open("test.txt")
    #file = open("Day" + str(day) + "inputs.txt")
    startmap = file.read()
    file.close()
    return startmap

def map_to_grid(startmap):
    gridlist = []
    for line in startmap.splitlines():
        row = [char for char in line]
        gridlist.append(row)
    global grid, warpd
    grid = set()
    warpd = {}
    for y, line in enumerate(gridlist):
        for x, char in enumerate(line):
            if char in (" ", "#"):
                continue
            pos = (x, y)
            if char.isupper():
                warpd[pos] = char
            else:
                grid.add(pos)

def neighbours(pos):
    x, y = [pos[0], pos[1]]
    neighs = [(x+1, y),
              (x, y+1),
              (x-1, y),
              (x, y-1)]
    return neighs

def warp_points():
    newwarps = dict(warpd)
    global warps, warpent
    warps = {}
    warpent = {}
    f1, f2 = [lambda a,b: a+b, lambda a,b: a-b]
    steps =[(1,0), (0,1), (-1,0), (0,-1)]
    for pos in warpd:
        if pos not in newwarps:
            continue
        char1 = newwarps[pos]
        for step in steps:
            neigh = tuple(map(f1, pos, step))
            if neigh in newwarps:
                char2 = newwarps[neigh]
                warp = "".join(sorted([char1, char2]))
                check1 = tuple(map(f2, pos, step))
                check2 = tuple(map(f1, neigh, step))
                if check1 in grid:
                    warps[pos] = warp
                    warpent[pos] = check1
                elif check2 in grid:
                    warps[neigh] = warp
                    warpent[neigh] = check2
                else:
                    print("Can't find Warp point")
                del newwarps[pos], newwarps[neigh]
                break
    global start, end
    newwarps = dict(warps)
    for warp in newwarps:
        code = warps[warp]
        if code == "AA":
            neighs = neighbours(warp)
            for n in neighs:
                if n in grid:
                    start = n
                    break
            del warps[warp]
            continue
        elif code == "ZZ":
            neighs = neighbours(warp)
            for n in neighs:
                if n in grid:
                    end = n
                    break
            del warps[warp]
            continue
        pointA = warpent[warp]
        for w in warps:
            if w == warp:
                continue
            if warps[w] == code:
                pointB = warpent[w]
                warps[warp] = pointB
                warps[w] = pointA
    del warpent, newwarps

def start_to_finish():
    pos = start
    stepcount = {pos: 0}
    posset = {pos}
    while posset:
        newposset = set()
        for pos in posset:
            neighs = neighbours(pos)
            for n in neighs:
                if n in warps:
                    n = warps[n]
                if n not in stepcount and n in grid:
                    steps = stepcount[pos] + 1
                    newposset.add(n)
                    stepcount[n] = steps
                    if n == end:
                        print(stepcount[n])
                        return
        
        posset = set(newposset)

day = 20

startmap = open_file()
map_to_grid(startmap)
warp_points()
start_to_finish()