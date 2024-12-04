def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def formatdata():
    global points
    points = {}
    for i, line in enumerate(inputs):
        _, pos, vel = line.split("<")
        pos = pos.split(">")[0]
        x, y = pos.split(", ")
        pos = (int(x), int(y))
        velx, vely = vel.strip(">").split(", ")
        vel = (int(velx), int(vely))
        points[i] = (pos, vel)

def find_min_time():
    global mintime
    mintime = 0
    for point in points:
        pos, vel = points[point]
        x, y = pos
        vx, vy = vel
        xyt = [abs(x//vx), abs(y//vy)]
        if mintime == 0 or min(xyt) < mintime:
            mintime = min(xyt)

def draw_grid():
    minx, maxx = [min(xset), max(xset)]
    miny, maxy = [min(yset), max(yset)]
    newgrid = []
    for y in range(miny, maxy + 1):
        row = ""
        for x in range(minx, maxx + 1):
            if (x, y) in posset:
                row += "#"
            else:
                row += "."
        newgrid.append(row)
    [print(line) for line in newgrid]      

def apply_min_time():
    find_min_time()
    for i in range(300):
        newmintime = mintime + i
        global posset, xset, yset
        posset = set()
        xset = set()
        yset = set()
        for point in points:
            pos, vel = points[point]
            x, y = pos
            vx, vy = vel
            x += vx * newmintime
            y += vy * newmintime
            xset.add(x)
            yset.add(y)
            pos = (x, y)
            posset.add(pos)
        yrange = max(yset) - min(yset)
        if yrange > 10:
            continue
        else:
            print(newmintime)
            draw_grid()



day = 10
open_file()

formatdata()

apply_min_time()