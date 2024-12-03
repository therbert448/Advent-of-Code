"""
Advent of Code
2023 Day 2

@author: Tom Herbert
"""

day = 2

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    return inputs

def read_games(inputs):
    idcs = ["red", "green", "blue"]
    games = []
    for line in inputs:
        gameID, sets = line.split(": ")
        _, gameID = gameID.split(" ")
        sets = sets.split("; ")
        game = [0, 0, 0]
        for s in sets:
            cubes = s.split(", ")
            for cube in cubes:
                num, colour = cube.split(" ")
                if int(num) > game[idcs.index(colour)]:
                    game[idcs.index(colour)] = int(num)
        games.append(game)
    return games

def product(args):
    total = 1
    for arg in args:
        total *= arg
    return total

def part_one(games, limits):
    total = 0
    for i, game in enumerate(games):
        if all([game[j] <= limits[j] for j in range(len(game))]):
            total += i + 1
    print(f"Part One = {total}")

def part_two(games):
    total = 0
    for game in games:
        total += product(game)
    print(f"Part Two = {total}")

inputs = open_file(day)
games = read_games(inputs)

limits = [12, 13, 14]

part_one(games, limits)
part_two(games)