"""
Advent of Code
2022 Day 16

@author: Tom Herbert
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
    # Reduce all the valves down to only the ones with flow rates
    # No point stopping and opening a valve if it has zero flow rate
    # This list is all the valves that should be stopped at
    global stops
    stops = []
    for valve, values in valves.items():
        if values["rate"] != 0:
            stops.append(valve)
    stops.append("AA")

def find_routes(): 
    # For all the possible stops, calculate the number of steps between it and
    # any other stop, including the starting position "AA"
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
    stops.remove("AA")

def open_state(path):
    # Keep an ordered list of the paths visited. When opening a valve, store 
    # this order and the associated flow rate.
    opened = list(path) #path is the list of opened valves, in order
    openString = ".".join(opened)
    return openString #String to be used as a key for the states dict.

def calculate_moves(path, opened, unopened, flow, time):
    # Given a current position and a list of unopened valves, move to each of 
    # the unopened valves in turn, calculating the flow rate when opening that
    # valve next.
    current = path
    for valve in unopened: # Go to each unopened valve
        nUnopened = list(unopened)
        nOpened = list(opened)
        nPath = valve
        steps = valves[current]["routes"][valve] + 1
        tLeft = time - steps 
        #Calculate how much time is left after valve is opened
        if tLeft <= 0: #If there's no time left, this move isn't possible
            continue
        extraFlow = tLeft * valves[valve]["rate"] 
        nFlow = flow + extraFlow #Calculate new flow rate after valve is opened
        nUnopened.remove(valve) #Make sure this valve won't be returned to
        nOpened.append(valve) #Keep track of the path taken
        state = open_state(nOpened) #Make a key out of the path
        states[state] = nFlow #Save the path and the flow rate
        calculate_moves(nPath, nOpened, nUnopened, nFlow, tLeft)
        #Move on to next position

def find_path_pairs():
    # Find the paths that can be run in parallel, without either stopping at 
    # the same stop
    best = max(state[1] for state in states) 
    #best is at least the best flow rate of a single path
    maxLen = (len(stops) * 2) + 2
    #Each path lists every 2 character stop, plus "AA", which doesn't open
    for i, items in enumerate(states): 
        #Start from the highest flow rate path and move down
        first, firstFlow = items
        if firstFlow + states[i+1][1] <= best:
            #If this flow rate plus the next highest flow rate isn't as big as
            #the current best, this will not be the answer
            break
        if 2 * (len(first) + 1)//3 == maxLen:
            #If this path opened all the valves, then there is no parallel path
            continue
        for items2 in states[i+1:]:
            second, secondFlow = items2
            if firstFlow + secondFlow <= best:
                #If the sum of the two flow rates is less than the current best
                #Then this will not be the answer
                break
            if 2 * (len(second) + 1)//3 == maxLen:
                #If the second path opened all the valves...
                continue
            duplicates = False
            for stop in stops:
                if stop in first and stop in second:
                    #Check that no stop appears in both paths
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
    calculate_moves(path, opened, unopened, flow, time)
    print(f"Part One = {max(states.values())}")

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
    #Sorting the states in descending order of flow rate makes the pair search
    #quicker
    best = find_path_pairs()
    print(f"Part Two = {best}")

inputs = open_file()

format_data()

find_stops()
find_routes()

part_one()
part_two()