"""
Advent of Code
2021 Day 19

@author: Tom Herbert
"""

class Scanner:
    def __init__(self, beacons, orientated = False, pos = None):
        self.beacons = set(beacons)
        self.orientated = orientated
        self.pos = pos
        self.checked = set()
    
    def rotate(self, rotID):
        rotate = arrangements[rotID]
        beacons = set()
        for beac in self.beacons:
            newxyz = tuple([sum(map(multiply, xyz, beac)) for xyz in rotate])
            beacons.add(newxyz)
        return beacons
    
    def match(self, other):
        if not other.orientated:
            return False
        if other in self.checked:
            return False
        for rotID in arrangements:
            beacons = self.rotate(rotID)
            offs = {}
            for fixed in other.beacons:
                for beacon in beacons:
                    off = tuple(map(subtract, fixed, beacon))
                    if off not in offs:
                        offs[off] = 1
                    else:
                        offs[off] += 1
                    if offs[off] >= 12:
                        add = lambda a,b : a + b
                        new = set([tuple(map(add, b, off)) for b in beacons])
                        self.pos = tuple(off)
                        self.orientated = True
                        self.beacons = set(new)
                        allBeacons.update(new)
                        return True
        self.checked.add(other)
        return False

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [line.strip().splitlines() for line in file.read().split("\n\n")]
    file.close()
    return inputs

def format_data():
    global scanners, allBeacons
    scanners = []
    for i, beac in enumerate(inputs):
        beacons = [tuple([int(v) for v in l.strip().split(",")]) for l in beac[1:]]
        if i == 0:
            pos = (0, 0, 0)
            scanner = Scanner(beacons, True, pos)
            allBeacons = set(beacons)
        else:
            scanner = Scanner(beacons)
        scanners.append(scanner)

def subtract(a, b):
    return a - b

def multiply (a, b):
    return a * b

def manhattan(a, b):
    return abs(a-b)

def part_one():
    while not all([scanner.orientated for scanner in scanners]):
        remaining = [scanner for scanner in scanners if not scanner.orientated]
        fixed = [scanner for scanner in scanners if scanner.orientated]
        for scanner in remaining:
            for fix in fixed:
                orientated = scanner.match(fix)
                if orientated:
                    break
    print(f"Part One = {len(allBeacons)}")

def part_two():
    maxManhattan = 0
    for i, scanner in enumerate(scanners):
        for s in scanners[i+1:]:
            manhattanDist = sum(map(manhattan, scanner.pos, s.pos))
            if manhattanDist > maxManhattan:
                maxManhattan = manhattanDist
    print(f"Part Two = {maxManhattan}")

day = 19
inputs = open_file()

format_data()

arrangements = {0:  [[1, 0, 0],  [0, 1, 0],  [0, 0, 1]],
                1:  [[1, 0, 0],  [0, 0, -1], [0, 1, 0]],
                2:  [[1, 0, 0],  [0, -1, 0], [0, 0, -1]],
                3:  [[1, 0, 0],  [0, 0, 1],  [0, -1, 0]],
                4:  [[-1, 0, 0], [0, 1, 0],  [0, 0, -1]],
                5:  [[-1, 0, 0], [0, 0, -1], [0, -1, 0]],
                6:  [[-1, 0, 0], [0, -1, 0], [0, 0, 1]],
                7:  [[-1, 0, 0], [0, 0, 1],  [0, 1, 0]],
                8:  [[0, 1, 0],  [0, 0, 1],  [1, 0, 0]],
                9:  [[0, 1, 0],  [-1, 0, 0], [0, 0, 1]],
                10: [[0, 1, 0],  [0, 0, -1], [-1, 0, 0]],
                11: [[0, 1, 0],  [1, 0, 0],  [0, 0, -1]],
                12: [[0, -1, 0], [0, 0, 1],  [-1, 0, 0]],
                13: [[0, -1, 0], [-1, 0, 0], [0, 0, -1]],
                14: [[0, -1, 0], [0, 0, -1], [1, 0, 0]],
                15: [[0, -1, 0], [1, 0, 0],  [0, 0, 1]],
                16: [[0, 0, 1],  [1, 0, 0],  [0, 1, 0]],
                17: [[0, 0, 1],  [0, 1, 0],  [-1, 0, 0]],
                18: [[0, 0, 1],  [-1, 0, 0], [0, -1, 0]],
                19: [[0, 0, 1],  [0, -1, 0], [1, 0, 0]],
                20: [[0, 0, -1], [1, 0, 0],  [0, -1, 0]],
                21: [[0, 0, -1], [0, 1, 0],  [1, 0, 0]],
                22: [[0, 0, -1], [-1, 0, 0], [0, 1, 0]],
                23: [[0, 0, -1], [0, -1, 0], [-1, 0, 0]]}

part_one()
part_two()