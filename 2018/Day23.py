def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()
    return inputs

def format_data():
    global nanobots
    nanobots = {}
    xset, yset, zset = [set(), set(), set()]
    for line in inputs:
        line = line.split(">, r=")
        coords = line[0].split("<")[1]
        pos = tuple(int(i) for i in coords.split(","))
        x, y, z = pos
        [xset.add(x), yset.add(y), zset.add(z)]
        radius = int(line[1])
        nanobots[pos] = radius
    global xmin, xmax, ymin, ymax, zmin, zmax, xrange, yrange, zrange
    xmin, xmax = [min(xset), max(xset)]
    ymin, ymax = [min(yset), max(yset)]
    zmin, zmax = [min(zset), max(zset)]
    xrange = xmax - xmin # xrange is the biggest = 352117827
    yrange = ymax - ymin
    zrange = zmax - zmin

def best_nanobot():
    global bestbot
    botvals = list(nanobots.values())
    botpos = list(nanobots.keys())
    idx = botvals.index(max(botvals))
    bestbot = botpos[idx]

def bot_dists():
    inrangecount = 0
    for bot in nanobots:
        dist = sum([abs(bestbot[i] - bot[i]) for i in range(3)])
        if dist <= nanobots[bestbot]:
            inrangecount += 1
    return inrangecount

def neighbours(pos):
    x, y, z = pos
    neighs = [(x-1, y, z),
              (x+1, y, z),
              (x, y-1, z),
              (x, y+1, z),
              (x, y, z-1),
              (x, y, z+1)]
    return neighs

def bots_from_pos(pos):
    botcount = 0
    for bot in nanobots:
        dist = sum([abs(pos[i] - bot[i]) for i in range(3)])
        if dist <= nanobots[bot]:
            botcount += 1
    return botcount

def part_one():
    best_nanobot()
    print("Part One:", bot_dists())

def part_two():
    xrange = [xmin, xmax]
    yrange = [ymin, ymax]
    zrange = [zmin, zmax]
    div = 1
    while div < xmax - xmin: #find cube big enough to cover all bots
        div *= 2
    found = 0
    while not found:
        maxcount = -1
        bestmandist = -1
        #check the vertices of the cube
        for x in range(min(xrange), max(xrange) + 1, div):
            for y in range(min(yrange), max(yrange) + 1, div):
                for z in range(min(zrange), max(zrange) + 1, div):
                    pos = (x, y, z)
                    botcount = bots_from_pos(pos)
                    #number of bots in range of the vertex
                    mandist = sum([abs(pos[i]) for i in range(3)])
                    if botcount > maxcount:
                        maxcount = botcount
                        bestmandist = mandist
                        bestpos = pos
                    elif botcount == maxcount and mandist < bestmandist:
                        bestmandist = mandist
                        bestpos = pos
        if div == 1:
            print("Part Two")
            print("Maximum bots:", maxcount)
            print("Best Manhattan distance:", bestmandist)
            found = 1
            break
        else:
            x, y, z = bestpos
            xrange = [x - div, x + div]
            yrange = [y - div, y + div]
            zrange = [z - div, z + div]
            div = div // 2
            #recentre cube and increase sampling points
            #then the cube is shrunk and recentred

day = 23
open_file()

format_data()

part_one()
part_two()