"""
Advent of Code
2023 Day 20

@author: Tom Herbert
"""

day = 20

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip().split(" -> ") for line in file.readlines()]
    modules, flipFlops, conjunctions = {}, {}, {}
    for line in inputs:
        start, ends = line
        ends = ends.split(", ")
        if start[0] == "%":
            flipFlops[start[1:]] = False
            modules[start[1:]] = ends
        elif start[0] == "&":
            conjunctions[start[1:]] = {}
            modules[start[1:]] = ends
        else:
            modules[start] = ends
    for conj in conjunctions:
        for start, ends in modules.items():
            if conj in ends:
                conjunctions[conj][start] = False
            if "rx" in ends: #rx has only one preceding module which is a conj 
                rx = start
    return modules, flipFlops, conjunctions, rx

def product(args):
    result = 1
    for arg in args:
        result *= arg
    return result

def galvanise(flipFlops, conjs, partTwo = False):
    high, low = 0, 0
    N = 1000
    i = 0
    loops = {k: 0 for k in conjs[rx]}
    while True:
        if partTwo and all(loops.values()):
            return product(loops.values())
        queue = [('button', False, 'broadcaster')]
        i += 1
        while queue:
            start, pulse, end = queue.pop(0)
            if pulse:
                high += 1
            else:
                low += 1
            if end == "broadcaster":
                outPulse = pulse
            elif end in flipFlops:
                if pulse:
                    continue
                flipFlops[end] = not flipFlops[end]
                outPulse = flipFlops[end]
            elif end in conjs:
                if start not in conjs[end]:
                    print("Input not recognised")
                    continue
                conjs[end][start] = pulse
                if all(conjs[end].values()):
                    outPulse = False
                else:
                    outPulse = True
                if pulse and end == rx:
                    loops[start] = i
            if end not in modules: continue
            for dest in modules[end]:
                queue.append((end, outPulse, dest))
        activeFlipFlops = any(flipFlops.values())
        activeConjs = any(any(conj.values()) for conj in conjs.values())
        if not activeFlipFlops and not activeConjs:
            break
        if not partTwo and i >= N:
            return high * low

def part_one():
    newFlipFlops = {k: v for k, v in flipFlops.items()}
    newConjs = {k: {k2: v2 for k2, v2 in v.items()} for k, v in conjs.items()}
    result = galvanise(newFlipFlops, newConjs)
    print(f"Part One = {result}")

def part_two():
    newFlipFlops = {k: v for k, v in flipFlops.items()}
    newConjs = {k: {k2: v2 for k2, v2 in v.items()} for k, v in conjs.items()}
    result = galvanise(newFlipFlops, newConjs, True)
    print(f"Part Two = {result}")

modules, flipFlops, conjs, rx = open_file(day)

part_one()
part_two()