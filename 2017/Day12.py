def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global connected, allprogs
    connected = {}
    allprogs = set()
    for line in inputs:
        proga, progsb = line.split(" <-> ")
        progsb = set(progsb.split(", "))
        connected[proga] = progsb
        allprogs.add(proga)

def connected_to(program):
    global connset
    connset = {program}
    addset = set(connset)
    while addset:
        newset = set()
        for progid in addset:
            progset = connected[progid]
            newset.update(progset)
        addset = set()
        for n in newset:
            if n not in connset:
                addset.add(n)
        connset.update(newset)

def run():
    global grouplist
    grouplist = []
    #part one
    connected_to("0")
    print("Part One:", len(connset))
    #part two
    grouplist.append(connset)
    groupset = set(connset)
    progsleft = allprogs.symmetric_difference(groupset)
    while progsleft:
        sortprogsleft = sorted(progsleft)
        nextprog = sortprogsleft[0]
        connected_to(nextprog)
        grouplist.append(connset)
        groupset.update(connset)
        progsleft = allprogs.symmetric_difference(groupset)
    print("Part Two:", len(grouplist))

day = 12
open_file()

format_data()

run()