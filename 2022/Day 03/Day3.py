"""
Advent of Code
2022 Day 3

@author: Tom Herbert
"""

day = 3

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    return inputs

def part_one():
    compartments = []
    for line in inputs:
        mid = len(line)//2
        compartments.append([set(line[:mid]), set(line[mid:])])
    priorities = []
    for comp in compartments:
        a, b = comp
        (duplicate, ) = a.intersection(b)
        priority = ord(duplicate.lower()) - 96
        if duplicate.isupper():
            priority += 26
        priorities.append(priority)
    print(f"Part One = {sum(priorities)}")

def part_two():
    bags = []
    for line in inputs:
        bags.append(set(line))
    badgePriorities = []
    for i in range(len(bags)//3):
        a, b, c = bags[i*3:i*3 + 3]
        (badge, ) = a.intersection(b, c)
        priority = ord(badge.lower()) - 96
        if badge.isupper():
            priority += 26
        badgePriorities.append(priority)
    print(f"Part Two = {sum(badgePriorities)}")

inputs = open_file()

part_one()
part_two()
