import numpy as np

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global asts
    asts = []
    for i, row in enumerate(inputs):
        r = [char for char in row.strip()]
        for j, char in enumerate(r):
            if char == "#":
                asts.append((j,i))

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def vector(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    if x == 0:
        y /= abs(y)
    elif y == 0:
        x /= abs(x)
    else:
        fact = gcd(abs(x), abs(y))
        if fact > 1:
            x /= fact
            y /= fact
    vec = (int(x), int(y))
    return vec

def pos_from_base(base, vec, newasts):
    for n in range(1,dim):
        pos = tuple(map(lambda a, b: a+(b*n), base, vec))
        if pos in newasts:
            return pos
    return base

def vis_asts_count():
    astdict = {}
    for i, ast in enumerate(asts):
        astset = set()
        for j, ast2 in enumerate(asts):
            if j == i:
                continue
            vec = vector(ast, ast2)
            astset.add(vec)
        astdict[ast] = len(astset)
    maxast = max(astdict.values())
    print(maxast)
    for ast in astdict:
        if astdict[ast] == maxast:
            base = ast
    return astdict, base

def get_angle(vec):
    vecc = complex(-vec[1], vec[0])
    ang = np.angle(vecc, 1)
    ang = ang % 360
    return ang
    

def vis_asts_set(base):
    ast = base
    astset = set()
    for i, ast2 in enumerate(asts):
        if ast2 == ast:
            continue
        vec = vector(ast, ast2)
        astset.add(vec)
    angtovec = {}
    angs = []
    for vec in astset:
        ang = get_angle(vec)
        angtovec[ang] = vec
        angs.append(ang)
    angs.sort()
    sortvec = []
    for a in angs:
        sortvec.append(angtovec[a])
    return angs, sortvec
        
def shoot_asts(base):
    angs, sortvec = vis_asts_set(base)
    newasts = list(asts)  
    count = 0
    while len(newasts) > 1:
        for i in range(len(angs)):
            vec = sortvec[i]
            pos = pos_from_base(base, vec, newasts)
            if pos == base:
                continue
            else:
                count += 1
                newasts.remove(pos)
                if count == 200:
                    print("200th asteroid =", pos)
                    return

day = 10
inputs = open_file()

formatdata(inputs)

dim = 32

astdict, base = vis_asts_count()
shoot_asts(base)