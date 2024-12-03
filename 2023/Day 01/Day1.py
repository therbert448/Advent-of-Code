"""
Advent of Code
2023 Day 1

@author: Tom Herbert
"""

day = 1

words = {"one": 'o1e', "two": 't2o', "three": 'th3ee', "four": 'f4ur', 
         "five": 'fi5e', "six": 's6x', "seven": 'se7en', "eight": 'ei8ht', 
         "nine": 'ni9e'}

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    return inputs

def part_one(inputs):
    total = 0
    for line in inputs:
        nums = [char for char in line if char.isnumeric()]
        total += int(nums[0] + nums[-1])
    print(f"Part One = {total}")

def part_two(inputs):
    total = 0
    for line in inputs:
        for word, rep in words.items():
            line = line.replace(word, rep)
        nums = [char for char in line if char.isnumeric()]
        total += int(nums[0] + nums[-1])
    print(f"Part Two = {total}")

inputs = open_file(day)

part_one(inputs)
part_two(inputs)