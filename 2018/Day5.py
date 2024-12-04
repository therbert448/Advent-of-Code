def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global polymer
    polymer = file.read()
    file.close()

def unit_pairs():
    global pairset, charset
    pairset = set()
    charset = set()
    for char in polymer:
        if char.lower() not in charset:
            charset.add(char.lower())
    for char in charset:
        cap = char.upper()
        pairset.add(cap + char)
        pairset.add(char + cap)

def remove_unit(unit):
    newpoly = str(polymer)
    unitin = 1
    while unitin:
        if unit.upper() not in newpoly and unit not in newpoly:
            break
        newpoly = newpoly.replace(unit, "")
        newpoly = newpoly.replace(unit.upper(), "")
    return newpoly

def react(polymer):
    string = str(polymer)
    changing = 1
    while changing:
        changing = 0
        for pair in pairset:
            if pair in string:
                string = string.replace(pair, "")
                changing = 1
    return string

def part_one():
    unit_pairs()
    string = react(polymer)
    print("Part One:", len(string))

def part_two():
    unitdict = {}
    for unit in charset:
        newpoly = remove_unit(unit)
        string = react(newpoly)
        unitdict[unit] = len(string)
    print("Part Two:", min(unitdict.values()))

day = 5
open_file()

part_one()
part_two()