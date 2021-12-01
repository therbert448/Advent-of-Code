def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global steps
    steps = []
    for line in inputs:
        if "rect" in line:
            _, dims = line.split(" ")
            x, y = dims.split("x")
            x, y = [int(x), int(y)]
            step = ["rect", x, y]
            steps.append(step)
        elif "rotate" in line and "x" in  line:
            _, dims = line.split("=")
            x, shift = dims.split(" by ")
            x, shift = [int(x), int(shift)]
            step = ["rotx", x, shift]
            steps.append(step)
        elif "rotate" in line and "y" in line:
            _, dims = line.split("=")
            y, shift = dims.split(" by ")
            y, shift = [int(y), int(shift)]
            step = ["roty", y, shift]
            steps.append(step)

def follow_steps():
    global grid
    grid = set()
    for step in steps:
        newgrid = set()
        command = step[0]
        if command == "rect":
            xdim, ydim = step[1:]
            for x in range(xdim):
                for y in range(ydim):
                    pixel = (x, y)
                    newgrid.add(pixel)
        elif command == "rotx":
            x, shift = step[1:]
            for y in range(ymax):
                newy = (y + shift) % ymax
                pixel, newpixel = [(x, y), (x, newy)]
                if pixel in grid:
                    grid.remove(pixel)
                    newgrid.add(newpixel)
        elif command == "roty":
            y, shift = step[1:]
            for x in range(xmax):
                newx = (x + shift) % xmax
                pixel, newpixel = [(x, y), (newx, y)]
                if pixel in grid:
                    grid.remove(pixel)
                    newgrid.add(newpixel)
        grid.update(newgrid)
    print(f"Part One: {len(grid)}")

def print_screen():
    string = ""
    for y in range(ymax):
        for x in range(xmax):
            pixel = (x, y)
            if pixel in grid:
                string += "#"
            else:
                string += " "
        string += "\n"
    print("Part Two:") 
    print(string)

day = 8
open_file()

format_data()

xmax = 50
ymax = 6
follow_steps()
print_screen()