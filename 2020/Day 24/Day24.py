def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata():
    global tiles
    tiles = []
    for line in inputs:
        tile = []
        chars = [char for char in line.strip()]
        while len(chars) > 0:
            if chars[0] == "e" or chars[0] == "w":
                tile.append(chars.pop(0))
            else:
                direct = chars.pop(0) + chars.pop(0)
                tile.append(direct)
        tiles.append(tile)

def move_in_dir(pos, direct, n): #move in the given direction n times
    f = lambda a, b: a + (b * n)
    d = compass[direct]
    pos = tuple(map(f, pos, d))
    return pos
    
def find_tile(): #follow each line of instructions and flip the tile
    flipcount = {}
    for tile in tiles:
        pos = (0, 0)
        counts = {}
        for d in directions:
            counts[d] = tile.count(d)
        ew = counts["e"] - counts["w"]
        #A step east then a step west leaves you at the starting position
        nesw = counts["ne"] - counts["sw"] #Same for ne and sw
        nwse = counts["nw"] - counts["se"] #And for nw and se
        directs = [ew, nesw, nwse] #number of steps in each direction
        for i, d in enumerate(compass.keys()):
            pos = move_in_dir(pos, d, directs[i])
        if pos in flipcount:
            flipcount[pos] += 1
        else:
            flipcount[pos] = 1
    return flipcount

def count_black(): #count number of tiles flipped an odd number of times
    flipcount = find_tile()
    black = 0
    global blackdict
    blackdict = {}
    for pos in flipcount:
        if flipcount[pos] % 2 == 1:
            blackdict[pos] = 1 #dict of black tiles for part two
            black += 1
    print(black) #answer to part one

def find_borders(bdict): #define search range to check tiles
    xset = set()
    yset = set()
    for pos in bdict:
        xset.add(pos[0])
        yset.add(pos[1])
    posset = set()
    minx, maxx = [min(xset), max(xset)]
    miny, maxy = [min(yset), max(yset)]
    for x in range(minx-1, maxx+2):
        for y in range(miny-1, maxy+2):
            posset.add((x, y))
    return posset

def adjacent_tiles(pos): #list tiles touching given tile
    adjset = set()
    for i in range(2):
        i = (i * 2) - 1
        for d in compass.keys():
            adj = move_in_dir(pos, d, i)
            adjset.add(adj)
    return adjset

def day_flip(bdict): #flip tiles each day based on the rules
    newblackdict = {}
    posset = find_borders(bdict)
    for pos in posset:
        adjset = adjacent_tiles(pos)
        count = 0
        for a in adjset:
            if a in bdict:
                count += 1
        if pos in bdict and 0 < count < 3:
            newblackdict[pos] = 1
        elif pos not in bdict and count == 2:
            newblackdict[pos] = 1
    return newblackdict
            
def one_hundred_days(): #run up to one hundred days of flipping tiles
    bdict = dict(blackdict)
    for i in range(100):
        bdict = day_flip(bdict)
    print(len(bdict)) #answer to part two
    return bdict

day = 24
inputs = open_file()

formatdata()

directions = ["e", "ne", "nw", "w", "sw", "se"] #all 6 directions

compass = {"e": (1, 0), "ne": (0, 1), "nw": (-1, 1)} #3 axes of directions
#The "x" coordinate is the number of steps east (negative means west)
#The "y" coordinate is the number of steps north east (opposite is south west)
#A step north west is equivalent to a step west, then a step north east

count_black() #run part one
one_hundred_days() #run part two