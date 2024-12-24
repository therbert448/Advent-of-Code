"""
Advent of Code
2024 Day 19

@author: Tom Herbert
"""
from time import time

day = 19

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        towels, patterns = file.read().split("\n\n")
    towelDict = {"w": [], "u": [], "b": [], "r": [], "g": []}
    for towel in towels.strip().split(", "):
        towelDict[towel[0]].append((towel, len(towel)))
    patterns = [line.strip() for line in patterns.splitlines()]
    return towelDict, patterns

def match_pattern(pattern):
    if pattern in possiblePatterns: 
        return possiblePatterns[pattern]
    else:
        possiblePatterns[pattern] = 0
    start = pattern[0]
    for towel, length in towelDict[start]:
        if pattern == towel:
            possiblePatterns[pattern] += 1
        elif pattern[:length] == towel:
            possiblePatterns[pattern] += match_pattern(pattern[length:])
    return possiblePatterns[pattern]

towelDict, patterns = open_file(day)

possiblePatterns = {}
partOne = 0
partTwo = 0
for pattern in patterns:
    count = match_pattern(pattern)
    if count: 
        partOne += 1
        partTwo += count
print(partOne)
print(partTwo)