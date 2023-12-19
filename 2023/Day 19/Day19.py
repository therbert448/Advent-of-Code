"""
Advent of Code
2023 Day 19

@author: Tom Herbert
"""

day = 19

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        first, second = file.read().split("\n\n")
    workflow = {}
    for line in first.splitlines():
        name, rules = line.split("{")
        workflow[name] = [r.split(":") for r in rules.strip("}").split(",")]
    parts = []
    for line in second.splitlines():
        ratings = line.strip("{}").split(",")
        xmas = [int(rating.split("=")[1]) for rating in ratings]
        parts.append(xmas)
    return workflow, parts

def run_workflow(part):
    x, m, a, s = part
    current = "in"
    while current not in ("A", "R"):
        for rule in workflow[current]:
            if len(rule) == 1:
                break
            if eval(rule[0]):
                break
        current = rule[-1]
    return current

def difference(ends):
    return ends[1] - ends[0] + 1

def product(args):
    result = 1
    for arg in args:
        result *= arg
    return result

def accepted_combos(current, ranges):
    if current == "R":
        return 0
    if current == "A":
        return product([difference(ends) for ends in ranges.values()])
    result = 0
    for rule in workflow[current]:
        dest = rule[-1]
        if len(rule) == 1:
            result += accepted_combos(dest, ranges)
            return result
        spinoffRanges = {k: v for k, v in ranges.items()}
        rating, inequal, *value = rule[0]
        value = int("".join(value))
        edges = ranges[rating]
        #Ranges are always split, so don't need to check if value is between edges
        if inequal == ">":
            spinoffRanges[rating] = (value+1, edges[1])
            ranges[rating] = (edges[0], value)
        else:
            spinoffRanges[rating] = (edges[0], value-1)
            ranges[rating] = (value, edges[1])
        result += accepted_combos(dest, spinoffRanges)

def part_one():
    accepted = []
    for part in parts:
        if run_workflow(part) == "A":
            accepted.append(sum(part))
    print(f"Part One = {sum(accepted)}")

def part_two():
    limits = (1, 4000)
    ratingRanges = {"x": limits, "m": limits, "a": limits, "s": limits}
    current = "in"
    result = accepted_combos(current, ratingRanges)
    print(f"Part Two = {result}")

workflow, parts = open_file(day)

part_one()
part_two()