"""
Advent of Code
2023 Day 5

@author: Tom Herbert
"""

day = 5

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = file.read().split("\n\n")
    return inputs

def read_input(inputs):
    maps = {}
    for i, block in enumerate(inputs):
        if not i:
            seeds = [int(val) for val in block.split(": ")[1].split(" ")]
            continue
        table = {}
        for j, line in enumerate(block.splitlines()):
            if not j:
                source, _, dest = line.split(" ")[0].split("-")
                maps[source] = [dest]
                continue
            d, s, l = [int(val) for val in line.split(" ")]
            table[s] = (l, d)
        maps[source].append(table)
    return seeds, maps

def translate(value, table):
    for start in sorted(table.keys()):
        length, end = table[start]
        if start <= value < start + length:
            value += end - start
            break
    return value

def split_ranges(left, right):
    newRanges = {}
    for source, length in left.items():
        for start, l in right.items():
            if source <= start < source + length:
                newRanges[source] = start - source
                length -= start - source
                newRanges[start] = min(length, l)
                length -= min(length, l)
                if length:
                    source = start + l
                else:
                    break
        if length:
            newRanges[source] = length
    return newRanges

def part_one(seeds, maps):
    current = "seed"
    values = [v for v in seeds]
    while current != "location":
        current, table = maps[current]
        values = [translate(v, table) for v in values]
    print(f"Part One = {min(values)}")

def part_two(seeds, maps):
    current = "seed"
    ranges = {seeds[i]: seeds[i+1] for i in range(0, len(seeds), 2)}
    while current != "location":
        left = dict(sorted(ranges.items()))
        current, table = maps[current]
        right = {source: table[source][0] for source in sorted(table.keys())}
        left = split_ranges(left, right)
        ranges = {translate(k, table): v for k, v in left.items()}
    print(f"Part Two = {min(ranges.keys())}")

inputs = open_file(day)

seeds, maps = read_input(inputs)

part_one(seeds, maps)
part_two(seeds, maps)