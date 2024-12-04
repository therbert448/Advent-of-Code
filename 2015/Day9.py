def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global pairs, locations
    pairs = {}
    locations = set()
    for line in inputs:
        a, _, b, _, dist = line.split(" ")
        dist = int(dist)
        pair = tuple(sorted([a, b]))
        pairs[pair] = dist
        locations.add(a)
        locations.add(b)

def shortest_route(start, left):
    state = (start, "".join(sorted(left)))
    if state in routes:
        return routes[state]
    mindist = -1
    for nextloc in left:
        pair = tuple(sorted([start, nextloc]))
        if pair not in pairs:
            continue
        dist = pairs[pair]
        newlocs = set(left)
        newlocs.remove(nextloc)
        if not newlocs:
            return dist
        dist += shortest_route(nextloc, newlocs)
        if mindist == -1 or dist < mindist:
            mindist = dist
    routes[state] = mindist
    return mindist

def longest_route(start, left):
    state = (start, "".join(sorted(left)))
    if state in routes:
        return routes[state]
    maxdist = 0
    for nextloc in left:
        pair = tuple(sorted([start, nextloc]))
        if pair not in pairs:
            continue
        dist = pairs[pair]
        newlocs = set(left)
        newlocs.remove(nextloc)
        if not newlocs:
            return dist
        dist += longest_route(nextloc, newlocs)
        if dist > maxdist:
            maxdist = dist
    routes[state] = maxdist
    return maxdist

def part_one():
    global routes
    routes = {}
    mindist = -1
    for start in locations:
        newlocs = set(locations)
        newlocs.remove(start)
        dist = shortest_route(start, newlocs)
        if mindist == -1 or dist < mindist:
            mindist = dist
    print(f"Part One: {mindist}")

def part_two():
    global routes
    routes = {}
    maxdist = 0
    for start in locations:
        newlocs = set(locations)
        newlocs.remove(start)
        dist = longest_route(start, newlocs)
        if dist > maxdist:
            maxdist = dist
    print(f"Part Two: {maxdist}")

day = 9
open_file()

format_data()

part_one()
part_two()