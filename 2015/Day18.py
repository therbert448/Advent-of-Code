def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global lights
    lights = set()
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char == "#":
                pos = (x, y)
                lights.add(pos)

def neighbours(pos):
    x, y = pos
    neighs = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            neighs.append((x+dx, y+dy))
    return neighs

def animate(grid):
    if part == 1:
        newgrid = set()
    else:
        newgrid = set(corners)
    for x in range(100):
        for y in range(100):
            pos = (x, y)
            neighs = neighbours(pos)
            count = 0
            for n in neighs:
                if n in grid:
                    count += 1
            if pos in grid and count in (2, 3):
                newgrid.add(pos)
            elif pos not in grid and count == 3:
                newgrid.add(pos)
    return newgrid

def iterate():
    if part == 1:
        grid = set(lights)
    else:
        grid = lights.union(corners)
    for _ in range(100):
        grid = animate(grid)
    if part == 1:
        print(f"Part One: {len(grid)}")
    else:
        print(f"Part Two: {len(grid)}")

day = 18
open_file()

format_data()

corners = {(0, 0), (0, 99), (99, 0), (99, 99)}

part = 1
iterate()
part = 2
iterate()