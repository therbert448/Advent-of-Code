"""
Advent of Code
2022 Day 1

@author: Tom Herbert
"""

def open_file():
    with open("Day" + str(day) + "inputs.txt") as file:
        inputs = file.read().split("\n\n")
    return inputs

def format_data():
    global elves
    elves = sorted([sum(map(int, l.strip().split())) for l in inputs])

def part_one():
    print(f"Part One = {max(elves)}")

def part_two():
    print(f"Part Two = {sum(elves[-3:])}")

day = 1
inputs = open_file()

format_data()

part_one()
part_two()
