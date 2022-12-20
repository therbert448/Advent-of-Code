"""
Advent of Code
2022 Day 20

@author: Tom Herbert
"""

day = 20

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [int(line.strip()) for line in file.readlines()]
    return inputs

def copy_inputs(inputs): #copy of original list, to be mixed up
    global copy
    copy = [(value, i) for i, value in enumerate(inputs)]
    # Real inputs have duplicate values, so make a tuple with the index for
    # unique values

def mix(i, value, inputs): 
    # value is the number to move, i is the original index, where value is in inputs
    copyidx = copy.index((value, i))
    # find the current position of the value, idx tuple
    end = (copyidx + value) % (len(inputs) - 1)
    # find the position to move the value to (list will be shorter after pop)
    toMove = copy.pop(copyidx) # pop value from list
    copy.insert(end, toMove) # insert value in new position in list

def score(inputs):
    total = 0
    initialIdx = inputs.index(0)
    zeroIdx = copy.index((0, initialIdx))
    for i in range(3):
        jump = ((i+1) * 1_000) % len(inputs)
        jumpIdx = (zeroIdx + jump) % len(inputs)
        value, _ = copy[jumpIdx]
        total += value
    return total

def part_one():
    copy_inputs(inputs)
    for i, value in enumerate(inputs):
        mix(i, value, inputs)
    total = score(inputs)
    print(f"Part One = {total}")

def part_two():
    N = 811589153
    newInputs = [v * N for v in inputs]
    copy_inputs(newInputs)
    for _ in range(10):
        for i, value in enumerate(newInputs):
            mix(i, value, newInputs)
    total = score(newInputs)
    print(f"Part Two = {total}")

inputs = open_file()

part_one()
part_two()