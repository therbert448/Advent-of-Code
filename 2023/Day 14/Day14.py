"""
Advent of Code
2023 Day 14

@author: Tom Herbert
"""

day = 14

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        rows = [line.strip() for line in file.readlines()]
    return rows

def rows_to_columns(rows):
    cols = [""] * len(rows[0])
    for line in rows:
        for x, char in enumerate(line):
            cols[x] += char
    return cols

def fall_north(rows):
    cols = rows_to_columns(rows)
    newCols = []
    for c in cols:
        c = "#".join(["".join(sorted(s, reverse=True)) for s in c.split("#")])
        newCols.append(c)
    rows = rows_to_columns(newCols)
    return rows

def rotate(rows):
    yMax, xMax = len(rows), len(rows[0])
    newRows = [""] * xMax
    for y in range(yMax):
        for x in range(xMax):
            newRows[y] += rows[xMax-x-1][y]
    return newRows

def find_result(rows):
    total = 0
    for y, row in enumerate(rows):
        val = len(rows) - y
        for char in row:
            if char == "O":
                total += val
    return total

def part_one(rows):
    newRows = fall_north(rows)
    result = find_result(newRows)
    print(f"Part One = {result}")                

def part_two(rows):
    states, N, results = {}, 1_000_000_000, []
    for i in range(N):
        for _ in range(4):
            rows = fall_north(rows)
            rows = rotate(rows)
        grid = "\n".join(rows)
        results.append(find_result(rows))
        if grid in states:
            break
        states[grid] = i
    remainder = (N - 1 - states[grid]) % (i - states[grid])
    idx = (states[grid] + remainder) % (i-1)
    result = results[idx]
    print(f"Part Two = {result}")

rows = open_file(day)

part_one(rows)
part_two(rows)