def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip("\n") for line in file.readlines()]
    file.close()

def format_data():
    global grid, start
    grid = {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            pos = (x, y)
            if char == " ":
                continue
            if char == "|" and y == 0:
                start = pos
            grid[pos] = char

def move(a, b):
    return a + b

def run_grid():
    global letterstring, stepcount
    letterstring = ""
    pos = start
    didx = 0
    direct = directs[didx]
    end = 0
    stepcount = 0
    while not end:
        if pos not in grid:
            end = 1
            break
        stepcount += 1
        if grid[pos].isupper():
            letterstring += grid[pos]
        elif grid[pos] == "+":
            lefti = (didx-1) % 4
            ld = directs[lefti]
            leftpos = tuple(map(move, pos, ld))
            if leftpos in grid:
                pos = leftpos
                didx = lefti
                direct = ld
                continue
            righti = (didx+1) % 4
            rd = directs[righti]
            rightpos = tuple(map(move, pos, rd))
            if rightpos in grid:
                pos = rightpos
                didx = righti
                direct = rd
                continue
        pos = tuple(map(move, pos, direct))
    print("Part One:", letterstring)
    print("Part Two:", stepcount)
            

day = 19
open_file()

format_data()

directs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

run_grid()