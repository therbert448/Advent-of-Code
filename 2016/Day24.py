class MapClass:
    def __init__(self, string):
        self.map = string
        
    def map_to_grid(self):
        grid = []
        for line in self.map.splitlines():
            row = [char for char in line.strip()]
            grid.append(row)
        self.griddict = {}
        self.posd = {}
        for y, line in enumerate(grid):
            for x, char in enumerate(line):
                if char == "#":
                    continue
                pos = (x, y)
                try:
                    char = int(char)
                    self.posd[char] = pos
                    if char == 0:
                        self.startpos = char
                except:
                    pass
                self.griddict[pos] = char
    
def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global startmap
    startmap = file.read()
    file.close()
    
def neighbours(pos):
    x, y = [pos[0], pos[1]]
    neighs = [(x+1, y),
              (x, y+1),
              (x-1, y),
              (x, y-1)]
    return neighs

def steps_to_pos(posnum):
    pos = Map.posd[posnum]
    stepcount = {pos: 0}
    posset = {pos}
    while posset:
        newposset = set()
        for pos in posset:
            neighs = neighbours(pos)
            steps = stepcount[pos] + 1
            for n in neighs:
                if n not in stepcount and n in Map.griddict:
                    char = Map.griddict[n]
                    if isinstance(char, int):
                        path = tuple(sorted([posnum, char]))
                        psteps[path] = steps
                    newposset.add(n)
                    stepcount[n] = steps
        posset = set(newposset)

def find_pairs():
    global posnumset, psteps, startnum, Map
    Map = MapClass(startmap)
    Map.map_to_grid()
    startnum = Map.startpos
    posnumset = sorted(list(Map.posd.keys()))
    psteps = {}
    for posnum in posnumset:
        steps_to_pos(posnum)
        del Map.posd[posnum]
        if len(Map.posd) == 1:
            del Map.posd
            break
    posnumset.remove(startnum)

def find_locs(startnum, posnums, part):
    possible_paths = []
    state = (str(startnum), "".join([str(num) for num in posnums]))
    if state in states:
        return states[state]
    for endnum in posnums:
        for path in psteps:
            if startnum in path and endnum in path:
                possible_paths.append(path)
    if not possible_paths:
        return 0
    mindist = -1
    for path in possible_paths:
        for char in path:
            if char != startnum:
                end = char
        distance = psteps[path]
        newposnums = list(posnums)
        newposnums.remove(end)
        if part == 2 and not newposnums and end != 0:
            newposnums.append(0)
        newstart = end
        distance += find_locs(newstart, newposnums, part)
        if mindist == -1 or distance < mindist:
            mindist = distance
    states[state] = mindist
    return mindist

def run_robot():
    global states
    find_pairs()
    posnums = list(posnumset)
    states = {}
    mindist = find_locs(startnum, posnums, 1)
    print(f"Part One: {mindist}")
    posnums = list(posnumset)
    states = {}
    mindist = find_locs(startnum, posnums, 2)
    print(f"Part Two: {mindist}")

day = 24
open_file()

run_robot()