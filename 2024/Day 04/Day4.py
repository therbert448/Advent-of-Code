"""
Advent of Code
2024 Day 04

@author: Tom Herbert
"""

day = 4

def open_file(day):
    #filename = "test2.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def part_one(grid, dimx, dimy):
    word = "XMAS"
    count = 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if line[x:x+4] == word: count += 1
            if line[x:x+4][::-1] == word: count += 1
            if y+4 <= dimy:
                string = "".join([grid[y+i][x] for i in range(4)])
                if string == word: count += 1
                if string[::-1] == word: count += 1
                if x+4 <= dimx:
                    string = "".join([grid[y+i][x+i] for i in range(4)])
                    if string == word: count += 1
                    if string[::-1] == word: count += 1
                if x >= 3:
                    string = "".join([grid[y+i][x-i] for i in range(4)])
                    if string == word: count += 1
                    if string[::-1] == word: count += 1
    print(f"Part One = {count}")

def part_two(grid, dimx, dimy):
    word = "MAS"
    count = 0
    for y in range(1, dimy-1):
        for x in range(1, dimx-1):
            up = grid[y+1][x-1] + grid[y][x] + grid[y-1][x+1]
            down = grid[y-1][x-1] + grid[y][x] + grid[y+1][x+1]
            if word in (up, up[::-1]) and word in (down, down[::-1]):
                count += 1
    print(f"Part Two = {count}")

grid = open_file(day)
dimx, dimy = len(grid[0]), len(grid)

part_one(grid, dimx, dimy)
part_two(grid, dimx, dimy)