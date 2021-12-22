"""
Advent of Code
2021 Day 22

@author: Tom Herbert
"""

class Cube:
    def __init__(self, bounds, minD = False, maxD = False):
        self.minD, self.maxD = minD, maxD
        self.inRange = 1
        xmin, xmax, ymin, ymax, zmin, zmax = bounds
        if minD or maxD:
            if xmin > maxD or ymin > maxD or zmin > maxD:
                self.inRange = 0
            if xmax < minD or ymax < minD or zmax < minD:
                self.inRange = 0
            xmin, ymin, zmin = max(xmin, minD), max(ymin, minD), max(zmin, minD)
            xmax, ymax, zmax = min(xmax, maxD), min(ymax, maxD), min(zmax, maxD)
        self.bounds = [(xmin, xmax), (ymin, ymax), (zmin, zmax)]
        self.offCubes = []
    
    def intersection(self, other):
        selfBounds, otherBounds = self.bounds, other.bounds
        newBounds = []
        for i, axis in enumerate(selfBounds):
            otherAxis = otherBounds[i]
            if axis[1] < otherAxis[0] or axis[0] > otherAxis[1]:
                return False
            newBounds.append(max(axis[0], otherAxis[0]))
            newBounds.append(min(axis[1], otherAxis[1]))
        return newBounds
    
    def remove_intersection(self, other):
        bounds = self.intersection(other)
        if bounds:
            for cube in self.offCubes:
                #if new cube intersects with a previous intersection
                cube.remove_intersection(other)
                #keep track of additional intersections
            self.offCubes.append(Cube(bounds, self.minD, self.maxD))
            #add cube object to keep track of all intersections
    
    def calculate_volume(self):
        volume = 1
        for i, axis in enumerate(self.bounds):
            volume *= axis[1] + 1 - axis[0]
        volume -= sum([cube.calculate_volume() for cube in self.offCubes])
        return volume

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [line.strip().split() for line in file.readlines()]
    file.close()
    return inputs

def format_data():
    global steps
    steps = []
    for line in inputs:
        onOff, bounds = line
        x, y, z = bounds.split(",")
        x = [int(val) for val in x[2:].split("..")]
        y = [int(val) for val in y[2:].split("..")]
        z = [int(val) for val in z[2:].split("..")]
        steps.append([onOff, (*x, *y, *z)])

def part_one():
    global cubes
    cubes = []
    for line in steps:
        onOff, bounds = line
        newCube = Cube(bounds, -50, 50)
        if newCube.inRange:
            for cube in cubes:
                cube.remove_intersection(newCube)
                #if next step intersects with a previous cube
                #even if new cube is on or off
                #remove the intersection from the previous cube
                #if new cube on, intersection will be counted in new cube
                #if new cube off, previous cube should remove intersection
            if onOff == "on":
                cubes.append(newCube)
                #if new cube on, remove any sections of previous cubes where
                #they intersect, and count that removed section as part of this
                #new cube
    answer = sum([cube.calculate_volume() for cube in cubes])
    print(f"Part One = {answer}")

def part_two():
    global cubes
    cubes = []
    for line in steps:
        onOff, bounds = line
        newCube = Cube(bounds)
        for cube in cubes:
            cube.remove_intersection(newCube)
        if onOff == "on":
            cubes.append(newCube)
    answer = sum([cube.calculate_volume() for cube in cubes])
    print(f"Part Two = {answer}")

day = 22
inputs = open_file()

format_data()

part_one()
part_two()