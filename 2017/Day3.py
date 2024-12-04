def bottom_right():
    global i, lastcorner
    i = 1
    corner = i**2
    while corner < square:
        lastcorner = corner
        i += 2
        corner = i**2

def find_square():
    steps = square - lastcorner
    edgesize = i - 1
    xymax = edgesize//2
    stepsleft = steps % edgesize
    fromorig = xymax - stepsleft
    dist = xymax + abs(fromorig)
    print("Part One:", dist)

def sum_neighs(pos):
    neighs = []
    x, y = pos
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            n = (x + dx, y + dy)
            neighs.append(n)
    posval = 0
    for n in neighs:
        if n in vals:
            posval += vals[n]
    vals[pos] = posval

def spiral():
    directs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    start = (0, 0)
    global vals
    vals = {start: 1}
    pos = start
    didx = -1
    while vals[pos] < square:
        x, y = pos
        if abs(x) == abs(y):
            if x <= 0 or y >= 0:
                didx = (didx + 1) % 4
        direct = directs[didx]
        pos = tuple(pos[i] + direct[i] for i in range(2))
        sum_neighs(pos)
        if abs(x) == abs(y):
            if x >= 0 and y <= 0:
                didx = (didx + 1) % 4
        value = vals[pos]
    print("Part Two:", value)

square = 277678

bottom_right()
find_square()
spiral()