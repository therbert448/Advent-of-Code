"""
Advent of Code
2023 Day 13

@author: Tom Herbert
"""

day = 13

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [block.splitlines() for block in file.read().split("\n\n")]
    return inputs

def find_reflection(pattern, partTwo = False):
    for i in range(len(pattern)):
        top = pattern[i::-1]
        bottom = pattern[i+1:]
        length = min(len(top), len(bottom))
        if not length: continue
        top = "\n".join(top[:length])
        bottom = "\n".join(bottom[:length])
        if top == bottom and not partTwo:
            return i + 1
        elif top != bottom and partTwo:
            count = 0
            for j, char in enumerate(top):
                if char != bottom[j]:
                    count += 1
                if count > 1:
                    break
            if count == 1:
                return i + 1
    return False

def transpose(pattern):
    newPattern = []
    for i in range(len(pattern[0])):
        string = ""
        for j in range(len(pattern)):
            string += pattern[j][i]
        newPattern.append(string)
    return newPattern

def part_one_and_two(inputs, partTwo = False):
    rowCount, columnCount = 0, 0
    for pattern in inputs:
        row = find_reflection(pattern, partTwo)
        if row:
            rowCount += row
        else:
            columnCount += find_reflection(transpose(pattern), partTwo)
    result = columnCount + (100 * rowCount)
    if partTwo: 
        print(f"Part Two = {result}") 
    else: print(f"Part One = {result}")

inputs = open_file(day)

part_one_and_two(inputs)
part_one_and_two(inputs, True)