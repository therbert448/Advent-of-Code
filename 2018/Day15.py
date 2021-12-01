def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global copygobs, copyelves, copymaps
    maps = set()
    gobs = {}
    elves = {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char == "#":
                continue
            pos = (y, x)
            if char == "G":
                gobs[pos] = 200
            elif char == "E":
                elves[pos] = 200
            else:
                maps.add(pos)
    global maxx, maxy
    copygobs = dict(gobs)
    copyelves = dict(elves)
    copymaps = set(maps)
    maxx = x
    maxy = y

def neighbours(pos):
    y, x = pos
    neighs = [(y-1, x),
              (y, x-1),
              (y, x+1),
              (y+1, x)]
    return neighs

def attack(enems):
    minhp = 201
    for e in enems:
        try:
            hp = elves[e]
        except: 
            hp = gobs[e]
        if hp < minhp:
            minhp = hp
            victim = e
    try:
        elves[victim] -= 3
        if elves[victim] <= 0:
            del elves[victim]
            maps.add(victim)
    except:
        gobs[victim] -= elfpower
        if gobs[victim] <= 0:
            del gobs[victim]
            maps.add(victim)

def steps_from_to(start, end):
    stepcount = {start: 0}
    posset = {start}
    while posset:
        newposset = set()
        for pos in posset:
            neighs = neighbours(pos)
            for n in neighs:
                if n not in stepcount and n in maps:
                    steps = stepcount[pos] + 1
                    newposset.add(n)
                    stepcount[n] = steps
        posset = set(newposset)
    if end not in stepcount:
        return -1
    else:
        return stepcount[end]

def move(ge, possteps):
    if ge in gobs:
        enems = list(elves.keys())
    else:
        enems = list(gobs.keys())
    inrange = []
    for e in enems:
        neighs = neighbours(e)
        for n in neighs:
            if n in maps:
                inrange.append(n)
    inrange = sorted(inrange)
    if not inrange:
        return ge
    minstep = 1000
    for end in inrange:
        steps = steps_from_to(ge, end)
        if steps == -1:
            continue
        elif steps < minstep:
            minstep = steps
            target = end
    if minstep == 1000:
        return ge
    minstep = 1000
    for end in possteps:
        steps = steps_from_to(target, end)
        if steps == -1:
            continue
        elif steps < minstep:
            minstep = steps
            nextpos = end
    if ge in gobs:
        gobs[nextpos] = gobs[ge]
        del gobs[ge]
    else:
        elves[nextpos] = elves[ge]
        del elves[ge]
    maps.add(ge)
    maps.remove(nextpos)
    return nextpos

def make_move(ge):
    neighs = neighbours(ge)
    possteps = []
    enems = []
    for n in neighs:
        if (ge in gobs and n in elves) or (ge in elves and n in gobs):
            enems.append(n)
        elif n in maps:
            possteps.append(n)
    if enems:
        attack(enems)
        return
    elif possteps:
        ge = move(ge, possteps)
        neighs = neighbours(ge)
        for n in neighs:
            if (ge in gobs and n in elves) or (ge in elves and n in gobs):
                enems.append(n)
        if enems:
            attack(enems)
            return

def run_round():
    gobset, elfset = [set(gobs.keys()), set(elves.keys())]
    gobelf = sorted(gobset.union(elfset))
    for ge in gobelf:
        if not gobs or not elves:
            return -1
        elif len(elves) < totalelves and elfpower != 3:
            return -1
        if ge not in gobs and ge not in elves:
            continue
        make_move(ge)
    return 1

def fight():
    global elfpower, totalelves
    elfpower = 3
    totalelves = len(copyelves)
    elvesdead = 1
    while elvesdead:
        global elves, gobs, maps
        elves = dict(copyelves)
        gobs = dict(copygobs)
        maps = set(copymaps)
        i = 0
        while gobs and elves:
            check = run_round()
            if check == -1:
                break
            i += 1
        if elfpower == 3:
            print("Part One:")
            if elves:
                score = sum(elves.values())
                print("Elves won with outcome =",i,"*",score,"=",i*score)
            else:
                score = sum(gobs.values())
                print("Goblins won with outcome =",i,"*",score,"=",i*score)
        elif elves and len(elves) == totalelves:
            print("Part Two:")
            score = sum(elves.values())
            print("Elves won with outcome =",i,"*",score,"=",i*score)
            elvesdead = 0
            break
        elfpower += 1

day = 15
open_file()

format_data()

fight()