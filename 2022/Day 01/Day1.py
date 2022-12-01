"""
Advent of Code
2022 Day 1

@author: Tom Herbert
"""

with open("Day1inputs.txt") as file:
    elves = sorted(sum(map(int, l.split())) for l in file.read().split("\n\n"))
print(f"Part One = {max(elves)}")
print(f"Part Two = {sum(elves[-3:])}")