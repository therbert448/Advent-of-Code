"""
Advent of Code
2023 Day 22

@author: Tom Herbert
"""

day = 22

class Brick:
    def __init__(self, i, line):
        self.x1, self.y1, self.z1 = [int(v) for v in line[0].split(",")]
        self.x2, self.y2, self.z2 = [int(v) for v in line[1].split(",")]
        self.ID = i
        self.settled = False
    
    def get_coords(self):
        coords = []
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                for z in range(self.z1, self.z2 + 1):
                    coords.append((x, y ,z))
        return coords
    
    def settle(self):
        coords = self.get_coords()
        for c in coords:
            del grid[c] #Remove current brick from grid, so it doesn't block itself
        while not self.settled:
            coords = self.get_coords()
            if self.z1 == 1: #Brick is on the floor, can't settle any more
                self.settled = True
            elif any((x, y, z-1) in grid for x, y, z in coords): #There is a brick below it
                self.settled = True
            else:
                self.z1 -= 1
                self.z2 -= 1
        for c in coords:
            grid[c] = self.ID #Put current brick back into the grid

    def find_below(self): #Find the brick IDs for all bricks the current brick is resting on
        self.below = set()
        coords = self.get_coords()
        z = min(c[2] for c in coords)
        for x, y, _ in coords:
            if (x, y, z-1) in grid:
                self.below.add(grid[(x, y, z-1)])

    def find_above(self): #Find the brick IDs for all bricks being supported by current brick
        self.above = set()
        coords = self.get_coords()
        z = max(c[2] for c in coords)
        for x, y, _ in coords:
            if (x, y, z+1) in grid:
                self.above.add(grid[(x, y, z+1)])
    
    def collapse_above(self): #Remove given brick and cascade through to other supported bricks
        cascade = {self.ID,}
        toCheck = self.above
        while toCheck:
            newCheck = set()
            for brickID in toCheck:
                if all(b in cascade for b in bricks[brickID].below):
                    cascade.add(brickID)
                    for above in bricks[brickID].above:
                        newCheck.add(above)
            toCheck = newCheck
        return len(cascade)-1 #Don't count the brick that started the cascade

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip().split("~") for line in file.readlines()]
    bricks = {}
    for i, line in enumerate(inputs):
        bricks[i] = Brick(i, line)
    return bricks

def get_grid(bricks):
    grid = {}
    for brick in bricks.values():
        coords = brick.get_coords()
        for c in coords:
            grid[c] = brick.ID
    return grid

def part_one():
    ordered = sorted(bricks.values(), key = lambda b: b.z1)
    for brick in ordered: brick.settle() #Settle all the bricks, starting with the lowest ones
    for brick in bricks.values(): brick.find_below()
    supporting = set()
    for brick in bricks.values():
        if len(brick.below) == 1: #Only one support, so will collapse if the support collapses
            supporting.update(brick.below) #Keep a set of bricks that can't be moved
    disintegrate = len(bricks) - len(supporting)
    print(f"Part One = {disintegrate}")

def part_two():
    for brick in bricks.values(): brick.find_above()
    total = sum(brick.collapse_above() for brick in bricks.values())
    print(f"Part Two = {total}")

bricks = open_file(day)
grid = get_grid(bricks)

part_one()
part_two()