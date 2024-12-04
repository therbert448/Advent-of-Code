def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    startmap = file.readlines()
    file.close()
    return startmap

def formatdata(inputs):
    global bugs, size
    bugs = set()
    size = len(inputs)
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char == "#":
                pos = (x, y)
                bugs.add(pos)

def neighbours(pos):
    x, y = [pos[0], pos[1]]
    neighbours = [(x+1, y),
                  (x, y+1),
                  (x-1, y),
                  (x, y-1)]
    neighs = []
    for n in neighbours:
        x, y = [n[0], n[1]]
        if x < 0 or x >= size or y < 0 or y >= size:
            continue
        else:
            neighs.append(n)
    return neighs

def rec_neighs(pos):
    level, x, y = [pos[0], pos[1][0], pos[1][1]]
    neighbours = [(x+1, y),
                  (x, y+1),
                  (x-1, y),
                  (x, y-1)]
    neighs = []
    for n in neighbours:
        x, y = [n[0], n[1]]
        if n == (2, 2):
            if pos[1] == (2, 1):
                innerns = [(level-1, (0, 0)),
                           (level-1, (1, 0)),
                           (level-1, (2, 0)),
                           (level-1, (3, 0)),
                           (level-1, (4, 0))]
            elif pos[1] == (1, 2):
                innerns = [(level-1, (0, 0)),
                           (level-1, (0, 1)),
                           (level-1, (0, 2)),
                           (level-1, (0, 3)),
                           (level-1, (0, 4))]
            elif pos[1] == (3, 2):
                innerns = [(level-1, (4, 0)),
                           (level-1, (4, 1)),
                           (level-1, (4, 2)),
                           (level-1, (4, 3)),
                           (level-1, (4, 4))]
            elif pos[1] == (2, 3):
                innerns = [(level-1, (0, 4)),
                           (level-1, (1, 4)),
                           (level-1, (2, 4)),
                           (level-1, (3, 4)),
                           (level-1, (4, 4))]
            for inn in innerns:
                neighs.append(inn)
        elif x == -1:
            outern = (level+1, (1, 2))
            neighs.append(outern)
        elif x == size:
            outern = (level+1, (3, 2))
            neighs.append(outern)
        elif y == -1:
            outern = (level+1, (2, 1))
            neighs.append(outern)
        elif y == size:
            outern = (level+1, (2, 3))
            neighs.append(outern)
        else:
            neighs.append((level, n))
    return neighs

def update_grid(bugs):
    newbugs = set()
    for x in range(size):
        for y in range(size):
            pos = (x, y)
            neighs = neighbours(pos)
            count = 0
            for n in neighs:
                if n in bugs:
                    count += 1
            if pos in bugs and count == 1:
                newbugs.add(pos)
            elif pos not in bugs and count in (1, 2):
                newbugs.add(pos)
    posids = []
    for bug in newbugs:
        x, y = [bug[0], bug[1]]
        posid = (y * size) + x
        posids.append(posid)
    state = tuple(posids)
    return newbugs, state

def update_rec_grid(bugs):
    newbugs = set()
    for pos in bugs:
        neighs = rec_neighs(pos)
        poscount = 0
        for neigh in neighs:
            if neigh in bugs:
                poscount += 1
            neighneighs = rec_neighs(neigh)
            neighcount = 0
            for n in neighneighs:
                if n in bugs:
                    neighcount += 1
            if neigh in bugs: 
                poscount += 1
                if neighcount == 1:
                    newbugs.add(neigh)
            elif neigh not in bugs and neighcount in (1, 2):
                newbugs.add(neigh)
        if pos in bugs and poscount == 1:
            newbugs.add(pos)
        elif pos not in bugs and poscount in (1, 2):
            newbugs.add(pos)
    return newbugs

def run_GOL():
    states = set()
    newbugs = set(bugs)
    while True:
        newbugs, state = update_grid(newbugs)
        if state in states:
            return state
        else:
            states.add(state)

def run_rec_GOL():
    newbugs = set()
    for bug in bugs:
        newbugs.add((0, bug))
    for _ in range(200):
        newbugs = update_rec_grid(newbugs)
    return newbugs

def part_one():
    state = run_GOL()
    total = 0
    for pos in state:
        total += 2**pos
    print(total)

def part_two():
    newbugs = run_rec_GOL()
    print(len(newbugs))

day = 24
inputs = open_file()

formatdata(inputs)

part_one()
part_two()