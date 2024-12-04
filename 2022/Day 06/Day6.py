"""
Advent of Code
2022 Day 6

@author: Tom Herbert
"""

day = 6

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        stream = [char for char in file.read().strip()]
    return stream

def find_marker(n, part):
    for i in range(len(stream)-n):
        marker = set(stream[i:i+n])
        if len(marker) == n:
            break
    print(f"Part {part} = {i+n}")

stream = open_file()

find_marker(4, "One")
find_marker(14, "Two")
