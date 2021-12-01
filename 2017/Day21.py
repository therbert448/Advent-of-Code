def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global twoxtwo, threexthree
    twoxtwo = {} #rules for a 2x2 subpicture
    threexthree = {} #rules for a 3x3 subpicture
    #could technically combine the two, but this works as well
    for line in inputs:
        rule, out = line.split(" => ")
        rule = tuple(rule.split("/")) #make the rule a tuple and key for later
        out = out.split("/")
        if len(rule) == 2:
            twoxtwo[rule] = out
        else:
            threexthree[rule] = out

def split_picture(pattern):
    global size, gridsize, subsize
    size = len(pattern)
    if size % 2 == 0: #determine how we are splitting it
        subsize = 2
    elif size % 3 == 0:
        subsize = 3
    gridsize = size//subsize #how many subpictures will we need per row
    subpics = []
    for i in range(gridsize):
        row = []
        for j in range(gridsize):
            s = subsize
            sub = [pattern[(i*s)+k][(j*s):(j*s)+s] for k in range(s)]
            row.append(sub)
        subpics.append(row)
    #original pattern becomes a gridsize x gridsize grid of subpics
    #each subpic is subsize x subsize
    return subpics
                

def flip_and_rotate(pic):
    #maximum 8 unique orientations
    size = len(pic)
    configs = {tuple(pic)} #original orientation, set to eliminate duplicates
    configs.add(tuple(pic[::-1])) #flip vertically
    fliphori = [line[::-1] for line in pic]
    configs.add(tuple(fliphori)) #flip horizontally
    configs.add(tuple(fliphori[::-1])) #flip both horizontally and vertically
    #equivalent to rotating by 180 degs
    rot = []
    for x in range(size):
        row = ""
        for y in range(size):
            y = size - 1 - y
            row += pic[y][x]
        rot.append(row)
    configs.add(tuple(rot)) #rotate 90 degs, doesn't matter which way
    configs.add(tuple(rot[::-1])) #flip rotation vertically
    rotfliph = [line[::-1] for line in rot]
    configs.add(tuple(rotfliph)) #flip rotation horizontally
    configs.add(tuple(rotfliph[::-1])) #flip both
    #equivalent to a 90 deg rotation in the other direction
    return configs

def stitch(subpics):
    #stitch all the subpics together to form one pattern in input format
    newpat = []
    newsubsize = subsize + 1
    for i in range(gridsize):
        for j in range(newsubsize):
            string = ""
            for k in range(gridsize):
                string += subpics[i][k][j]
            newpat.append(string)
    return newpat

def check_rules(pattern):
    subpics = split_picture(pattern) #split into a subgrid
    if subsize == 2: #determine which rules apply
        rules = twoxtwo
    elif subsize == 3:
        rules = threexthree
    for y, row in enumerate(subpics):
        for x, pic in enumerate(row):
            configs = flip_and_rotate(pic) #find all orientations of a subpic
            for rule in rules:
                if rule in configs: #check if a rule matches an orientation
                    break #only one rule can match
            newsub = rules[rule] #output of the rule, doesn't flip or rotate
            subpics[y][x] = newsub #replace old subpic with new subpattern
    newpat = stitch(subpics) #stitch all subpics together for the next pattern
    return newpat

def run_iterations(n):
    newpattern = list(pattern)
    for _ in range(n):
        newpattern = check_rules(newpattern)
    newpattern = "\n".join(newpattern) #make pattern single string to count #
    if n == 5:
        print("Part One:", newpattern.count("#"))
    else:
        print("Part Two:", newpattern.count("#"))

day = 21
open_file()

format_data()

pattern = [".#.",
           "..#",
           "###"]
#initial pattern

run_iterations(5)
run_iterations(18) 
#runs in a reasonable time despite a max grid size of 1458x1458