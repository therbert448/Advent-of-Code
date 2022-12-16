"""
Advent of Code
2022 Day 16

@author: Tom Herbert

I'm pleased with this solution.
Part One works out all the possible routes for a 30 min time limit and saves
the flow for each route.

Despite already having the function to save all the routes for a given time 
limit, my initial approach to Part Two was very laborious; I spent too long
trying the model the two parallel paths and whilst the code worked on the 
example, the real input was far too large to produce a result in a reasonable
amount of time.

Eventually I realised that I could generate all the paths for the 26 min time
limit, then go through the paths trying to find pairs that didn't share a stop,
i.e. they could run in parallel independently.
Then for all of these pairs of parallel paths, I just needed to find the max
combined flow rate.
This approach ended up being a lot quicker.
"""

day = 16

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip().split() for line in file.readlines()]
    return inputs

def format_data():
    global valves
    valves = {}
    for line in inputs:
        _, valve, _, _, rate, _, _, _, _, *tunnels = line
        rate = int(rate.strip(";").split("=")[-1])
        tunnels = [tunnel.strip(",") for tunnel in tunnels]
        valves[valve] = {"rate": rate, "tunnels": tunnels, "routes": {}}

def find_stops():
    global stops
    stops = []
    for valve, values in valves.items():
        if values["rate"] != 0:
            stops.append(valve)
    stops.append("AA")

def find_routes():
    for start in stops:
        for end in stops:
            if start == end:
                continue
            current = start
            moves = set(valves[current]["tunnels"])
            steps = 1
            found = False
            while not found:
                nextMoves = set()
                for valve in moves:
                    if valve == end:
                        found = True
                        valves[start]["routes"][end] = steps
                        break
                    for nextMove in valves[valve]["tunnels"]:
                        nextMoves.add(nextMove)
                moves = nextMoves
                steps += 1

def open_state(openValves):
    opened = list(openValves)
    openString = ".".join(opened)
    return openString

def calculate_moves(path, opened, unopened, flow, time):
    maxFlow = flow
    current = path
    for valve in unopened:
        nUnopened = list(unopened)
        nOpened = list(opened)
        nPath = valve
        steps = valves[current]["routes"][valve] + 1
        tLeft = time - steps
        if tLeft <= 0:
            continue
        extraFlow = tLeft * valves[valve]["rate"]
        nFlow = flow + extraFlow
        nUnopened.remove(valve)
        nOpened.append(valve)
        state = open_state(nOpened)
        if state in states and nFlow > states[state]:
            states[state] = nFlow
        elif state not in states:
            states[state] = nFlow
        nFlow = calculate_moves(nPath, nOpened, nUnopened, nFlow, tLeft)
        if nFlow > maxFlow:
            maxFlow = nFlow
    return maxFlow

def find_path_pairs():
    best = max(state[1] for state in states)
    maxLen = (len(stops) * 2) + 2
    for i, items in enumerate(states):
        first, firstFlow = items
        if firstFlow + states[i+1][1] <= best:
            break
        if 2 * (len(first) + 1)//3 == maxLen:
            continue
        for items2 in states[i+1:]:
            second, secondFlow = items2
            if firstFlow + secondFlow <= best:
                break
            if 2 * (len(second) + 1)//3 == maxLen:
                continue
            duplicates = False
            for stop in stops:
                if stop in first and stop in second:
                    duplicates = True
                    break
            if not duplicates:
                best = firstFlow + secondFlow
    return best

def part_one():
    global states
    path = "AA"
    opened = [path]
    unopened = list(stops)
    flow = 0
    time = 30
    stateString = open_state(opened)
    states = {stateString: flow}
    maxFlow = calculate_moves(path, opened, unopened, flow, time)
    print(f"Part One = {maxFlow}")

def part_two():
    global states
    path = "AA"
    opened = [path]
    unopened = list(stops)
    flow = 0
    time = 26
    stateString = open_state(opened)
    states = {stateString: flow}
    calculate_moves(path, opened, unopened, flow, time)
    states = sorted(states.items(), key = lambda item: item[1], reverse = True)
    best = find_path_pairs()
    print(f"Part Two = {best}")

inputs = open_file()

format_data()

find_stops()
find_routes()
stops.remove("AA")

part_one()
part_two()
