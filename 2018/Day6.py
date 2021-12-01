def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.readlines()
    file.close()

def formatdata():
    global locs, xset, yset
    locs = {}
    xset, yset = [set(), set()]
    for i, line in enumerate(inputs):
        x, y = line.strip().split(", ")
        x, y = [int(x), int(y)]
        xset.add(x)
        yset.add(y)
        locs[i] = (x, y)

def grid_size():
    xrange = [min(xset), max(xset)+1]
    yrange = [min(yset), max(yset)+1]
    return xrange, yrange

def define_bad_areas():
    newlocs = dict(locs)
    xrange, yrange = grid_size()
    posdict = {}
    for x in range(*xrange):
        for y in range(*yrange):
            pos = (x, y)
            for idx, loc in newlocs.items():
                locx, locy = [*loc]
                xdif, ydif = [abs(x - locx), abs(y - locy)]
                mandist = xdif + ydif
                if pos not in posdict:
                    posdict[pos] = [idx, mandist]
                elif mandist < posdict[pos][1]:
                    posdict[pos] = [idx, mandist]
                elif mandist == posdict[pos][1]:
                    posdict[pos] = [".", mandist]
            posdict[pos] = posdict[pos][0]
    for x in range(*xrange):
        for y in range(*yrange):
            if x in (xrange[0], xrange[1]-1) or y in (yrange[0], yrange[1]-1):
                pos = (x, y)
                if posdict[pos] in newlocs:
                    del newlocs[posdict[pos]]
    posvalues = list(posdict.values())
    maxarea = 0
    for idx in newlocs:
        countidx = posvalues.count(idx)
        if countidx > maxarea:
            maxarea = countidx
    print("Part One:", maxarea)

def define_good_areas():
    xrange, yrange = grid_size()
    goodpos = set()
    for x in range(*xrange):
        for y in range(*yrange):
            pos = (x, y)
            distcount = 0
            good = 1
            for loc in locs.values():
                locx, locy = [*loc]
                xdif, ydif = [abs(x - locx), abs(y - locy)]
                mandist = xdif + ydif
                distcount += mandist
                if distcount >= 10_000:
                    good = 0
                    break
            if good:
                goodpos.add(pos)
    print("Part Two:", len(goodpos))

    
day = 6
open_file()

formatdata()

define_bad_areas()
define_good_areas()