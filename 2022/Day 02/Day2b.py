"""
Advent of Code
2022 Day 2

@author: Tom Herbert

Version 2:
    Translate the letters into indices
    The score of each round can be determined with a single line equation,
    using the indices and mod 3
"""

day = 2

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        matches = [line.strip().split() for line in file.readlines()]
    return matches

def part_one():
    score = 0
    for match in matches:
        opp, pick = [indices[val] for val in match]
        score += (((pick - opp + 1) % 3) * 3) + pick + 1
    print(f"Part One = {score}")

def part_two():
    score = 0
    for match in matches:
        opp, outcome = [indices[val] for val in match]
        score += (outcome * 3) + ((outcome - 1 + opp) % 3) + 1
    print(f"Part Two = {score}")

indices = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}

matches = open_file()

part_one()
part_two()