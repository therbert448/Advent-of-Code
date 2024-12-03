"""
Advent of Code
2023 Day 6

@author: Tom Herbert
"""

day = 6

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    races = [[int(v) for v in l.split(":")[1].strip().split()] for l in inputs]
    return races

def quadratic(time, record):
    disc = time**2 - (4 * record)
    lower = int(((time - pow(disc, 0.5))/2) + 1)
    score = time - (2 * lower) + 1
    return score

def run_races(races):
    times, records = races
    total = 1
    for i, time in enumerate(times):
        record = records[i]
        total *= quadratic(time, record)
    return total

def part_one_and_two(races):
    print(f"Part One = {run_races(races)}")
    races = [[int("".join([str(val) for val in line]))] for line in races]
    print(f"Part Two = {run_races(races)}")

races = open_file(day)

part_one_and_two(races)