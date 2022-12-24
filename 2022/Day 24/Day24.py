"""
Advent of Code
2022 Day 24

@author: Tom Herbert
"""

day = 24

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = file.readlines()
    return inputs

def format_data():
    global grid, blizzards, start, end, xmax, ymax
    grid = set()
    blizzards = set()
    for y, line in enumerate(inputs):
        for x, char in enumerate(line.strip()):
            if char == "#":
                continue
            else:
                grid.add((x, y))
                if char != ".":
                    blizzards.add(((x, y), char))
    start = (1, 0)
    end = (x-1, y)
    xmax, ymax = x, y

def add(a, b): return a+b

def move_blizzards(blizz):
    copyBlizzards = set(blizz)
    newBlizzards = set()
    for blizzard in copyBlizzards:
        pos, dire = blizzard 
        newPos = tuple(map(add, pos, dires[dire]))
        if newPos not in grid:
            x, y = newPos
            if x <= 0: x = xmax-1
            if y <= 0: y = ymax-1
            if x >= xmax: x = 1
            if y >= ymax: y = 1
            newPos = (x, y)
        newBlizzards.add((newPos, dire))
    return newBlizzards

def unsafe_tiles(blizz):
    unsafe = set()
    for blizzard in blizz:
        pos, _ = blizzard
        unsafe.add(pos)
    return unsafe

def find_moves(pos):
    newMoves = [tuple(map(add, pos, move)) for move in moves]
    viable = []
    for m in newMoves:
        if m in grid and m not in unsafe:
            viable.append(m)
    return viable

def pass_time(current, blizz):
    global unsafe
    blizz = move_blizzards(blizz)
    unsafe = unsafe_tiles(blizz)
    newCurrent = set()
    for pos in current:
        nextMoves = find_moves(pos)
        newCurrent.update(set(nextMoves))
    return newCurrent, blizz

def part_one_and_two():
    current = {start}
    t = 0
    blizz = set(blizzards)
    while end not in current:
        current, blizz = pass_time(current, blizz)
        t += 1
    print(f"Part One = {t}")
    current = {end}
    while start not in current:
        current, blizz = pass_time(current, blizz)
        t += 1
    current = {start}
    while end not in current:
        current, blizz = pass_time(current, blizz)
        t += 1
    print(f"Part Two = {t}")

inputs = open_file()

format_data()

dires = {">": (1, 0), "v": (0, 1), "<": (-1,0), "^": (0, -1)}
moves = {(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)}

part_one_and_two()