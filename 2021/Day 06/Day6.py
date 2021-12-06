"""
Advent of Code
2021 Day 6

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [int(val) for val in file.read().split(",")]
    file.close()
    return inputs

def format_data():
    global school
    school = {}
    for i in range(9):
        school[i] = sum([1 for timer in inputs if timer == i])

def new_day(school):
    newSchool = {k-1: v for k, v in school.items()}
    if -1 in newSchool:
        new = newSchool[-1]
        newSchool[8] = new
        newSchool[6] += new
        newSchool.pop(-1)
    return newSchool

def part_one():
    newSchool = dict(school)
    for i in range(80):
        newSchool = new_day(newSchool)
    totalFish = sum(newSchool.values())
    print(f"Part One = {totalFish}")

def part_two():
    newSchool = dict(school)
    for i in range(256):
        newSchool = new_day(newSchool)
    totalFish = sum(newSchool.values())
    print(f"Part Two = {totalFish}")

day = 6
inputs = open_file()

format_data()

part_one()
part_two()