def find_type(pos):
    x, y = pos
    if (x == 0 and y == 0) or (x == xmax and y == ymax):
        gi = 0
    elif y == 0:
        gi = x * xgeo
    elif x == 0:
        gi = y * ygeo
    else:
        one = (x-1, y)
        if one not in erosions:
            find_type(one)
        elone = erosions[one]
        two = (x, y-1)
        if two not in erosions:
            find_type(two)
        eltwo = erosions[two]
        gi = elone * eltwo
    el = (gi + depth) % emod
    erosions[pos] = el
    types[pos] = el % tmod

def type_grid():
    global erosions, types
    erosions = {}
    types = {}
    for x in range(xmax + 1):
        for y in range(ymax + 1):
            pos = (x, y)
            find_type(pos)

def neighbours(pos):
    x, y = pos
    neighs = [(x+1, y), (x, y+1)]
    if x != 0:
        neighs.append((x-1, y))
    if y != 0:
        neighs.append((x, y-1))
    return neighs
            
def risk_level():
    typelist = list(types.values())
    print("Part One:", sum(typelist))

def cross_map():
    start = (0, 0, "T")
    t = 0
    global mincount
    mincount = {start: t}
    tpos = (xmax, ymax)
    target = (*tpos, "T")
    finished = 0
    positions = {start}
    while not finished:
        newpos = set()
        for current in positions:
            if mincount[current] > t:
                newpos.add(current)
                continue
            pos = tuple(current[0:-1])
            equipped = current[2]
            if pos == tpos and equipped != "T":
                nextpos = (*pos, "T")
                newpos.add(nextpos)
                if nextpos not in mincount:
                    mincount[nextpos] = mincount[current] + 7
                continue
            if current == target:
                print("Part Two:", mincount[target])
                return
            curreg = types[pos]
            curgear = regions[curreg]
            neighs = neighbours(pos)
            for n in neighs:
                nextpos = (*n, equipped)
                if n not in types:
                    find_type(n)
                nextreg = types[n]
                nextgear = regions[nextreg]
                if equipped not in nextgear:
                    need = [*curgear.intersection(nextgear)]
                    nextpos = (*pos, need.pop())
                    if nextpos not in mincount:
                        mincount[nextpos] = mincount[current] + 7
                        newpos.add(nextpos)
                    elif mincount[nextpos] > mincount[current] + 7:
                        mincount[nextpos] = mincount[current] + 7
                        newpos.add(nextpos)
                    continue
                else:
                    if nextpos not in mincount:
                        mincount[nextpos] = mincount[current] + 1
                        newpos.add(nextpos)
                    elif mincount[nextpos] > mincount[current] + 1:
                        mincount[nextpos] = mincount[current] + 1
                        newpos.add(nextpos)
        positions = set(newpos)
        t += 1

def part_one():
    type_grid()
    risk_level()

def part_two():
    cross_map()

#inputs
xmax = 10
ymax = 725
depth = 8787
emod = 20183
tmod = 3
xgeo = 16807
ygeo = 48271
regions = {0: {"C", "T"}, 1: {"C", "N"}, 2: {"N", "T"}}
gear = {"C": [0, 1], "N": [1, 2], "T": [0, 2]}

part_one()
part_two()