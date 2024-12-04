def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global happiness, guests
    happiness = {}
    guests = set()
    for line in inputs:
        a, _, gain, val, *_, b = line.split(" ")
        a = a[0]
        b = b[0]
        if gain == "lose":
            val = -int(val)
        else:
            val = int(val)
        pair = tuple(sorted([a, b]))
        if pair not in happiness:
            happiness[pair] = val
        else:
            happiness[pair] += val  
        guests.add(a)

def seat_guests(sat, left):
    newleft = sorted(left)
    if sat in newleft:
        newleft.remove(sat)
    if not newleft:
        pair = tuple(sorted([sat, "A"]))
        return happiness[pair]
    state = (sat, "".join(newleft))
    if state in states:
        return states[state]
    maxhappy = None
    for guest in newleft:
        pair = tuple(sorted([sat, guest]))
        happy = happiness[pair]
        happy += seat_guests(guest, newleft)
        if maxhappy == None or happy > maxhappy:
            maxhappy = happy
    states[state] = maxhappy
    return maxhappy

def part_one():
    global states
    states = {}
    maxhappy = seat_guests("A", guests)
    print(f"Part One: {maxhappy}")

def part_two():
    global states
    states = {}
    for guest in guests:
        pair = tuple(sorted([guest, "ME"]))
        happiness[pair] = 0
    guests.add("ME")
    maxhappy = seat_guests("A", guests)
    print(f"Part Two: {maxhappy}")

day = 13
open_file()

format_data()

part_one()
part_two()