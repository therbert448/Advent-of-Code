"""
Advent of Code
2022 Day 15

@author: Tom Herbert

Reworked from original solution with a different method. This version of Part
Two is much faster, taking less than a second, compared to nearly a minute 
before.

Previous solution from Part Two utilised the logic of Part One, but instead of
finding the "no beacon" zone(s) for a given line, it returned the "possible 
beacon" zone for each line. If such a zone existed for any row, that was the 
answer.
This was inefficient because it still had to iterate down each of the 4,000,000
rows until an answer was found.

This new solution doesn't have to consider the 4,000,000 x 4,000,000 grid, 
except to enforce limits. Instead it looks at the perimeter of each sensor's 
"no beacon" zone.
It draws a line over each of the 4 outside edges of the "no beacon" zone for 
each sensor, then finds all the points where the lines of any sensor intersect 
with the lines of any other sensor. If any of these points are outside the grid, 
they are discarded.
The points remaining are then checked against every sensor, making sure they 
aren't positioned in any "no beacon" zones. The first intersection point that
is in the grid and isn't in any "no beacon" zone is the answer.
"""

day = 15

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
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

def y_intercepts():
    global intercepts
    intercepts = []
    for sensor in sensors:
        sx, sy, _, _, distance = sensor
        a = sy - sx - distance - 1
        b = sy - sx + distance + 1
        c = sy + sx - distance - 1
        d = sy + sx + distance + 1
        intercepts.append([a, b, c, d])
    
def intersections(lim):
    y_intercepts()
    for i, sensor in enumerate(intercepts):
        a, b, c, d  = sensor
        down1, up1 = [a, b], [c, d]
        for other in intercepts[i+1:]:
            e, f, g, h  = other
            down2, up2 = [e, f], [g, h]
            ups = [up1, up2]
            downs = [down1, down2]
            for j in range(2):
                for up in ups[j]:
                    for down in downs[1-j]:
                        y = (up + down)//2
                        x = up - y
                        if x < lim[0] or x > lim[1] or y < lim[0] or y > lim[1]:
                            continue
                        answer = True
                        for sensor in sensors:
                            sx, sy, _, _, distance = sensor
                            if abs(sx - x) + abs(sy - y) <= distance:
                                answer = False
                                break
                        if answer:
                            return (x, y)

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
    lim = [0, N]
    x, y = intersections(lim)
    result = x * N + y
    print(f"Part Two = {result}")

inputs = open_file()

format_data()

part_one()
part_two()