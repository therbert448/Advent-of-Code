def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global steps
    steps = file.read().strip().split(", ")
    file.close()

def follow_steps():
    didx = 0
    pos = (0, 0)
    posset = {pos}
    firstdup = 1
    for step in steps:
        lr = step[0]
        dist = int(step[1:])
        if lr == "R":
            didx = (didx + 1) % 4
            direct = directs[didx]
        elif lr == "L":
            didx = (didx - 1) % 4
            direct = directs[didx]
        for _ in range(dist):
            pos = tuple(map(lambda a,b : a + b, pos, direct))
            if pos not in posset:
                posset.add(pos)
            elif firstdup:
                mandist = sum([abs(xy) for xy in pos])
                firstdup = 0
    dist = sum([abs(xy) for xy in pos])
    print("Part One:", dist)
    print("Part Two:", mandist)

day = 1
open_file()

directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

follow_steps()