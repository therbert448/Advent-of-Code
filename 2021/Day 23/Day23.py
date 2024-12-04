"""
Advent of Code
2021 Day 1

@author: Tom Herbert
"""

doors = {"A": 2, "B": 4, "C": 6, "D": 8}
scores = {"A": 1, "B": 10, "C": 100, "D": 1000}
hallway = {}
hallwayLength = 11

def save_state(hallway, rooms):
    hall = ""
    for i in range(hallwayLength):
        if i in hallway:
            hall += hallway[i]
        else:
            hall += "."
    roomStates = ["".join(room) for room in rooms.values()]
    state = (hall, *roomStates)
    return state

def load_state(state):
    hall, a, b, c, d = state
    hallway = {}
    for i, char in enumerate(hall):
        if char != ".":
            hallway[i] = char
    rooms = {}
    rooms["A"] = [char for char in a]
    rooms["B"] = [char for char in b]
    rooms["C"] = [char for char in c]
    rooms["D"] = [char for char in d]
    return hallway, rooms

def next_move(hallway, rooms):
    moves = {}
    if hallway:
        for pos, amphi in hallway.items():
            if len(rooms[amphi]) == roomSize:
                continue
            if len(rooms[amphi]) and not all([a == amphi for a in rooms[amphi]]):
                continue
            moveable = True
            for a in hallway:
                if pos < a < doors[amphi] or doors[amphi] < a < pos:
                    moveable = False
            if not moveable:
                continue
            newRooms = {k: list(v) for k, v in rooms.items()}
            newHallway = dict(hallway)
            steps = abs(pos - doors[amphi]) + roomSize - len(rooms[amphi])
            newRooms[amphi].append(amphi)
            del newHallway[pos]
            state = save_state(newHallway, newRooms)
            moves[state] = steps * scores[amphi]
    for room, amphis in rooms.items():
        if not amphis or all([amp == room for amp in amphis]):
            continue
        moveable = amphis[-1]
        pos = doors[room]
        if hallway:
            left = max([val if val < pos else -1 for val in hallway]) + 1
            right = min([v if v > pos else hallwayLength for v in hallway])
        else:
            left, right = 0, hallwayLength
        for newPos in range(left, right):
            if newPos in doors.values():
                continue
            newRooms = {k: list(v) for k, v in rooms.items()}
            newHallway = dict(hallway)
            steps = abs(newPos - pos) + roomSize + 1 - len(amphis)
            newRooms[room].pop()
            newHallway[newPos] = moveable
            state = save_state(newHallway, newRooms)
            moves[state] = steps * scores[moveable]
    return moves

def make_move(state):
    currentScore = states[state]
    hallway, rooms = load_state(state)
    moves = next_move(hallway, rooms)
    for move, score in moves.items():
        newScore = currentScore + score
        if move in states and newScore >= states[move]:
            continue
        states[move] = newScore
        make_move(move)

def part_one():
    global states, moves
    states = {}
    state = save_state(hallway, rooms)
    states[state] = 0
    make_move(state)
    result = states[endState]
    print(f"Part One = {result}")

def part_two():
    global states, moves
    states = {}
    state = save_state(hallway, rooms)
    states[state] = 0
    make_move(state)
    result = states[endState]
    print(f"Part Two = {result}")

rooms = {"A": ["D", "A"],
         "B": ["A", "C"],
         "C": ["D", "B"],
         "D": ["B", "C"]}
endState = ("...........", "AA", "BB", "CC", "DD")
roomSize = len(rooms["A"])

part_one()

rooms = {"A": ["D", "D", "D", "A"],
         "B": ["A", "B", "C", "C"],
         "C": ["D", "A", "B", "B"],
         "D": ["B", "C", "A", "C"]}
endState = ("...........", "AAAA", "BBBB", "CCCC", "DDDD")
roomSize = len(rooms["A"])

part_two()