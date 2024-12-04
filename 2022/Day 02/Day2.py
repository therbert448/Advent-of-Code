"""
Advent of Code
2022 Day 2

@author: Tom Herbert

Version 1:
    Simply put all 9 possible matches into a dict with its resulting score
"""

day = 2

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        matches = [line.strip() for line in file.readlines()]
    return matches

def part_one():
    score = 0
    for match in matches:
        score += scores[match][0]
    print(f"Part One = {score}")

def part_two():
    score = 0
    for match in matches:
        score += scores[match][1]
    print(f"Part Two = {score}")

scores = {"A X": (4, 3), "A Y": (8, 4), "A Z": (3, 8),
          "B X": (1, 1), "B Y": (5, 5), "B Z": (9, 9),
          "C X": (7, 2), "C Y": (2, 6), "C Z": (6, 7)}

matches = open_file()

part_one()
part_two()