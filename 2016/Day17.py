import hashlib

def move():
    pos = (start, "")
    moves[pos] = 0
    atvault = 0
    currentpos = {pos}
    while currentpos:
        nextpos = set()
        for pos in currentpos:
            steps = moves[pos] + 1
            coords = pos[0]
            path = pos[1]
            if coords == target and atvault == 0:
                print(f"Part One: {path}")
                atvault = 1
                continue
            elif coords == target:
                continue
            x, y = coords
            code = passcode + path
            doors = hashlib.md5(code.encode()).hexdigest()[:4]
            posmoves = set()
            for i, door in enumerate(doors):
                if door in "bcdef":
                    direct = doordirects[i]
                    posmoves.add((directions[direct], direct))
            for move in posmoves:
                nextx, nexty = [x + move[0][0], y + move[0][1]]
                if nextx < 0 or nextx > 3 or nexty < 0 or nexty > 3:
                    continue
                nextp = ((nextx, nexty), path + move[1])
                if nextp not in moves:
                    moves[nextp] = steps
                    nextpos.add(nextp)
        currentpos = set(nextpos)
    maxsteps = 0
    for pos, steps in moves.items():
        coords = pos[0]
        if coords == target:
            if steps > maxsteps:
                maxsteps = steps
    print(f"Part Two: {maxsteps}")

start = (0, 0)
target = (3, 3)

passcode = "udskfozm"

directions = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}
doordirects = ["U", "D", "L", "R"]
moves = {}

move()