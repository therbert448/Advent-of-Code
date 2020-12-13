def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global time
    global buses
    global allbuses
    time = int(inputs[0])
    buses = inputs[1].split(",")
    allbuses = []
    for b in buses:
        if b != "x":
            allbuses.append(int(b))
        else:
            allbuses.append(b)
    buses = [int(b) for b in buses if b != "x"]
    
    return

def bus_time(bus, time):
    b = bus
    while bus < time:
        bus += b
    return bus

def next_bus():
    times = []
    for bus in buses:
        t = bus_time(bus, time)
        times.append(t)
    tbus = min(times)
    wait = tbus - time
    nextbus = buses[times.index(tbus)]
    answer = wait * nextbus
    return answer

def bus_sequence():
    firstbus = allbuses[0]
    t = []
    for i in range(1, len(allbuses)):
        if allbuses[i] == "x":
            continue
        for j in range(firstbus):
            bus = allbuses[i] * (j+1)
            rem = bus % firstbus
            if rem == i % firstbus:
                time = bus
                while time < i:
                    time += allbuses[i] * firstbus
                t.append(time - i)
                break
            
    addwait = max(buses) * firstbus
    maxt = max(t)
    idxmax = t.index(maxt)
    for j in range(len(t)):
        dif = maxt - t[j]
        mod = buses[j+1] * firstbus
        rem = dif % mod
        while rem != 0:
            maxt += addwait
            dif = maxt - t[j]
            rem = dif % mod
        if j != idxmax:
            addwait *= buses[j+1]
    
    return maxt

day = 13
inputs = open_file()

formatdata(inputs)

print(next_bus())
print(bus_sequence())
