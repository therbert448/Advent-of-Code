def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global orbits
    orbits = {}
    lines = [line.strip().split(")") for line in inputs]
    for line in lines:
        orbits[line[1]] = line[0]    

def count_orbit(obj):
    if obj in orbits:
        count = 1 + count_orbit(orbits[obj])
        return count
    elif obj == "COM":
        return 0
    else:
        print("Inner object doesn't orbit anything")
        return 0

def all_orbits():
    count_orbs = {}
    for obj in orbits:
        count_orbs[obj] = count_orbit(obj)
    sumorbs = 0
    for orbs in count_orbs:
        sumorbs += count_orbs[orbs]
    return sumorbs
        
def trace_obj(obj):
    orblist = []
    COM = 0
    while not COM:
        obj = orbits[obj]
        orblist.append(obj)
        if obj == "COM":
            COM = 1
    return orblist

def find_common_obj():
    you = "YOU"
    santa = "SAN"
    paths = {}
    paths[you] = trace_obj(you)
    paths[santa] = trace_obj(santa)
    for i, obj in enumerate(paths[you]):
        if obj in paths[santa]:
            break
    j = paths[santa].index(obj)
    dist = i + j
    return dist
        
day = 6
inputs = open_file()

formatdata(inputs)

print(all_orbits()) #295834
print(find_common_obj()) #361