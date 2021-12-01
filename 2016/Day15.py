def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global discs
    discs = {}
    for line in inputs:
        idx = line.index("#")
        num, *rest = line[idx+1:].split(" ")
        size = int(rest[1])
        startpos = int(rest[-1].strip("."))
        num = int(num)
        discs[num] = [size, startpos]

def find_time(part):
    if part == "Two":
        discs[7] = [11, 0]
    t = 0
    step = 1
    for disc in discs:
        length, startpos = discs[disc]
        firsttime = ((length - startpos) % length) - disc
        while firsttime < disc:
            firsttime += length
        while t != firsttime:
            if t < firsttime and (firsttime - t) % step == 0:
                t = firsttime
            elif t < firsttime:
                firsttime += length
            elif (t - firsttime) % length == 0:
                firsttime = t
            else:
                t += step
        step *= length
        t %= step
    print(f"Part {part}: {t}")
    
day = 15
open_file()

format_data()

find_time("One")
find_time("Two")