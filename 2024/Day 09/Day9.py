"""
Advent of Code
2024 Day 09

@author: Tom Herbert
"""
from time import time

day = 9

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.read()]
    disc = []
    for digit in inputs:
        disc.append(int(digit))
    return disc

disc = open_file(day)
files = [disc[i] for i in range(len(disc)) if not i%2]
t0 = time()
fullDisc = []
for i, size in enumerate(disc):
    if i % 2: val = "."
    else: val = i//2
    for _ in range(size): fullDisc.append(val)

newFullDisc = [0] * sum(files)
filled = [v for v in fullDisc if v != "."]
for i, val in enumerate(fullDisc):
    if i >= len(newFullDisc): break
    if val == ".":
        newVal = filled.pop(-1)
        newFullDisc[i] = newVal
    else:
        newFullDisc[i] = val

result = sum(i*val for i, val in enumerate(newFullDisc))
print(f"Part One = {result}")    
t1 = time()
print(f"...took {round(t1-t0, 6)}s\n")

fileIDs = list(range(len(files)))
empty = [disc[i] for i in range(len(disc)) if i%2]
ID = len(files) - 1
while ID > 0:
    size = files[ID]
    emptyPoint = fileIDs.index(ID)
    for i, empSize in enumerate(empty[:emptyPoint]):
        if size <= empSize:
            fileIDs.remove(ID)
            fileIDs.insert(i+1, ID)
            newEmpty = empSize - size
            empty[i] = 0
            empty.insert(i+1, newEmpty)
            left = empty.pop(emptyPoint)
            if emptyPoint < len(empty):
                empty[emptyPoint] += left + size
            break
    ID -= 1

finalFiles = [files[v] for v in fileIDs]
idx = 0
result = 0
for i, size in enumerate(finalFiles):
    ID = fileIDs[i]
    for _ in range(size):
        result += idx * ID
        idx += 1
    if i < len(empty):
        idx += empty[i]
print(f"Part Two = {result}")
t2 = time()
print(f"...took {round(t2-t1, 6)}s\n")