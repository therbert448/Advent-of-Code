"""
Advent of Code
2021 Day 1

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def format_data():
    global octopuses
    octopuses = {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line.strip()):
            octopuses[(x, y)] = int(char)

def add_energy(octopi):
    octopi = {k:v+1 for k, v in octopi.items()}
    return octopi

def neighbours(pos):
    add = lambda a, b: a + b
    adjacent = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    neighs = [tuple(map(add, adj, pos)) for adj in adjacent]
    for n in list(neighs):
        if n not in octopuses:
            neighs.remove(n)
    return neighs

def flash(pos, flashed, octopi):
    flashed.add(pos)
    neighs = neighbours(pos)
    for n in neighs:
        octopi[n] += 1
    for n in neighs:
        if octopi[n] > 9 and n not in flashed:
            flashed, octopi = flash(n, flashed, octopi)
    return flashed, octopi

def part_one():
    count = 0
    octopi = dict(octopuses)
    for i in range(100):
        flashed = set()
        octopi = add_energy(octopi)
        for pos, val in octopi.items():
            if val > 9 and pos not in flashed:
                flashed, octopi = flash(pos, flashed, octopi)
        for pos, val in octopi.items():
            if val > 9:
                octopi[pos] = 0
        count += len(flashed)
    print(f"Part One = {count}")

def part_two():
    iteration = 0
    octopi = dict(octopuses)
    simultaneous = 0
    while not simultaneous:
        iteration += 1
        flashed = set()
        octopi = add_energy(octopi)
        for pos, val in octopi.items():
            if val > 9 and pos not in flashed:
                flashed, octopi = flash(pos, flashed, octopi)
        for pos, val in octopi.items():
            if val > 9:
                octopi[pos] = 0
        if len(flashed) == len(octopi.keys()):
            simultaneous = 1
            break
    print(f"Part Two = {iteration}")

day = 11
inputs = open_file()

format_data()

part_one()
part_two()