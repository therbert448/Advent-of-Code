"""
Advent of Code
2021 Day 24

@author: Tom Herbert

Digit 1: add 7
Digit 2: add 8
Digit 3: add 2
Digit 4: add 11
Digit 5: compare to (digit 4) + 11 - 3
Digit 6: add 12
Digit 7: add 14
Digit 8: compare to (digit 7) + 14 - 16
Digit 9: add 15
Digit 10: compare to (digit 9) + 15 - 8
Digit 11: compare to (digit 6) + 12 - 12
Digit 12: compare to (digit 3) + 2 - 7
Digit 13: compare to (digit 2) + 8 - 6
Digit 14: compare to (digit 1) + 7 - 11

1 and 14:   (14) = (1) - 4.   Max: (1) = 9, (14) = 5.   Min: (1) = 5, (14) = 1
2 and 13:   (13) = (2) + 2.   Max: (2) = 7, (13) = 9.   Min: (2) = 1, (13) = 3
3 and 12:   (12) = (3) - 5.   Max: (3) = 9, (12) = 4.   Min: (3) = 1, (12) = 6
6 and 11:   (11) = (6).       Max: (6) = 9, (11) = 9.   Min: (6) = 1, (11) = 1
9 and 10:   (10) = (9) + 7.   Max: (9) = 2, (10) = 9.   Min: (9) = 1, (10) = 8
7 and 8:    (8) = (7) - 2.    Max: (7) = 9, (8) = 7.    Min: (7) = 3, (8) = 1
4 and 5:    (5) = (4) + 8.    Max: (4) = 1, (5) = 9.    Min: (4) = 1, (5) = 9
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [line.strip().split() for line in file.readlines()]
    file.close()
    return inputs

def format_data():
    global steps
    steps = []
    for line in inputs:
        command, *args = line
        steps.append([command, args])

def inp(reg):
    if reg not in registers:
        return
    if modelNumber:
        registers[reg] = modelNumber.pop(0)
    else:
        val = int(input("Enter a Digit: "))
        registers[reg] = val

def add(reg, b):
    if reg not in registers:
        return
    a = registers[reg]
    if b in registers:
        b = registers[b]
    else:
        b = int(b)
    registers[reg] = a + b

def mul(reg, b):
    if reg not in registers:
        return
    a = registers[reg]
    if b in registers:
        b = registers[b]
    else:
        b = int(b)
    registers[reg] = a * b

def div(reg, b):
    if reg not in registers:
        return
    a = registers[reg]
    if b in registers:
        b = registers[b]
    else:
        b = int(b)
    registers[reg] = a//b

def mod(reg, b):
    if reg not in registers:
        return
    a = registers[reg]
    if b in registers:
        b = registers[b]
    else:
        b = int(b)
    registers[reg] = a % b

def eql(reg, b):
    if reg not in registers:
        return
    a = registers[reg]
    if b in registers:
        b = registers[b]
    else:
        b = int(b)
    if a == b:
        registers[reg] = 1
    else:
        registers[reg] = 0

def run_steps():
    for line in steps:
        command, args = line
        command += "(*args)"
        eval(command)

def part_one():
    global modelNumber, registers
    answer = 97919997299495 #From above
    registers = {"w":0, "x": 0, "y": 0, "z": 0}
    modelNumber = [int(val) for val in str(answer)]
    run_steps()
    if registers["z"] == 0:
        print(f"Part One = {answer}")

def part_two():
    global modelNumber, registers
    answer = 51619131181131 #From above
    registers = {"w":0, "x": 0, "y": 0, "z": 0}
    modelNumber = [int(val) for val in str(answer)]
    run_steps()
    if registers["z"] == 0:
        print(f"Part One = {answer}")

day = 24
inputs = open_file()

format_data()

part_one()
part_two()