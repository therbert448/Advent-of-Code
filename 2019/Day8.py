def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().strip()
    file.close()
    return inputs

def formatdata(inputs):
    global layers
    layers = []
    w = 25
    h = 6
    layersize = w * h
    chars = [char for char in inputs]
    numlayers = int(len(chars)/layersize)
    for i in range(numlayers):
        rows = []
        for j in range(h):
            row = []
            for k in range(w):
                idx = (i * w * h) + (j * w) + k
                row.append(chars[idx])
            rows.append(row)
        layers.append(rows)
                
def part_one():
    layercount = []
    for l in layers:
        zcount = 0
        for row in l:
            zcount += row.count("0")
        layercount.append(zcount)
    mincount = min(layercount)
    layer = layers[layercount.index(mincount)]
    onecount = 0
    twocount = 0
    for row in layer:
        onecount += row.count("1")
        twocount += row.count("2")
    answer = onecount * twocount
    return answer

def part_two():
    pixcol = []
    w = 25
    h = 6
    for i in range(h):
        row = []
        for j in range(w):
            for k in range(len(layers)):
                if layers[k][i][j] != "2":
                    if layers[k][i][j] == "0":
                        row.append(".")
                    else:
                        row.append(layers[k][i][j])
                    break
        row = "".join(row)
        pixcol.append(row)
    for row in pixcol:
        print(row)
    return
        
day = 8
inputs = open_file()

formatdata(inputs)

print(part_one())
part_two()