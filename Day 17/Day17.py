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

def shift_cubes(cubedict):
    #To keep xyz(w) values positive and easy to search over
    shiftdict = {}
    for cube in cubedict:
        newpos = tuple(xyz + 1 for xyz in cube)
        #Shift origin by +1 in every direction
        shiftdict[newpos] = cubedict[cube]
    return shiftdict

def shell_cubes(cubedict, dims):
    #Add cubes to the outside of the current set
    #Might be better to check if needed first, but this covers worst case
    #and is simpler to write
    shiftdict = shift_cubes(cubedict)
    dims = [xyz+2 for xyz in dims]
    #Cubes either side, so xyz dimensions increase by two
    for x in range(dims[0]):
        for y in range(dims[1]):
            for z in range(dims[2]):
                pos = (x, y, z)
                if pos not in shiftdict:
                    shiftdict[pos] = "."
    return shiftdict, dims

def shell_cubes4(cubedict, dims):
    #Same as above, but 4 dimensions
    shiftdict = shift_cubes(cubedict)
    dims = [xyzw+2 for xyzw in dims]
    for x in range(dims[0]):
        for y in range(dims[1]):
            for z in range(dims[2]):
                for w in range(dims[3]):
                    pos = (x, y, z, w)
                    if pos not in shiftdict:
                        shiftdict[pos] = "."
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

def cycle_cube(cubedict, vects, dims, case):
    if case == "3D": #run correct shell program for dimension
        shelldict, dims = shell_cubes(cubedict, dims)
    elif case == "4D":
        shelldict, dims = shell_cubes4(cubedict, dims)
    newdict = {}
    for cube in shelldict: #Check each cube
        count = 0
        for vec in vects: #Check all adjacent cubes
            pos = tuple(map(add, cube, vec))
            if pos in shelldict and shelldict[pos] == "#":
                count += 1 #Count active adjacent cubes
        if shelldict[cube] == "#" and not (count == 2 or count == 3):
            newdict[cube] = "." #Switch to inactive
        elif shelldict[cube] == "." and count == 3:
            newdict[cube] = "#" #Switch to active
        else:
            newdict[cube] = shelldict[cube] #No change
    return newdict, dims
                
def run_iterations(cubedict, vects, dims, n, case):
    for i in range(n):
        cubedict, dims = cycle_cube(cubedict, vects, dims, case)
    return cubedict             
                
day = 17
inputs = open_file()

formatdata(inputs)
#Part 1
t0 = time.perf_counter()
vects = adj_cubes_vec()
newdict = run_iterations(cubes, vects, dims, 6, "3D")
newvals = list(newdict.values())
print("Answer to Part 1 is", newvals.count("#")) #218
t1 = time.perf_counter()
#Part 2
vects4 = adj_cubes_vec4()
newdict4 = run_iterations(cubes4, vects4, dims4, 6, "4D")
newvals4 = list(newdict4.values())
print("Answer to Part 2 is", newvals4.count("#")) #1908
t2 = time.perf_counter()

print(f"Part 1 took {t1 - t0:0.7f} seconds")
#Part 1 took 0.4083943 seconds
print(f"Part 2 took {t2 - t1:0.7f} seconds")
#Part 2 took 12.5151661 seconds