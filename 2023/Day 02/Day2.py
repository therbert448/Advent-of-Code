"""
Advent of Code
2022 Day 25

@author: Tom Herbert
"""

day = 2

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    return inputs

def read_games(inputs):
    games = {}
    for line in inputs:
        gameID, sets = line.split(": ")
        _, gameID = gameID.split(" ")
        sets = sets.split("; ")
        setList = []
        for s in sets:
            balls = s.split(", ")
            ballsDict = {}
            for ball in balls:
                num, colour = ball.split(" ")
                ballsDict[colour] = int(num)
            setList.append(ballsDict)
        games[int(gameID)] = setList
    return games

def product(args):
    total = 1
    for arg in args:
        total *= arg
    return total

def part_one(games, limits):
    total = 0
    for gameID, game in games.items():
        valid = True
        for gameSet in game:
            for colour, num in gameSet.items():
                if num > limits[colour]:
                    valid = False
                    break
            if not valid:
                break
        if valid: total += gameID
    print(f"Part One = {total}")

def part_two(games):
    total = 0
    for game in games.values():
        minBalls = {"red": 0, "green": 0, "blue": 0}
        for gameSet in game:
            for colour, num in gameSet.items():
                if num > minBalls[colour]:
                    minBalls[colour] = num
        power = product(list(minBalls.values()))
        total += power
    print(f"Part Two = {total}")

inputs = open_file(day)
games = read_games(inputs)

limits = {"red": 12, "green": 13, "blue": 14}

part_one(games, limits)
part_two(games)