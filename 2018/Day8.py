def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global tree
    #tree = [2,3,0,3,10,11,12,1,1,0,1,99,2,1,1,2]
    tree = [int(line) for line in file.read().split(" ")]
    file.close()

def find_meta(idx):
    start = idx
    numnodes = tree[idx]
    metalen = tree[idx+1]
    idx += 2
    metasum = 0
    for _ in range(numnodes):
        idx, meta = find_meta(idx)
        metasum += meta
    metasum += sum(tree[idx:idx+metalen])
    idx += metalen
    end = idx
    nodedict[start] = [end, numnodes, metalen]
    return idx, metasum   

def find_root(idx):
    node = newnodedict[idx]
    end, count, meta = node
    if count == 0:
        metasum = sum(tree[end-meta:end])
        return metasum
    childs = []
    idx += 2
    for _ in range(count):
        childs.append(idx)
        idx = newnodedict[idx][0]
    metaids = tree[end-meta:end]
    iddict = {}
    metasum = 0
    for met in metaids:
        if 0 < met <= count and met not in iddict:
            idx = childs[met-1]
            metsum = find_root(idx)
            iddict[met] = metsum
            metasum += metsum
        elif met in iddict:
            metasum += iddict[met]
    return metasum
    
day = 8
open_file()


nodedict = {}
_, metasum = find_meta(0)
print("Part One:", metasum)

newnodedict = {}
for key in sorted(nodedict.keys()):
    newnodedict[key] = list(nodedict[key])
    
print("Part Two:", find_root(0))