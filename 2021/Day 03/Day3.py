"""
Advent of Code
2021 Day 3

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [line.strip() for line in file.readlines()]
    file.close()
    return inputs

def format_data():
    global bitsums
    lenBinary = len(inputs[0])
    bitsums = [0] * lenBinary
    for line in inputs:
        bits = [int(char) for char in line]
        bitsums = list(map(lambda a, b: a+b, bitsums, bits))

def find_rating(bitStrings, idx, oxyOrCo2):
    if idx >= len(bitStrings[0]):
        print("Run out of bits to check")
        raise KeyboardInterrupt()
    count = 0
    for line in bitStrings:
        count += int(line[idx])
    if oxyOrCo2 == "O":
        if count >= len(bitStrings)/2:
            check = "1"
        else:
            check = "0"
    elif oxyOrCo2 == "C":
        if count >= len(bitStrings)/2:
            check = "0"
        else:
            check = "1"
    newList = []
    for line in bitStrings:
        if line[idx] == check:
            newList.append(line)
    if len(newList) > 1:
        newList = find_rating(newList, idx+1, oxyOrCo2)
    if len(newList) == 1:
        return newList
    else:
        print("No more values")
        raise KeyboardInterrupt()

def part_one():
    lenInput = len(inputs)
    lenBinary = len(bitsums)
    bitString = ""
    for bit in bitsums:
        if bit > lenInput/2:
            bitString += "1"
        else:
            bitString += "0"
    gamma = int(bitString, 2)
    epsilon = 2**lenBinary - 1 - gamma
    print(f"Part One = {gamma * epsilon}")

def part_two():
    oxy = list(inputs)
    co2 = list(inputs)
    oxy = int(find_rating(oxy, 0, "O").pop(), 2)
    co2 = int(find_rating(co2, 0, "C").pop(), 2)
    print(f"Part Two = {oxy * co2}") 

day = 3
inputs = open_file()

format_data()

part_one()
part_two()