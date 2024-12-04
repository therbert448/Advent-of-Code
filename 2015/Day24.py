def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [int(line.strip()) for line in file.readlines()]
    file.close()

def format_data():
    global presents, weightone, weighttwo
    presents = sorted(inputs, reverse=True)
    weightone = sum(presents)//3
    weighttwo = sum(presents)//4

def combs(group, left):
    weightleft = weight - sum(group)
    if sum(left) < weightleft:
        return
    if weightleft in left:
        group.add(weightleft)
        comb = tuple(group)
        if firsts:
            minnum, minqe = min(firsts.values())
            if len(comb) > minnum:
                return
        mult = 1
        for val in comb:
            mult *= val
        if firsts and len(comb) == minnum and mult >= minqe:
            return
        firsts[comb] = (len(comb), mult)
    for i, present in enumerate(left):
        if present > weightleft:
            continue
        newgroup = set(group)
        newgroup.add(present)
        combs(newgroup, left[i+1:])

def first_group():
    global firsts
    firsts = {}
    for i, present in enumerate(presents):
        group = {present}
        combs(group, presents[i+1:])
    minqe = min(firsts.values())
    if part == 1:
        print(f"Part One: {minqe[1]}")
    else:
        print(f"Part Two: {minqe[1]}")

day = 24
open_file()

format_data()

part = 1
weight = weightone
first_group()

part = 2
weight = weighttwo
first_group()