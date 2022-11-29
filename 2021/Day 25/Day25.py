"""
Advent of Code
2021 Day 25

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [line.strip() for line in file.readlines()]
    file.close()
    return inputs

def format_data():
    global east, south, xmax, ymax
    east, south = set(), set()
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char == ">":
                east.add((x, y))
            elif char == "v":
                south.add((x, y))
    xmax, ymax = x+1, y+1

def move(east, south):
    moves = 0
    newEast = set()
    for cucumber in east:
        x, y = cucumber
        nextPos = ((x+1) % xmax, y)
        if nextPos in east or nextPos in south:
            newEast.add(cucumber)
            continue
        newEast.add(nextPos)
        moves += 1
    newSouth = set()
    for cucumber in south:
        x, y = cucumber
        nextPos = (x, (y+1) % ymax)
        if nextPos in newEast or nextPos in south:
            newSouth.add(cucumber)
            continue
        newSouth.add(nextPos)
        moves += 1
    return newEast, newSouth, moves

def print_grid(east, south):
    string = ""
    for y in range(ymax):
        for x in range(xmax):
            if (x, y) in east:
                string += ">"
            elif (x, y) in south:
                string += "v"
            else:
                string += "."
        string += "\n"
    print(string)

def part_one():
    moves = 0
    changes = 1
    newEast, newSouth = set(east), set(south)
    while changes:
        newEast, newSouth, changes = move(newEast, newSouth)
        moves += 1
    print(f"Part One = {moves}")

day = 25
inputs = open_file()

format_data()

part_one()