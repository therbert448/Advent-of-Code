def open_or_wall(pos):
    x, y = pos
    val = x*x + 3*x + 2*x*y + y + y*y
    val += favnum
    binary = bin(val)[2:]
    count = binary.count("1")
    return count % 2

def neighbours(pos):
    neighs = []
    x, y = pos
    neighs.append((x+1, y))
    neighs.append((x, y+1))
    if x != 0:
        neighs.append((x-1, y))
    if y != 0:
        neighs.append((x, y-1))
    return neighs

def move():
    global stepcount
    stepcount = {start: 0}
    target_reached = 0
    nextsteps = {start}
    while not target_reached:
        newsteps = set()
        for pos in nextsteps:
            steps = stepcount[pos] + 1
            neighs = neighbours(pos)
            for n in neighs:
                if n in stepcount:
                    continue
                if n == target:
                    stepcount[n] = steps
                    target_reached = 1
                    return stepcount
                wall = open_or_wall(n)
                if wall:
                    stepcount[n] = -1
                else:
                    stepcount[n] = steps
                    newsteps.add(n)
        nextsteps = set(newsteps)

def run():
    move()
    print(f"Part One: {stepcount[target]}")
    count = 0
    for val in stepcount.values():
        if 0 <= val <= 50:
            count += 1
    print(f"Part Two: {count}")

start = (1, 1)
favnum = 1352
target = (31, 39)

run()