def generate_inputs(): #translate input key into lists of lengths
    global strings, asclens
    suffix = [17, 31, 73, 47, 23]
    strings = []
    asclens = []
    string = inputstr
    for i in range(128):
        newstr = string + "-" + str(i)
        strings.append(newstr)
        asclen = [ord(char) for char in newstr]
        for s in suffix:
            asclen.append(s)
        asclens.append(asclen)

def generate_list(): #generate the starting list of 0-255
    global listlist
    listlist = [i for i in range(size)]

def hash_list(length, point, skip): #run the hash sequence for each length
    rev = []
    for i in range(length):
        idx = (point+i) % size
        rev.append(listlist[idx])
    for i in range(length):
        idx = (point+i) % size
        listlist[idx] = rev.pop() 
    point = (point + length + skip) % size
    skip += 1
    return point, skip

def run_hash(): #run all the strings through the hash algorithm
    global lists
    lists = []
    for asclen in asclens:
        generate_list()
        point = 0
        skip = 0
        for _ in range(64):
            for length in asclen:
                point, skip = hash_list(length, point, skip)
        lists.append(listlist)

def xor(listlist): #sparse list to dense hash
    result = 0
    for x in listlist:
        result = result ^ x
    return result

def dense_hash(listlist): #sparse list to dense hash
    densehash = []
    length = 16
    for i in range(length):
        densehash.append(xor(listlist[(i*length):(i+1)*length]))
    return densehash

def hexa(densehash): #translate dense hash to hexadecimal
    finalhash = ""
    for d in densehash:
        inhex = str(hex(d)[2:]).zfill(2)
        finalhash += inhex
    return finalhash

def translate_hex(): #translate hexadecimal to binary
    global mapstr
    mapstr = ""
    for line in hexes:
        linestr = ""
        for char in line:
            dec = int(char, 16)
            bina = bin(dec)[2:].zfill(4)
            linestr += bina
        linestr += "\n"
        mapstr += linestr
    mapstr = mapstr.strip()        

def map_to_grid(): #translate the map string to the grid
    global grid
    grid = set()
    for y, line in enumerate(mapstr.splitlines()):
        for x, char in enumerate(line.strip()):
            pos = (x, y)
            if char == "1":
                grid.add(pos)

def neighbours(pos): #find adjacent squares
    x, y = pos
    neighs = [(x+1, y),
              (x-1, y),
              (x, y+1),
              (x, y-1)]
    return neighs

def region_sets(pos): #find all the squares in a region
    global regset
    regset = {pos}
    nextpos = [pos]
    while nextpos:
        newpos = set()
        for nextp in nextpos:
            neighs = neighbours(nextp)
            for n in neighs:
                if n in grid and n not in regset:
                    regset.add(n)
                    newpos.add(n)
        nextpos = list(newpos)

def part_one(): #generate the knot hash for each input string
    generate_inputs()
    run_hash()
    global hexes
    hexes = []
    for listlist in lists:
        densehash = dense_hash(listlist)
        hexes.append(hexa(densehash))
    translate_hex() #translate the knot hashes into a map
    print("Part One:", mapstr.count("1")) #print the number of 1s in the map

def part_two(): #find all the regions
    map_to_grid() #translate the map string to a grid
    global reglist
    reglist = [] #list of all the separate regions
    regions = set() #set of all the squares already accounted for
    posleft = grid.symmetric_difference(regions) #all the squares left to check
    while posleft: #whilst there are squares without regions
        sortposleft = sorted(posleft)
        nextpos = sortposleft[0] #pick a square that isn't already in a region
        region_sets(nextpos) #find all the squares in the same region
        reglist.append(regset) #make a note of this new region for the count
        regions.update(regset) #update the set of squares accounted for
        posleft = grid.symmetric_difference(regions) #what squares are still left
    print("Part Two:", len(reglist))

size = 256
inputstr = "jxqlasbh"

part_one()
part_two()