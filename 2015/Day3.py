def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.read().strip()
    file.close()

def deliver_presents():
    global houses
    pos = (0, 0)
    houses = {pos}
    for char in inputs:
        direct = directs[char]
        pos = tuple(map(lambda a,b : a+b, pos, direct))
        houses.add(pos)
    print(f"Part One: {len(houses)}")
    santa, robot = [(0, 0), (0, 0)]
    houses = {santa, robot}
    for i, char in enumerate(inputs):
        direct = directs[char]
        if i % 2 == 0:
            santa = tuple(map(lambda a,b : a+b, santa, direct))
            houses.add(santa)
        else:
            robot = tuple(map(lambda a,b : a+b, robot, direct))
            houses.add(robot)
    print(f"Part Two: {len(houses)}")

day = 3
open_file()

directs = {">": (1, 0), "^": (0, 1), "<": (-1, 0), "v": (0, -1)}

deliver_presents()