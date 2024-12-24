"""
Advent of Code
2024 Day 21

@author: Tom Herbert
"""
from time import time

day = 21

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        codes = [line.strip() for line in file.readlines()]
    return codes

def neighbours(coord, valid):
    add = lambda a, b: a + b
    steps = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}
    neighs = {k: tuple(map(add, coord, v)) for k, v in steps.items()}
    neighs = {k: v for k, v in neighs.items() if v in valid}
    return neighs

def pad_paths(code, pad, valid, d):
    if d == 0:
        return len(code)
    currentKey = "A"
    total = 0
    while code:
        nextKey = code[0]
        pair = (currentKey, nextKey)
        if pair in counts and d in counts[pair]: 
            total += counts[pair][d]
            currentKey = nextKey
            code = code[1:]
            continue
        if pair not in counts: counts[pair] = {}    
        counts[pair][d] = 0
        if pair not in paths:
            paths[pair] = []
            start = pad[currentKey]
            end = pad[nextKey]
            current = {(start, "")}
            Nsteps = 0
            visited = {start: Nsteps}
            while current:
                Nsteps += 1
                newCurrent = set()
                for coord, path in current:
                    neighs = neighbours(coord, valid)
                    neighs[""] =  coord
                    for move, pos in neighs.items():
                        if pos == end:
                            visited[end] = Nsteps
                            nPath = path + move + "A"
                            paths[pair].append(nPath)
                            continue
                        if pos in visited and Nsteps > visited[pos]: continue
                        visited[pos] = Nsteps
                        newPath = path + move
                        newCurrent.add((pos, newPath))
                if end in visited: break
                current = {tup for tup in newCurrent}
        pathsList = [string for string in paths[pair]]
        minLen = min([len(string) for string in pathsList])
        pathsList = [string for string in pathsList if len(string) == minLen]
        minLen = 0
        for moves in pathsList:
            length = pad_paths(moves, direPad, direValid, d-1)
            if not minLen or length < minLen:
                minLen = length
        counts[pair][d] = minLen
        total += minLen
        currentKey = nextKey
        code = code[1:]
    return total

codes = open_file(day)

keypad = {"7":(0, 0), "8":(1, 0), "9":(2, 0), "4":(0, 1), "5":(1, 1),
          "6":(2, 1), "1":(0, 2), "2":(1, 2), "3":(2, 2), "0":(1, 3), "A":(2, 3)}
keyValid = set(keypad.values())
direPad = {"^":(1, 0), "A":(2, 0), "<":(0, 1), "v":(1, 1), ">":(2, 1)}
direValid = set(direPad.values())

code = codes[0]

paths, counts = {}, {}
result = 0
for code in codes:
    depth = 3
    minLen = pad_paths(code, keypad, keyValid, depth)
    value = int(code[:-1])
    result += minLen * value
print(result)

result = 0
for code in codes:
    depth = 26
    minLen = pad_paths(code, keypad, keyValid, depth)
    value = int(code[:-1])
    result += minLen * value
print(result)

