"""
Advent of Code
2024 Day 22

@author: Tom Herbert
"""
from time import time

day = 22

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    return numbers

def evolve(num):
    toMix = num * 64
    num = prune(mix(num, toMix))
    toMix = num//32
    num = prune(mix(num, toMix))
    toMix = num * 2048
    num = prune(mix(num, toMix))
    return num

def mix(num, toMix):
    return num ^ toMix

def prune(num):
    return num % 16777216

def run_secret_number(num, N, i):
    prev = num % 10
    sequence = []
    for _ in range(N):
        num = evolve(num)
        current = num % 10
        change = current - prev
        sequence.append(change)
        if len(sequence) == 5: sequence.pop(0)
        if len(sequence) == 4:
            seq = tuple(sequence)
            if seq in sequences and i not in sequences[seq]:
                sequences[seq][i] = current
            elif seq not in sequences:
                sequences[seq] = {i: current}
        prev = current
    return num

numbers = open_file(day)

N = 2000

sequences = {}
total = 0
for i, num in enumerate(numbers):
    total += run_secret_number(num, N, i)
print(total)
result = max([sum(bananas.values()) for bananas in sequences.values()])
print(result)