class MapClass:
    def __init__(self, string):
        self.map = string
        
    def map_to_grid(self):
        count = 1
        grid = []
        for line in self.map.splitlines():
            row = [char for char in line.strip()]
            grid.append(row)
        self.griddict = {}
        self.keyd = {}
        self.doord = {}
        self.startpos = []
        for y, line in enumerate(grid):
            for x, char in enumerate(line):
                if char == "#":
                    continue
                pos = (x, y)
                if char.isupper():
                    self.doord[char] = pos
                elif char.islower() or char == "@":
                    if char == "@":
                        char = str(count)
                        self.startpos.append(char)
                        count += 1
                    self.keyd[char] = pos
                self.griddict[pos] = char
    
def open_file(part):
    if part == 1:
        file = open("Day" + str(day) + "inputs.txt")
    elif part == 2:
        file = open("Day" + str(day) + "inputsb.txt")
    startmap = file.read()
    file.close()
    return startmap
    
def neighbours(pos):
    x, y = [pos[0], pos[1]]
    neighs = [(x+1, y),
              (x, y+1),
              (x-1, y),
              (x, y-1)]
    return neighs

def steps_to_keys(key):
    pos = Map.keyd[key]
    stepcount = {pos: [0, []]}
    posset = {pos}
    while posset:
        newposset = set()
        for pos in posset:
            neighs = neighbours(pos)
            for n in neighs:
                if n not in stepcount and n in Map.griddict:
                    steps = stepcount[pos][0] + 1
                    doorlist = list(stepcount[pos][1])
                    char = Map.griddict[n]
                    if char.isupper():
                        doorlist.append(char)
                    elif char.islower():
                        newkey = "".join(sorted([key, char]))
                        psteps[newkey] = steps
                        pdoors[newkey] = list(doorlist)
                    newposset.add(n)
                    stepcount[n] = [steps, list(doorlist)]
        posset = set(newposset)
    return psteps, pdoors

def find_pairs():
    global keyset, psteps, pdoors, starts, Map
    Map = MapClass(startmap)
    Map.map_to_grid()
    starts = Map.startpos
    keyset = sorted(list(Map.keyd.keys()))
    psteps = {}
    pdoors = {}
    for key in keyset:
        psteps, pdoors = steps_to_keys(key)
        del Map.keyd[key]
        if len(Map.keyd) == 1:
            return

def find_keys(starts, keys, pdoors):
    possible_paths = []
    state = ("".join(starts), "".join(keys))
    if state in states:
        return states[state]
    for pos in starts:
        if pos in keys:
            keys.remove(pos)
        for path in pdoors:
            if pos in path and not pdoors[path]:
                possible_paths.append(path)
    mindist = 1_000_000
    if not possible_paths:
        return 0
    for path in possible_paths:
        for char in path:
            if char in starts:
                start = char
                ind = starts.index(start)
            else:
                end = char
        distance = psteps[path]
        door = end.upper()
        newpdoors = dict(pdoors)
        for path in pdoors:
            if path in newpdoors and start in path:
                del newpdoors[path]
            elif path in newpdoors and door in newpdoors[path]:
                idx = newpdoors[path].index(door)
                newpdoors[path] = list(newpdoors[path])
                del newpdoors[path][idx]
        newkeys = list(keys)
        newkeys.remove(end)
        newstarts = list(starts)
        [newstarts.append(end), newstarts.pop(ind)]
        distance += find_keys(newstarts, newkeys, newpdoors)
        if distance < mindist:
            mindist = distance
    states[state] = mindist
    return mindist

day = 18

startmap = open_file(1)
find_pairs()
keys = list(keyset)
states = {}
print(find_keys(starts, keys, pdoors))

startmap = open_file(2)
find_pairs()
keys = list(keyset)
states = {}
print(find_keys(starts, keys, pdoors))