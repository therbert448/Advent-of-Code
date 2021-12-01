def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    startmap = file.read()
    file.close()
    return startmap

def map_to_grid(startmap):
    gridlist = []
    for line in startmap.splitlines():
        row = [char for char in line]
        gridlist.append(row)
    global grid, warpd, xsize, ysize
    ysize = len(gridlist)
    xsize = len(gridlist[0])
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
    warpinout = {}
    f1, f2 = [lambda a,b: a+b, lambda a,b: a-b]
    steps =[(1,0), (0,1), (-1,0), (0,-1)]
    for pos in warpd:
        if pos not in newwarps:
            continue
        char1 = newwarps[pos]
        x, y = [pos[0], pos[1]]
        if x < 2 or x >= xsize - 2:
            inout = "OUT"
        elif y < 2 or y >= ysize - 2:
            inout = "OUT"
        else:
            inout = "IN"
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
                    warpinout[pos] = inout
                elif check2 in grid:
                    warps[neigh] = warp
                    warpent[neigh] = check2
                    warpinout[neigh] = inout
                else:
                    print("Can't find Warp point")
                del newwarps[pos], newwarps[neigh]
                break
    global start, end, warpdict
    newwarps = dict(warps)
    warpdict = {}
    for warp in newwarps:
        code = warps[warp]
        if code == "AA":
            neighs = neighbours(warp)
            for n in neighs:
                if n in grid:
                    start = (0, n)
                    break
            del warps[warp]
            continue
        elif code == "ZZ":
            neighs = neighbours(warp)
            for n in neighs:
                if n in grid:
                    end = (0, n)
                    break
            del warps[warp]
            continue
        if warpinout[warp] == "OUT":
            level = 1
        else:
            level = -1
        pointA = (level, warpent[warp])
        for w in warps:
            if w == warp:
                continue
            if warps[w] == code:
                warpdict[warpent[warp]] = code
                warpdict[warpent[w]] = code
                pointB = (-level, warpent[w])
                warps[warp] = pointB
                warps[w] = pointA
    del warpent, newwarps, warpinout

def start_to_finish():
    pos = start
    global stepcount, posset
    stepcount = {pos: 0}
    posset = {pos}
    while posset:
        newposset = set()
        for pos in posset:
            p = pos[1]
            neighs = neighbours(p)
            for n in neighs:
                n = (pos[0], n)
                if n[1] in warps:
                    addlevel = warps[n[1]][0]
                    nextlevel = addlevel + n[0]
                    if nextlevel >= 0:
                        n = (nextlevel, warps[n[1]][1])
                if n not in stepcount and n[1] in grid:
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