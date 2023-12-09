"""
Advent of Code
2023 Day 9

@author: Tom Herbert
"""

day = 9

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip().split(" ") for line in file.readlines()]
    sequences = [[int(v) for v in line] for line in inputs]
    return sequences

def find_next(sequence):
    newSequence = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    if any(newSequence):
        add = find_next(newSequence)
        return add + sequence[-1]
    else:
        return sequence[-1]

def part_one_and_two(sequences):
    total = sum([find_next(sequence) for sequence in sequences])
    print(f"Part One = {total}")
    total = sum([find_next(sequence[::-1]) for sequence in sequences])
    print(f"Part Two = {total}")

sequences = open_file(day)

part_one_and_two(sequences)