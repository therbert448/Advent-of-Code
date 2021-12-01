def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global coordlist
    coordlist = []
    for line in inputs:
        coords = tuple(int(xyzw) for xyzw in line.split(","))
        coordlist.append(coords)

def pos_in_const(pos, consts):
    newconsts = list(consts)
    posconst = {pos}
    for coord in coordlist:
        dist = sum([abs(pos[i] - coord[i]) for i in range(4)])
        if dist <= 3:
            posconst.add(coord)
    for const in consts:
        if pos in const:
            newconsts.remove(const)
            posconst.update(const)
    newconsts.append(posconst)
    return newconsts

def link_each_pos():
    global consts
    consts = []
    while coordlist:
        coord = coordlist.pop()
        consts = pos_in_const(coord, consts)

def part_one():
    link_each_pos()
    print("Day 25:", len(consts))

day = 25
open_file()

format_data()

part_one()