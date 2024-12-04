"""
Advent of Code
2022 Day 23

@author: Tom Herbert
"""

day = 23

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = file.readlines()
    return inputs

def format_data():
    global grid
    grid = set()
    for y, line in enumerate(inputs):
        for x, char in enumerate(line.strip()):
            if char == "#":
                grid.add((x, y))

def add(a, b): return a + b

def propose(elf):
    i = count % len(props)
    for j in range(len(props)):
        dire = props[(i+j) % len(props)]
        checking = [tuple(map(add, elf, tile)) for tile in dire]
        if any(tile in elves for tile in checking):
            continue
        else:
            return checking[0]
    return elf
        
def find_adjacent(elf):
    adjacent = [tuple(map(add, elf, adj)) for adj in around]
    if any(adj in elves for adj in adjacent):
        newElf = propose(elf)
    else:
        newElf = elf
    return newElf

def print_grid():
    xmin, xmax = min(xy[0] for xy in elves), max(xy[0] for xy in elves)
    ymin, ymax = min(xy[1] for xy in elves), max(xy[1] for xy in elves)
    string = ""
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if (x, y) in elves:
                string += "#"
            else:
                string += "."
        string += "\n"
    print(string)

def count_empty():
    xmin, xmax = min(xy[0] for xy in elves), max(xy[0] for xy in elves)
    ymin, ymax = min(xy[1] for xy in elves), max(xy[1] for xy in elves)
    total = 0
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if (x, y) not in elves:
                total += 1
    return total

def run_elves():
    nextElves = {}
    overlaps = set()
    for elf in elves:
        newElf = find_adjacent(elf)
        if newElf in nextElves:
            other = nextElves[newElf]
            nextElves[other] = other
            nextElves[elf] = elf
            overlaps.add(newElf)
            del nextElves[newElf]
        elif newElf in overlaps:
            nextElves[elf] = elf
        else:
            nextElves[newElf] = elf
    newElves = set(nextElves.keys())
    if elves == newElves:
        return
    return newElves

def iterate_elves(partTwo = False, N = 10):
    global count, elves
    count = 0
    elves = set(grid)
    if partTwo:
        while True:
            newElves = run_elves()
            if newElves == None:
                count += 1
                break
            elves = newElves
            count += 1
    else:
        while count < N:
            newElves = run_elves()
            if newElves == None:
                count += 1
                break
            elves = newElves
            count += 1

def part_one():
    iterate_elves()
    total = count_empty()
    print(f"Part One = {total}")

def part_two():
    iterate_elves(True)
    print(f"Part Two = {count}")

inputs = open_file()

format_data()

around = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
props = [[(0, -1), (-1, -1), (1, -1)],
         [(0, 1), (-1, 1), (1, 1)],
         [(-1, 0), (-1, -1), (-1, 1)],
         [(1, 0), (1, -1), (1, 1)]
         ]

part_one()
part_two()