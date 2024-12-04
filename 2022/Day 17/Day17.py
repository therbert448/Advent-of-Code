"""
Advent of Code
2022 Day 17

@author: Tom Herbert
"""

day = 17

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        moves = [char for char in file.read()]
    return moves

def add(a, b): return a+b

def move_left_right(count, pos, point):
    x, y = pos
    move = moves[point % len(moves)]
    if move == "<":
        x -= 1
        if x == xmin: return pos
    else:
        x += 1
        if x == xmax - lengths[count % nShapes] + 1: return pos
    newPos = (x, y)
    rocks = [tuple(map(add, newPos, rock)) for rock in shapes[count % nShapes]]
    if any(rock in fallen for rock in rocks):
        newPos = tuple(pos)
    return newPos

def move_down(count, pos):
    x, y = pos
    y -= 1
    if y == 0:
        return True, pos
    newPos = (x, y)
    rocks = [tuple(map(add, newPos, rock)) for rock in shapes[count % nShapes]]
    if any(rock in fallen for rock in rocks):
        return True, pos
    return False, newPos

def find_row(ymax): #Save three rows to make sure the states are unique
    inRow = [rock for rock in fallen if rock[1] in (ymax, ymax-1, ymax-2)]
    string = ""
    for y in range(3):
        for x in range(xmin+1, xmax):
            if (x, ymax-y) in inRow:
                string += "#"
            else:
                string += "."
    return string

def plot(ymax):
    string = ""
    for y in range(ymax, -1, -1):
        for x in range(xmin+1, xmax):
            if (x, y) in fallen:
                string += "#"
            else:
                string += "."
        string += "\n"
    print(string)

def tetris():
    global fallen, xmin, xmax, ymax, states, counts, state, count
    states = {}
    counts = {}
    fallen = set()
    count = 0
    point = 0
    xmin, xmax, ymax = 0, 8, 0
    while True:
        landed = False
        pos = (xmin + 3, ymax + 4)
        while not landed:
            pos = move_left_right(count, pos, point)
            point += 1
            landed, pos = move_down(count, pos)
        ymax = max(ymax, pos[1] + heights[count % nShapes] - 1)
        rocks = [tuple(map(add, pos, r)) for r in shapes[count % nShapes]]
        [fallen.add(rock) for rock in rocks]
        row = find_row(ymax)
        count += 1
        state = (row, count % nShapes, point % len(moves))
        if state in states:
            break
        else:
            states[state] = count
            counts[count] = ymax

def calculate_loops(N, part):
    heightBefore = counts[states[state]] # Height before loop started
    loopLength = count - states[state] # How many shapes dropped each loop
    loopHeight = ymax - heightBefore # Increase in height each loop
    loops = (N - states[state])//loopLength # How many loops will run
    heightDuring = loopHeight * loops # Height of all these loops
    remaining = N - ((loops * loopLength) + states[state])
    # How many shapes left to drop
    remainingIdx = remaining + states[state] 
    # Add number of shapes dropped before loop started
    heightAfter = counts[remainingIdx] - heightBefore
    # Look up the height for the number of shapes, then subtract the non loop
    totalHeight = heightBefore + heightDuring + heightAfter
    print(f"Part {part} = {totalHeight}")

moves = open_file()

shapes = [[(0, 0), (1, 0), (2, 0), (3, 0)],
          [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
          [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
          [(0, 0), (0, 1), (0, 2), (0, 3)],
          [(0, 0), (1, 0), (0, 1), (1, 1)]          ]
heights = [1, 3, 3, 4, 2]
lengths = [4, 3, 3, 1, 2]
nShapes = 5

tetris()

calculate_loops(2022, "One")
calculate_loops(1_000_000_000_000, "Two")