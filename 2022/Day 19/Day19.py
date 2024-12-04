"""
Advent of Code
2022 Day 19

@author: Tom Herbert

First solution took about 2 mins for Part One and 3 mins for Part Two, but this
version can complete both within 20 seconds now.
If no robot was built at time t, when it was possible to build a robot, then
the robots that were skipped will not be built at time t+1.
The only reason to not build a robot when possible is when you're waiting for
enough resources to build a different type robot.
There will never be a benefit to waiting an extra minute to build a robot.
"""

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
    bots, ore, skipped = state[:4], state[4:8], list(state[8:])
    newStates = set()
    if all(bots[i] >= blueprint[-1][i] for i in range(3)):
        if all(ore[j] >= blueprint[-1][j] for j in range(3)):
            newState = list([*bots, *ore, 0, 0, 0, 0])
            newState[-5] += 1
            for k, cost in enumerate(blueprint[-1]):
                newState[k+4] -= cost
            newStates = {tuple(newState)}
        else:
            newStates = {tuple([*bots, *ore, 0, 0, 0, 0])}
        return newStates
    for i, robot in enumerate(blueprint):
        if skipped[i]:
            continue
        if i < 3 and bots[i] >= max(blue[i] for blue in blueprint):
            continue
        if i < 3 and ore[i] >= max(blue[i] for blue in blueprint) * time:
            continue
        if all(ore[j] >= robot[j] for j in range(len(robot))):
            skipped[i] = 1
            newState = list([*bots, *ore, 0, 0, 0, 0])
            newState[i] += 1
            for k, cost in enumerate(robot):
                newState[k+4] -= cost
            newStates.add(tuple(newState))
    newStates.add(tuple([*bots, *ore, *skipped]))
    return newStates

def pass_time(current, t, bp, minMaxGeodes = 0):
    newCurrent = set()
    for state in current:
        newStates = make_robots(state, bp, t)
        for newState in newStates:
            nBots, nOre = tuple(newState[:4]), list(newState[4:8])
            skipped = list(newState[8:])
            for i, numRobots in enumerate(state[:4]):
                nOre[i] += numRobots
            minMaxGeodes = max(minMaxGeodes, nOre[-1] + (nBots[-1] * (t-1)))
            maxPossible = nOre[-1] + (nBots[-1] * (t-1)) + ((t-2)*(t-1))//2
            if maxPossible < minMaxGeodes:
                continue
            newCurrent.add(tuple([*nBots, *nOre, *skipped]))
            robots[nBots] = nOre[-1]
    current = set()
    if any(state[-5] > 0 for state in newCurrent):
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
        skipped = (0, 0, 0, 0)
        robots = {tuple(bots): ore[-1]}
        time = 24
        state = tuple([*bots, *ore, *skipped])
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
        skipped = (0, 0, 0, 0)
        robots = {tuple(bots): ore[-1]}
        time = 32
        state = tuple([*bots, *ore, *skipped])
        current = {state}
        pass_time(current, time, blueprint)
        geodes = best[-1]
        score *= geodes
    print(f"Part Two = {score}")

inputs = open_file()

format_data()

part_one()
part_two()