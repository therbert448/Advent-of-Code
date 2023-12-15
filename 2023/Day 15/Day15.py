"""
Advent of Code
2023 Day 15

@author: Tom Herbert
"""

day = 15

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = file.read().split(",")
    return inputs

def HASH(string):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

def HASHMAP(inputs):
    boxes = {}
    for string in inputs:
        if "=" in string:
            label, focal = string.split("=")
            focal = int(focal)
            value = HASH(label)
            if value not in boxes: boxes[value] = {}
            boxes[value][label] = focal
        else:
            label = string.strip("-")
            value = HASH(label)
            if value not in boxes: boxes[value] = {}
            if label in boxes[value]:
                del boxes[value][label] 
    return boxes

def focusing_power(boxes):
    result = 0
    for value in boxes:
        for i, label in enumerate(boxes[value].keys()):
            focal = boxes[value][label]
            result += (value + 1) * (i + 1) * focal
    return result

def part_one(inputs):
    result = sum([HASH(string) for string in inputs])
    print(f"Part One = {result}")

def part_two(inputs):
    boxes = HASHMAP(inputs)
    result = focusing_power(boxes)
    print(f"Part Two = {result}")

inputs = open_file(day)

part_one(inputs)
part_two(inputs)