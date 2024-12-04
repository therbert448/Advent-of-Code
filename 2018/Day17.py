def open_file():
    #file = open("test.txt")
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [line.strip() for line in file.readlines()]
    file.close()
    return inputs

def format_data():
    global clay
    clay = set()
    xset = set()
    yset = set()
    for line in inputs:
        coords = line.split(", ")
        for i, coord in enumerate(coords):
            coord = coord.split("=")
            if i == 0:
                one, val = coord
                if one == "x":
                    x = int(val)
                    xset.add(x)
                else:
                    y = int(val)
                    yset.add(y)
            else:
                two, vals = coord
                minval, maxval = vals.split("..")
                rnge = [int(minval), int(maxval)]
                if two == "x":
                    for x in range(rnge[0], rnge[1]+1):
                        clay.add((x, y))
                        xset.add(x)
                else:
                    for y in range(rnge[0], rnge[1]+1):
                        clay.add((x, y))
                        yset.add(y)
    global minx, maxx, miny, maxy
    minx, maxx = [min(xset)-1, max(xset)+1]
    miny, maxy = [min(yset), max(yset)]

def hit_clay(pos):
    x, y = pos
    rowset = {pos}
    left = (x-1, y)
    right = (x+1, y)
    while left:
        if left in clay or left in still:
            left = 0
            lover = 1
            break
        rowset.add(left)
        lx, _ = left
        down = (lx, y+1)
        if down not in clay and down not in still:
            if down in water and water[down] == 0:
                lover = 0
                break
            elif down in water:
                left = (lx-1, y)
                continue
            water[down] = 0
            lover = running_water(down)
            if lover == 0:
                left = 0
                break
        left = (lx-1, y)
    while right:
        if right in clay or right in still:
            right = 0
            rover = 1
            break
        rowset.add(right)
        rx, _ = right
        down = (rx, y+1)
        if down not in clay and down not in still:
            if down in water and water[down] == 0:
                rover = 0
                break
            elif down in water:
                right = (rx+1, y)
                continue
            water[down] = 0
            rover = running_water(down)
            if rover == 0:
                break
        right = (rx+1, y)
    for p in rowset:
        if lover and rover:
            still.add(p)
            water[p] = 1
        else:
            water[p] = 0
    if lover and rover:
        return 1
    else:
        return 0
    
            

def running_water(start):
    #print(start)
    flowing = 1
    pos = tuple(start)
    while flowing:
        #print(pos)
        x, y = pos
        down = (x, y+1)
        if down not in clay and down not in still:
            pos = down
            if down[1] > maxy:
                return 0
            else:
                water[pos] = 0
                continue
        else:
            over = hit_clay(pos)
            if over:
                #print(pos)
                pos = (x, y-1)
            else:
                return 0

day = 17
inputs = open_file()

format_data()

start = (500, miny-1)
still = set()
water = {}
running_water(start)
print("Part One:", len(water))
print("Part Two:", len(still))