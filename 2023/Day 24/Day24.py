"""
Advent of Code
2023 Day 24

@author: Tom Herbert

Using sequences from Day 9
"""

import z3

day = 24

class Hailstone:
    def __init__(self, line):
        self.px, self.py, self.pz = [int(v) for v in line[0].split(",")]
        self.vx, self.vy, self.vz = [int(v) for v in line[1].split(",")]
        self.intersections = []
    
    def find_intersection_2D(self, other):
        px1, py1, vx1, vy1 = self.px, self.py, self.vx, self.vy
        px2, py2, vx2, vy2 = other.px, other.py, other.vx, other.vy
        x1, x2 = px1, px1 + vx1
        x3, x4 = px2, px2 + vx2
        y1, y2 = py1, py1 + vy1
        y3, y4 = py2, py2 + vy2
        den = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
        if not den: return False
        xnom = (x1*y2 - y1*x2)*(x3-x4) - (x3*y4 - y3*x4)*(x1 - x2)
        ynom = (x1*y2 - y1*x2)*(y3-y4) - (x3*y4 - y3*x4)*(y1 - y2)
        x = xnom/den
        y = ynom/den
        t1 = (x - px1)/vx1
        t2 = (x - px2)/vx2
        if t1 < 0 or t2 < 0:
            return False
        if limits[0] <= x <= limits[1] and limits[0] <= y <= limits[1]:
            return True
        return False

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        hail = [Hailstone(l.strip().split(" @ ")) for l in file.readlines()]
    return hail

def find_hailstone():
    solver = z3.Solver()
    x, y, z, a, b, c = map(z3.Int, "xyzabc")
    ts = [z3.Int(f"t{i}") for i in range(3)]
    for i, hailstone in enumerate(hail[:3]):
        t = ts[i]
        solver.add(x + t * a == hailstone.px + t * hailstone.vx)
        solver.add(y + t * b == hailstone.py + t * hailstone.vy)
        solver.add(z + t * c == hailstone.pz + t * hailstone.vz)
    solver.check()
    mod = solver.model()
    xyz = [mod[i].as_long() for i in (x, y, z)]
    return sum(xyz)

def part_one():
    count = 0
    for i, hailstone in enumerate(hail):
        for stone2 in hail[i+1:]:
            meet = hailstone.find_intersection_2D(stone2)
            if meet: count += 1
    print(f"Part One = {count}")

def part_two():
    result = find_hailstone()
    print(f"Part Two = {result}")

hail = open_file(day)

limits = [200000000000000, 400000000000000]

part_one()
part_two()