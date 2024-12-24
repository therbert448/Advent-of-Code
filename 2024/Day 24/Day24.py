"""
Advent of Code
2024 Day 24

@author: Tom Herbert
"""
from time import time

day = 24

def open_file(day):
    #filename = "test2.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as f:
        A, B = [b.strip().splitlines() for b in f.read().split("\n\n")]
    A = [line.strip().split(": ") for line in A]
    values = {line[0]: int(line[1]) for line in A}
    gates = {}
    for line in B:
        inputs, output = line.strip().split(" -> ")
        a, gate, b = inputs.split(" ")
        if output in gates: print("?")
        gates[output] = [(a, b), gate]
    return values, gates

values, gates = open_file(day)
operations, xyXORs, xyANDs, XORs, ANDs, ORs = {}, {}, {}, {}, {}, {}
for wire, op in gates.items():
    (a, b), gate = op
    wires = sorted([a, b])
    operations[(wires[0], gate, wires[1])] = wire
    if a[0] in ("x", "y") and b[0] in ("x", "y"):
        if gate == "XOR":
            xyXORs[a[1:]] = wire
        if gate == "AND":
            xyANDs[a[1:]] = wire
    elif gate == "XOR":
        XORs[a] = (b, wire)
        XORs[b] = (a, wire)
    elif gate == "AND":
        ANDs[a] = (b, wire)
        ANDs[b] = (a, wire)
    elif gate == "OR":
        ORs[a] = (b, wire)
        ORs[b] = (a, wire)

toDetermine = set(v for v in gates)

while toDetermine:
    newToDetermine = set(v for v in toDetermine)
    for wire in toDetermine:
        (wireA, wireB), gate = gates[wire]
        if all(inWire in values for inWire in (wireA, wireB)):
            a, b = values[wireA], values[wireB]
            if gate == "AND":
                result = int(a and b)
            elif gate == "OR":
                result = int(a or b)
            elif gate == "XOR":
                result = int(a ^ b)
            else:
                print("??")
            values[wire] = result
            newToDetermine.remove(wire)
    toDetermine = set(v for v in newToDetermine)
zWires = sorted([wire for wire in values if wire[0] == "z"], reverse=True)
zbinary = ""
for z in zWires:
    zbinary += str(values[z])
z = int(zbinary, 2)
print(z)

swapped, swappedDict = set(), {}
carryOver = None
for i in range(len(zWires)):
    bit = str(i).zfill(2)
    zi = "z" + bit
    if i == len(zWires) - 1:
        if zi != carryOver:
            swapped.add(zi), swapped.add(carryOver)
        break
    xyXOR = xyXORs[bit]
    xyAND = xyANDs[bit]
    if not i:
        if zi != xyXOR:
            swapped.add(zi), swapped.add(xyXOR)
        carryOver = xyAND
    else:
        wires = sorted([xyXOR, carryOver])
        XOR = (wires[0], "XOR", wires[1])
        if XOR not in operations:
            if carryOver not in XORs:
                other, XORout = XORs[xyXOR]
                swapped.add(carryOver), swapped.add(other)
                swappedDict[other] = carryOver
                carryOver = other
            elif xyXOR not in XORs:
                other, XORout = XORs[carryOver]
                swapped.add(xyXOR), swapped.add(other)
                swappedDict[other] = xyXOR
                xyXOR = other
            wires = sorted([xyXOR, carryOver])
            XOR = (wires[0], "XOR", wires[1])
        AND = (wires[0], "AND", wires[1])
        XORout = operations[XOR]
        if XORout in swappedDict: XORout = swappedDict[XORout]
        if XORout != zi:
            swapped.add(zi), swapped.add(XORout)
        ANDout = operations[AND]
        if ANDout in swappedDict: ANDout = swappedDict[ANDout]
        wires = sorted([xyAND, ANDout])
        OR = (wires[0], "OR", wires[1])
        if OR not in operations:
            if ANDout not in ORs:
                other, ORout = ORs[xyAND]
                swapped.add(ANDout), swapped.add(other)
                swappedDict[other] = ANDout
                ANDout = other
            elif xyAND not in ORs:
                other, ORout = ORs[ANDout]
                swapped.add(xyAND), swapped.add(other)
                swappedDict[other] = xyAND
                xyAND = other
            wires = sorted([xyAND, ANDout])
            OR = (wires[0], "OR", wires[1])
        ORout = operations[OR]
        if ORout in swappedDict: ORout = swappedDict[ORout]
        carryOver = ORout
print(",".join(sorted(list(swapped))))