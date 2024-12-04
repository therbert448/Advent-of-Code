def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.read().split("\n\n")
    file.close()

def format_data():
    global plants, rules
    plants = set()
    rules = {}
    _, _, row = inputs[0].strip().split(" ")
    for i, char in enumerate(row):
        if char == "#":
            plants.add(i)
    for rule in inputs[1].splitlines():
        rule = rule.strip().split(" => ")
        rulelist = []
        for i, char in enumerate(rule[0]):
            if i == 2 and char == "#" and rule[1] == ".":
                actpas = "acttopas"
            elif i == 2 and char == "#":
                actpas = "acttoact"
            elif i == 2 and rule[1] == "#":
                actpas = "pastoact"
            elif i == 2:
                actpas = "pastopas"
            elif char == "#":
                idx = i - 2
                rulelist.append(idx)
        if actpas not in rules:
            if len(rulelist) == 1:
                ruletup = rulelist[0]
            else:
                ruletup = tuple(rulelist)
            rules[actpas] = {ruletup}
        else:
            if len(rulelist) == 1:
                ruletup = rulelist[0]
            else:
                ruletup = tuple(rulelist)
            rules[actpas].add(ruletup)

def GOL(plants):
    minx, maxx = [min(plants)-2, max(plants)+3]
    newplants = set()
    for x in range(minx, maxx):
        neighlist = []
        for i in range(-2, 3):
            if i != 0:
                xi = x + i
                if xi in plants:
                    neighlist.append(i)
            elif x in plants:
                actpas = "act"
            else:
                actpas = "pas"
        if len(neighlist) == 1:
            neighs = neighlist[0]
        else:
            neighs = tuple(neighlist)
        for rule in rules:
            if rule[:3] == actpas and neighs in rules[rule]:
                change = rule[-3:]
                if change == "act":
                    newplants.add(x)
    return newplants

def part_one():
    newplants = set(plants)
    for i in range(20):
        newplants = GOL(newplants)
    print("Part One:", sum(newplants))

def part_two():
    newplants = set(plants)
    difgens = []
    for i in range(120): #Calculate additional plants for each generation
        #In this case plant growth steadies to +22 every generation after the
        #120th generation
        cursum = sum(newplants)
        newplants = GOL(newplants)
        newsum = sum(newplants)
        difgens.append(newsum - cursum)
    intersum = sum(newplants)
    steady = 22
    leftover = 50000000000 - 120
    addplants = leftover * steady
    finalsum = intersum + addplants
    print("Part Two:", finalsum)

day = 12
open_file()

format_data()

part_one()
part_two()