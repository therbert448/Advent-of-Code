"""
Advent of Code
2022 Day 15

@author: Tom Herbert
"""

import time

day = 15

def open_file():
    #filename = "Day" + str(day) + "inputs.txt"
    filename = "test.txt"
    with open(filename) as file:
        inputs = [line.strip().split() for line in file.readlines()]
    return inputs

def format_data():
    global sensors
    sensors = []
    for line in inputs:
        _, _, sx, sy, _, _, _, _, bx, by = line
        coords = [sx, sy, bx, by]
        coords = [int(val.strip(", :").split("=")[-1]) for val in coords]
        distance = abs(coords[0] - coords[2]) + abs(coords[1] - coords[3])
        sensors.append([*coords, distance])

def check_row(row):
    for sensor in sensors:
        sx, sy, bx, by, distance = sensor
        if sy - distance > row or sy + distance < row:
            continue
        xwidth = distance - abs(sy - row)
        xrange = [sx - xwidth, sx + xwidth]
        if by == row and xrange[0] <= bx <= xrange[1]:
            if xrange[0] == bx and xrange[1] == bx:
                continue
            elif xrange[0] == bx:
                xrange[0] = bx + 1  
            elif xrange[1] == bx:
                xrange[1] = bx - 1
            else:
                leftRange = [xrange[0], bx - 1]
                rightRange = [bx + 1, xrange[1]]
                ranges.append(leftRange)
                ranges.append(rightRange)
                continue
        ranges.append(xrange)

def check_possible(row, xlims):
    possible = [xlims]
    for sensor in sensors:
        sx, sy, bx, by, distance = sensor
        if sy - distance > row or sy + distance < row:
            continue
        xwidth = distance - abs(sy - row)
        if sx - xwidth <= xlims[0] and sx + xwidth >= xlims[1]:
            return []
        xrange = [max(xlims[0], sx - xwidth), min(xlims[1], sx + xwidth)]
        newPossible = []
        for lims in possible:
            if lims[0] >= xrange[0] and lims[1] <= xrange[1]:
                continue
            if lims[0] < xrange[0] <= lims[1]:
                newPossible.append([lims[0], xrange[0]-1])
            if lims[0] <= xrange[1] < lims[1]:
                newPossible.append([xrange[1]+1, lims[1]])
            if max(lims) < min(xrange) or min(lims) > max(xrange):
                newPossible.append(lims)
        possible = list(newPossible)
        if not possible:
            return possible
    return possible

def sort_ranges():
    newRanges = []
    current = 0
    point = 1
    minMax = ranges[current]
    while current < len(ranges) and point < len(ranges):
        compare = ranges[point]
        if min(minMax) <= max(compare) and max(minMax) >= min(compare):
            minMax = [min(minMax+compare), max(minMax+compare)]
            point += 1
        else:
            current = point
            point += 1
            newRanges.append(minMax)
            minMax = ranges[current]
    newRanges.append(minMax)
    return newRanges

def part_one():
    global ranges
    ranges = []
    lineNo = 2_000_000
    check_row(lineNo)
    ranges.sort()
    ranges = sort_ranges()
    total = sum(x[1]-x[0]+1 for x in ranges)
    print(f"Part One = {total}")

def part_two():
    N = 4_000_000
    xlims = [0, N]
    for y in range(N+1):
        possible = check_possible(y, xlims)
        if not possible:
            continue
        else:
            x = possible[0][0]
            break
    result = x * N + y
    print(f"Part Two = {result}")

inputs = open_file()

format_data()

part_one()
start = time.perf_counter()
part_two()
end = time.perf_counter()

print(f"Part Two took {end-start} seconds")