import time

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global cubes #for Part 1
    global cubes4 #for Part 2
    global dims #P1
    global dims4 #P2
    cubes = {} 
    cubes4 = {}
    z = 0
    w = 0
    for y, line in enumerate(inputs):
        line = [x for x in line.strip()]
        for x, val in enumerate(line):
            cubes[(x, y, z)] = val #Part 1
            cubes4[(x, y, z, w)] = val #Part 2
    xdim = x+1
    ydim = y+1
    zdim = z+1
    wdim = w+1
    dims = [xdim, ydim, zdim]
    dims4 = [xdim, ydim, zdim, wdim]

def shift_cubes(cubedict, dims):
    #To keep xyz(w) values positive and easy to search over
    shiftdict = {}
    for cube in cubedict:
        newpos = tuple(xyz + 1 for xyz in cube)
        #Shift origin by +1 in every direction
        shiftdict[newpos] = cubedict[cube]
    dims = [xyz + 2 for xyz in dims]
    return shiftdict, dims

def adj_cubes_vec():
    #Generate list of vectors for adjacent cubes (3D)
    vectors = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                vec = (x, y, z)
                vectors.append(vec)
    vectors.remove((0,0,0))
    return vectors

def adj_cubes_vec4():
    #4D list of vectors
    vectors = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for w in range(-1, 2):
                    vec = (x, y, z, w)
                    vectors.append(vec)
    vectors.remove((0,0,0,0))
    return vectors

def add(a, b):
    #To add vector to cube position (for each xyz(w))
    c = a + b
    return c

def check_cube(cdict, pos, vects):
    count = 0
    for vec in vects:
        adjpos = tuple(map(add, pos, vec))
        if adjpos in cdict and cdict[adjpos] == "#":
            count += 1
    if pos not in cdict and count == 3:
        return "#"
    elif pos not in cdict:
        return 0
    elif cdict[pos] == "#" and not (count==2 or count==3):
        return "." #Switch to inactive
    elif cdict[pos] == "." and count == 3:
        return "#" #Switch to active
    else:
        return cdict[pos] #No change
    

def cycle_cube(cubedict, vects, dims):
    cdict, dims = shift_cubes(cubedict, dims)
    d = len(dims)
    newdict = {}
    for x in range(dims[0]): #Check each cube
        for y in range(dims[1]):
            for z in range(dims[2]):
                if d == 4:
                    for w in range(dims[3]):
                        pos = (x, y, z, w)
                        val = check_cube(cdict, pos, vects)
                        if val == 0:
                            continue
                        else:
                            newdict[pos] = val
                else:
                    pos = (x, y, z)
                    val = check_cube(cdict, pos, vects)
                    if val == 0:
                        continue
                    else:
                        newdict[pos] = val
    return newdict, dims
                
def run_iterations(cubedict, vects, dims, n):
    for i in range(n):
        cubedict, dims = cycle_cube(cubedict, vects, dims)
    return cubedict             
                
day = 17
inputs = open_file()

formatdata(inputs)
#Part 1
t0 = time.perf_counter()
vects = adj_cubes_vec()
newdict = run_iterations(cubes, vects, dims, 6)
newvals = list(newdict.values())
print("Answer to Part 1 is", newvals.count("#")) #218
t1 = time.perf_counter()
#Part 2
vects4 = adj_cubes_vec4()
newdict4 = run_iterations(cubes4, vects4, dims4, 6)
newvals4 = list(newdict4.values())
print("Answer to Part 2 is", newvals4.count("#")) #1908
t2 = time.perf_counter()

print(f"Part 1 took {t1 - t0:0.7f} seconds")
#Part 1 took 0.2700086 seconds
print(f"Part 2 took {t2 - t1:0.7f} seconds")
#Part 2 took 9.3467008 seconds