"""
Advent of Code
2021 Day 10

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [line.strip() for line in file.readlines()]
    file.close()
    return inputs

def part_one():
    global missing #for part two
    missing = set()
    score = 0
    for line in inputs:
        corrupt = 0
        opening = []
        for char in line:
            if char in openBrackets:
                opening.append(char)
            elif char == matching[opening[-1]]:
                opening.pop()
            else:
                corrupt = 1
                score += corruptScores[char]
                break
        if not corrupt: #record sequence of closing characters for valid lines
            missing.add(tuple([matching[char] for char in opening[::-1]]))
    print(f"Part One = {score}")

def part_two():
    scores = []
    for line in missing: #using closing characters determined in part one
        lineScore = 0
        for char in line:
            lineScore *= 5
            lineScore += incompleteScores[char]
        scores.append(lineScore)
    scores.sort()
    middleScore = scores[(len(scores)-1)//2]
    print(f"Part Two = {middleScore}")

day = 10
inputs = open_file()

openBrackets = {"(", "[", "{", "<"}
matching = {"(":")", "[":"]", "{":"}", "<":">"}
corruptScores = {")": 3, "]": 57, "}": 1197, ">": 25137}
incompleteScores = {")": 1, "]": 2, "}": 3, ">": 4}

part_one()
part_two()