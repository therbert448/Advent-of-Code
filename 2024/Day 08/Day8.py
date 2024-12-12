"""
Advent of Code
2024 Day 08

@author: Tom Herbert
"""
from time import time

day = 8

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    frequencies = {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char == ".": continue
            if char in frequencies: frequencies[char].append(x + 1j*y)
            else: frequencies[char] = [x + 1j*y]
    return frequencies, x, y

def HCF(vector):
    a, b = int(vector.real), int(vector.imag)
    common = 0
    for val in range(1, min(a, b) + 1):
        if not a % val and not b % val:
            common = val
    if common:
        a, b = a//common, b//common
    return a + 1j*b

frequencies, xmax, ymax = open_file(day)
t0 = time()
vectors = {}
for freq, freqList in frequencies.items():
    vectors[freq] = []
    for i, coordA in enumerate(freqList):
        for coordB in freqList[i+1:]:
            diff = coordA - coordB
            vectors[freq].append((coordA, diff))

antinodes = set()
for freq, diffList in vectors.items():
    for pair in diffList:
        start, vector = pair
        a = start - (2*vector)
        if 0 <= a.real <= xmax and 0 <= a.imag <= ymax:
            antinodes.add(a)
        b = start + vector
        if 0 <= b.real <= xmax and 0 <= b.imag <= ymax:
            antinodes.add(b)

print(len(antinodes))
t1 = time()
print(t1 - t0)
antinodes = set()
for freq, diffList in vectors.items():
    for pair in diffList:
        start, vector = pair
        vector = HCF(vector)
        current = start
        while 0 <= current.real <= xmax and 0 <= current.imag <= ymax:
            antinodes.add(current)
            current += vector
        current = start - vector
        while 0 <= current.real <= xmax and 0 <= current.imag <= ymax:
            antinodes.add(current)
            current -= vector

print(len(antinodes))
t2 = time()
print(t2-t1)