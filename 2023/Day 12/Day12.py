"""
Advent of Code
2023 Day 12

@author: Tom Herbert
"""

day = 12

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    lines, combos = [], []
    for line in inputs:
        springs, combo = line.split(" ")
        combo = tuple([int(val) for val in combo.split(",")])
        lines.append(springs), combos.append(combo)
    return lines, combos

def find_combos(springs, combo):
    state = (springs, combo)
    if state in states: #If state has been seen before
        return states[state]
    #If successfully finished reducing springs and combos
    if not len(springs) and not len(combo):
        states[state] = 1
        return states[state]
    elif not len(springs): #If no springs left for combo
        states[state] = 0
        return states[state]
    #Check current run
    char = springs[0]
    if char == "?": #Spring is unknown
        brokenSpring = springs[1:] #Possibilities if spring is broken
        operSpring = "#" + springs[1:] #and if spring is operational
        broken = find_combos(brokenSpring.strip("."), combo)
        operational = find_combos(operSpring, combo)
        states[state] = broken + operational
        return states[state]
    else: #Spring is operational
        if not combo or len(springs) < combo[0]:
            pass #Nothing to match spring with
        elif "." in springs[:combo[0]]:
            pass #Broken spring in run
        elif springs[combo[0]:] and springs[combo[0]] == "#":
            pass #Working spring immediately after run
        else:
            newSprings = springs[combo[0]+1:]
            states[state] = find_combos(newSprings.strip("."), combo[1:])
            return states[state]
        states[state] = 0
        return states[state]

def part_one(lines, combos):
    result = 0
    for i in range(len(lines)):
        springs, combo = lines[i].strip("."), combos[i]
        result += find_combos(springs, combo)
    print(f"Part One = {result}")

def part_two(liness, combos):
    result = 0
    for i in range(len(lines)):
        springs, combo = lines[i], combos[i]
        springs = "?".join([springs] * 5).strip(".")
        combo = combo * 5
        result += find_combos(springs, combo)
    print(f"Part Two = {result}")

lines, combos = open_file(day)

states = {}

part_one(lines, combos)
part_two(lines, combos)