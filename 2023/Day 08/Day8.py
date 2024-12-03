"""
Advent of Code
2023 Day 8

@author: Tom Herbert
"""

day = 8

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        directions, block = file.read().split("\n\n")
    nodes = {}
    for line in block.splitlines():
        start, ends = line.strip().split(" = ")
        left, right = ends.strip("()").split(", ")
        nodes[start] = {'L': left, 'R': right}
    return directions, nodes

def run_network(directions, nodes):
    current, end = "AAA", "ZZZ"
    count = 0
    while current != end:
        dire = directions[count % len(directions)]
        current = nodes[current][dire]
        count += 1
    return count

def run_A_to_Z(LRs, nodes):
    current = set([node for node in nodes if node[-1] == 'A'])
    ends = []
    for i, node in enumerate(current):
        stops = {}
        count = 0
        looped = False
        while not looped:
            dire = LRs[count % len(LRs)]
            nextNode = nodes[node][dire]
            count += 1
            if nextNode[-1] == 'Z' and nextNode in stops:
                loops = [c % len(LRs) for c in stops[nextNode]]
                if any([count % len(LRs) == c for c in loops]):
                    looped = True
                    break
                stops[nextNode].append(count)
            elif nextNode[-1] == 'Z':
                stops[nextNode] = [count]
            node = nextNode
        stopList = []
        for stop in stops.values():
            stopList += stop
        ends.append(*stopList)
    return ends

def factors(num):
    end = int(pow(num, 0.5))
    facts = []
    for i in range(2, end+1):
        if not num % i:
            facts.append(i)
            facts.append(int(num/i))
    return set(facts)

def product(args):
    result = 1
    for arg in args:
        result *= arg
    return result

def LCM(a, b):
    aSet = factors(a)
    bSet = factors(b)
    common = aSet & bSet
    total = product([a, b])
    if common:
        total /= max(common)
    return int(total)

def part_one(directions, nodes):
    print(f"Part One = {run_network(directions, nodes)}")

def part_two(directions, nodes):
    ends = run_A_to_Z(directions, nodes)
    a = ends[0]
    for b in ends[1:]:
        a = LCM(a, b)
    print(f"Part Two = {a}")

directions, nodes = open_file(day)

part_one(directions, nodes)
part_two(directions, nodes)