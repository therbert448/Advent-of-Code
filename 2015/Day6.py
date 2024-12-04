def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global steps
    steps = []
    for line in inputs:
        line = line.split(" ")
        if line[0] == "toggle":
            topleft, _, bottomright = line[1:]
            command = "toggle"
        else:
            command, topleft, _, bottomright = line[1:]
        x1, y1 = topleft.split(",")
        xy1 = (int(x1), int(y1))
        x2, y2 = bottomright.split(",")
        xy2 = (int(x2), int(y2))
        step = [command, xy1, xy2]
        steps.append(step)

def christmas_lights(part):
    global lights
    lights = {}
    for x in range(1000):
        for y in range(1000):
            coords = (x, y)
            lights[coords] = 0
    for step in steps:
        command, minxy, maxxy = step
        minx, miny = minxy
        maxx, maxy = maxxy
        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                coords = (x, y)
                if command == "on":
                    if part == 1:
                        lights[coords] = 1
                    else:
                        lights[coords] += 1
                elif command == "off":
                    if part == 1:
                        lights[coords] = 0
                    else:
                        lights[coords] = max(0, lights[coords]-1)
                else:
                    if part == 1:
                        lights[coords] = (lights[coords] + 1) % 2
                    else:
                        lights[coords] += 2
    if part == 1:
        print(f"Part One: {sum(lights.values())}")
    else:
        print(f"Part Two: {sum(lights.values())}")

day = 6
open_file()

format_data()

christmas_lights(1)
christmas_lights(2)