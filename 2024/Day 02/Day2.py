"""
Advent of Code
2024 Day 02

@author: Tom Herbert
"""

day = 2

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as f:
        reports = [[int(v) for v in l.strip().split()] for l in f.readlines()]
    return reports

def part_one(allDiffs):
    count = 0
    for diffs in allDiffs:
        if all(4 > d > 0 for d in diffs) or all(0 > d > -4 for d in diffs):
            count += 1
    print(f"Part One = {count}")

def part_two(allDiffs):
    count = 0
    for diffs in allDiffs:
        if all(4 > d > 0 for d in diffs) or all(0 > d > -4 for d in diffs):
            count += 1
            continue
        for j in range(len(diffs)+1):
            if j == 0:
                newDiffs = diffs[1:]
            elif j == len(diffs):
                newDiffs = diffs[:-1]
            else:
                newDiffs = [d for d in diffs]
                newVal = newDiffs[j-1] + newDiffs.pop(j)
                newDiffs[j-1] = newVal
            if all(4>d>0 for d in newDiffs) or all(0>d>-4 for d in newDiffs):
                count += 1
                break
    print(f"Part Two = {count}")

reports = open_file(day)
allDiffs = [[l[i+1] - l[i] for i in range(len(l)-1)] for l in reports]

part_one(allDiffs)
part_two(allDiffs)