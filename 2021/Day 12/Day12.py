"""
Advent of Code
2021 Day 12

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def format_data():
    global links, bigCaves, smallCaves
    links, bigCaves, smallCaves = set(), set(), set()
    for line in inputs:
        start, end = line.strip().split("-")
        links.add(tuple([start, end]))
        for string in [start, end]:
            if string.isupper():
                bigCaves.add(string)
            else:
                smallCaves.add(string)

def make_moves(pos, route, routes):
    options = [link for link in links if pos in link]
    for o in options:
        for node in o:
            if node != pos:
                nextPos = node
        newRoute = list(route)
        if nextPos in route and nextPos in smallCaves:
            continue
        if nextPos == "end":
            newRoute.append(nextPos)
            routes.add(tuple(newRoute))
        else:
            newRoute.append(nextPos)
            routes = make_moves(nextPos, newRoute, routes)
    return routes      

def make_moves2(pos, route, routes, twice):
    options = [link for link in links if pos in link]
    for o in options:
        newTwice = twice
        for node in o:
            if node != pos:
                nextPos = node
        newRoute = list(route)
        if nextPos == "start":
            continue
        if nextPos in route and nextPos in smallCaves and newTwice:
            continue
        if nextPos == "end":
            newRoute.append(nextPos)
            routes.add(tuple(newRoute))
        else:
            if nextPos in route and nextPos in smallCaves and not newTwice:
                newTwice = nextPos
            newRoute.append(nextPos)
            routes = make_moves2(nextPos, newRoute, routes, newTwice)
    return routes  

def part_one():
    pos = "start"
    routes = set()
    route = [pos]
    routes = make_moves(pos, route, routes)
    print(f"Part One = {len(routes)}")

def part_two():
    pos = "start"
    routes = set()
    route = [pos]
    twice = ""
    routes = make_moves2(pos, route, routes, twice)
    print(f"Part Two = {len(routes)}")

day = 12
inputs = open_file()

format_data()

part_one()
part_two()