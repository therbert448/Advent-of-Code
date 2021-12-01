def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global dominos
    dominos = set()
    for line in inputs:
        a, b = line.split("/")
        dominos.add((int(a), int(b)))

def find_matches(port, domsleft):
    possdoms = []
    for dom in domsleft:
        if port in dom:
            possdoms.append(dom)
    if not possdoms:
        return 0
    maxstrength = 0
    for dom in possdoms:
        strength = sum(dom)
        newdoms = list(domsleft)
        newdoms.remove(dom)
        dlist = list(dom)
        dlist.remove(port)
        newport = dlist[0]
        strength += find_matches(newport, newdoms)
        if strength > maxstrength:
            maxstrength = strength
    return maxstrength

def find_lengths(port, domsleft):
    possdoms = []
    for dom in domsleft:
        if port in dom:
            possdoms.append(dom)
    if not possdoms:
        return 0, 0
    maxlength = -1
    maxstren = 0
    for dom in possdoms:
        strength = sum(dom)
        newdoms = list(domsleft)
        newdoms.remove(dom)
        dlist = list(dom)
        dlist.remove(port)
        newport = dlist[0]
        stren, length = find_lengths(newport, newdoms)
        strength += stren
        if length > maxlength:
            maxlength = length
            maxstren = strength
        elif length == maxlength and strength > maxstren:
            maxstren = strength
    return maxstren, maxlength + 1

def part_one():
    domsleft = list(dominos)
    maxstrength = find_matches(0, domsleft)
    print("Part One:", maxstrength)

def part_two():
    domsleft = list(dominos)
    maxstren, length = find_lengths(0, domsleft)
    print("Part Two:", maxstren)

day = 24
open_file()

format_data()

part_one()
part_two()