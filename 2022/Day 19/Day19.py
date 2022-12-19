"""
Advent of Code
2022 Day 19

@author: Tom Herbert
"""

import time

day = 19

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip().split(" ") for line in file.readlines()]
    return inputs

def format_data():
    global blueprints
    blueprints = []
    for line in inputs:
        oreCost = [int(line[6]), 0, 0]
        clayCost = [int(line[12]), 0, 0]
        obsidianCost = [int(line[18]), int(line[21]), 0]
        geodeCost = [int(line[27]), 0, int(line[30])]
        blueprints.append([oreCost, clayCost, obsidianCost, geodeCost])

def make_robots(state, blueprint, time):
    newStates = {tuple(state)}
    if all(state[i] >= blueprint[-1][i] for i in range(3)):
        if all(state[j+4] >= blueprint[-1][j] for j in range(3)):
            newState = list(state)
            newState[-1] += 1
            for k, ore in enumerate(blueprint[-1]):
                newState[k+4] -= ore
            newStates = {tuple(newState)}
        return newStates
    for i, robot in enumerate(blueprint):
        if i < 3 and state[i] >= max(blue[i] for blue in blueprint):
            continue
        if i < 3 and state[i+4] >= max(blue[i] for blue in blueprint) * time:
            continue
        if all(state[j+4] >= robot[j] for j in range(len(robot))):
            newState = list(state)
            newState[i] += 1
            for k, ore in enumerate(robot):
                newState[k+4] -= ore
            newStates.add(tuple(newState))
    return newStates

def pass_time(current, t, bp, minMaxGeodes = 0):
    #print(t, len(current))
    newCurrent = set()
    for state in current:
        newStates = make_robots(state, bp, t)
        for newState in newStates:
            nBots, nOre = tuple(newState[:4]), list(newState[4:])
            for i, numRobots in enumerate(state[:4]):
                nOre[i] += numRobots
            minMaxGeodes = max(minMaxGeodes, nOre[-1] + (nBots[-1] * (t-1)))
            maxPossible = nOre[-1] + (nBots[-1] * (t-1)) + ((t-2)*(t-1))//2
            if maxPossible < minMaxGeodes:
                continue
            newCurrent.add(tuple([*nBots, *nOre]))
            robots[nBots] = nOre[-1]
    current = set()
    if any(state[-1] > 0 for state in newCurrent):
        for state in newCurrent:
            if not state[1] or not state[2]:
                continue
            current.add(state)
    else:
        current = set(newCurrent)
    t -= 1
    if t > 0 and current:
        pass_time(current, t, bp, minMaxGeodes)
    else:
        best.append(max(ore for ore in robots.values()))

def part_one():
    global best, robots
    best = []
    score = 0
    for i, blueprint in enumerate(blueprints):
        bots = (1, 0, 0, 0)
        ore = (0, 0, 0, 0)
        robots = {tuple(bots): ore[-1]}
        time = 24
        state = tuple([*bots, *ore])
        current = {state}
        pass_time(current, time, blueprint)
        geodes = best[-1]
        score += (i+1) * geodes
    print(f"Part One = {score}")

def part_two():
    global best, robots
    best = []
    score = 1
    for i, blueprint in enumerate(blueprints[:3]):
        bots = (1, 0, 0, 0)
        ore = (0, 0, 0, 0)
        robots = {tuple(bots): ore[-1]}
        time = 32
        state = tuple([*bots, *ore])
        current = {state}
        pass_time(current, time, blueprint)
        geodes = best[-1]
        score *= geodes
    print(f"Part Two = {score}")

inputs = open_file()

format_data()
startp1 = time.perf_counter()
#part_one()
startp2 = time.perf_counter()
part_two()
end = time.perf_counter()

print(f"Part One took {round(startp2 - startp1, 3)} seconds")
print(f"Part Two took {round(end - startp2, 3)} seconds")