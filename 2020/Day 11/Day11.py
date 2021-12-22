import time

t0 = time.perf_counter()

def open_file(day):
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    lines = [i.strip() for i in inputs]
    global rows
    rows = []
    for line in lines:
        row = []
        for l in line:
            row.append(l)
        rows.append(row)
    return rows

def copy_list(list):
    new_list = []
    for i in range(len(list)):
        row = []
        for j in range(len(list[i])):
            row.append(list[i][j])
        new_list.append(row)
    return new_list
            

def adjseats(pos, rowsin):
    square = [-1, 0, 1]
    x = pos[0]
    y = pos[1]
    fullcount = 0
    for i in square:
        dx = x + i
        if dx < 0 or dx >= len(rowsin):
            continue
        for j in square:
            dy = y + j
            if dy < 0 or dy >= len(rowsin[i]):
                continue
            if [i, j] == [0, 0]:
                continue

            if rowsin[dx][dy] == "#":
                fullcount += 1
    
    return fullcount

def newadjseats(pos, rowsin, part):
    square = [-1, 0, 1]
    norows = len(rowsin)
    nocols = len(rowsin[0])
    x = pos[0]
    y = pos[1]
    fullcount = 0
    for i in square:
        dx = x + i
        if dx < 0 or dx >= norows:
            continue
        for j in square:
            dy = y + j
            if dy < 0 or dy >= nocols:
                continue
            if [i, j] == [0, 0]:
                continue

            if part == "a":
                if rowsin[dx][dy] == "#":
                    fullcount += 1

            elif part == "b":
                for n in range(1, min([norows, nocols])):
                    dx = x + (n * i)
                    dy = y + (n * j)

                    if dx < 0 or dx >= norows or dy < 0 or dy >= nocols:
                        break
                
                    if rowsin[dx][dy] == "#":
                        fullcount += 1
                        break
                    elif rowsin[dx][dy] == "L":
                        break
    
    return fullcount

def change_places(rowsin, part):
    changes = 0
    if part == "a":
        fullmin = 4
    elif part == "b":
        fullmin = 5
    maxrows = len(rowsin)
    rowsout = copy_list(rowsin)
    for i in range(maxrows):
        maxcols = len(rowsout[i])
        for j in range(maxcols):
            seat = rowsout[i][j]
            if seat == ".":
                continue
            else:
                pos = [i, j]
                full = newadjseats(pos, rowsin, part)
            if seat == "L" and full == 0:
                rowsout[i][j] = "#"
                changes += 1
            elif seat == "#" and full >= fullmin:
                rowsout[i][j] = "L"
                changes += 1
    return changes, rowsout
                        
def iterate_changes(part):
    newrow = copy_list(rows)
    #print(newrow[0])
    count = 0
    changes = 1
    while changes != 0:
        count += 1
        rowsin = copy_list(newrow)
        changes, newrow = change_places(rowsin, part)
        #print(newrow[0])
        if count > 100 and changes != 0:
            print("100 iterations and no result")
            return 0
    countseat = 0
    for row in newrow:
        c = row.count("#")
        countseat += c
    return countseat    

day = 11
inputs = open_file(day)

formatdata(inputs)

t1 = time.perf_counter()
print(iterate_changes("a"))
t2 = time.perf_counter()
print(iterate_changes("b"))
t3 = time.perf_counter()

print(f"Part 1 took {t2 - t1:0.4f} seconds")
print(f"Part 2 took {t3 - t2:0.4f} seconds")
print(f"Total time = {t3 - t0:0.4f} seconds")



