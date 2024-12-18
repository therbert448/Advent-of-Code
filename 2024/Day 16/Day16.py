"""
Advent of Code
2024 Day 16

@author: Tom Herbert
"""
from time import time

day = 16

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        maze = [line.strip() for line in file.readlines()]
    walls = set()
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == "#":
                walls.add((x, y))
            elif char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)
    return walls, start, end
t0 = time()
walls, start, end = open_file(day)
dires = ["E", "S", "W", "N"]
steps = {"E": (1, 0), "S": (0, 1), "W": (-1, 0), "N": (0, -1)}
startDire = "E"
add = lambda a, b: a + b

state = (start, startDire)
visited = {state: [0, {start}]}
endPaths = []
current = {state}
finalScore = None
while current:
    newCurrent = set()
    for state in current:
        score, path = visited[state]
        step, turn = score + 1, score + 1000
        pos, dire = state
        nextStep = (tuple(map(add, pos, steps[dire])), dire)
        left = (pos, dires[(dires.index(dire)-1) % 4])
        right = (pos, dires[(dires.index(dire)+1) % 4])
        newStates = [[nextStep, step], [left, turn], [right, turn]]
        for newState in newStates:
            newPath = set(pos for pos in path)
            state, newScore = newState
            if state[0] == end:
                newPath.add(end)
                if not finalScore or newScore == finalScore:
                    finalScore = newScore
                    endPaths.append(newPath)
                elif newScore < finalScore:
                    finalScore = newScore
                    endPaths = [newPath]
                continue
            if state[0] not in walls:
                newPath.add(state[0])
                if state not in visited or visited[state][0] > newScore:
                    visited[state] = [newScore, newPath]
                    newCurrent.add(state)
                elif visited[state][0] == newScore:
                    visitedPath = visited[state][1]
                    visited[state] = [newScore, newPath.union(visitedPath)]
                    newCurrent.add(state)
    current = set(state for state in newCurrent)

print(finalScore)

allPos = set()
for path in endPaths:
    allPos = allPos.union(path)
allPos = sorted(list(allPos))
print(len(allPos))
t1 = time()
print(t1-t0)