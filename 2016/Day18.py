def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global traps, rowlen
    row = file.read().strip()
    traps = set()
    rowlen = len(row)
    for i, char in enumerate(row):
        if char == "^":
            traps.add(i)
    file.close()

def next_row(prevrow):
    nextrow = set()
    for c in range(rowlen):
        l = c - 1
        r = c + 1
        if l in prevrow and c in prevrow and r not in prevrow:
            nextrow.add(c)
        elif l not in prevrow and c in prevrow and r in prevrow:
            nextrow.add(c)
        elif l in prevrow and c not in prevrow and r not in prevrow:
            nextrow.add(c)
        elif l not in prevrow and c not in prevrow and r in prevrow:
            nextrow.add(c)
    return nextrow

def safe_tiles(n):
    prevrow = set(traps)
    count = 0
    for i in range(n):
        count += rowlen - len(prevrow)
        if i == n-1:
            break
        prevrow = next_row(prevrow)
    if n == 40:
        print(f"Part One: {count}")
    else:
        print(f"Part Two: {count}")

day = 18
open_file()

safe_tiles(40)
safe_tiles(400000)