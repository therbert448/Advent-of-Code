def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.readlines()
    inputs = [line.strip() for line in inputs]
    inputs = sorted(inputs)
    file.close()

def formatdata():
    global guards, gmincount, gtimes, times
    guards = set()
    times = set()
    gmincount = {}
    gtimes = {}
    for i, line in enumerate(inputs):
        if "Guard" in line:
            time, guardID = line.split("Guard ")
            guardID = guardID.split(" ")[0]
            guards.add(guardID)
            times.add(time.strip(" []"))
            inputs[i] = time + guardID
        elif "asleep" in line:
            time, _ = line.split("] ")
            times.add(time.strip(" []"))
            inputs[i] = line.replace("falls asleep", "asleep")
        else:
            time, _ = line.split("] ")
            times.add(time.strip(" []"))
            inputs[i] = line.replace("wakes up", "awake")
    mincount = [0 for i in range(60)]
    for guard in guards:
        gmincount[guard] = list(mincount)
        gtimes[guard] = set()

def count_mins():
    guard = ""
    for line in inputs:
        if "#" in line:
            _, guard = line.split("] ")
        elif "asleep" in line:
            time, _ = line.strip("[").split("] ")
            shorttime, minute = time.split(":")
            minute = int(minute)
            gtimes[guard].add(time)
            gmincount[guard][minute] += 1
            while minute < 59:
                minute += 1
                time = shorttime + ":" + str(minute).zfill(2)
                if time in times:
                    break
                gtimes[guard].add(time)
                gmincount[guard][minute] += 1

def part_one():
    count_mins()
    maxmins = 0
    for guard in gtimes:
        totalmins = len(gtimes[guard])
        if totalmins > maxmins:
            maxmins = totalmins
            g = guard
    mincount = gmincount[g]
    minno = mincount.index(max(mincount))
    g = int(g.strip("#"))
    print("Part One:", minno * g)

def part_two():
    highestcount = 0
    for guard in gmincount:
        mincount = gmincount[guard]
        highcount = max(mincount)
        highmin = mincount.index(highcount)
        if highcount > highestcount:
            highestcount = highcount
            highestmin = highmin
            g = int(guard.strip("#"))
    print("Part Two:", g * highestmin)
    

day = 4
open_file()

formatdata()
part_one()
part_two()