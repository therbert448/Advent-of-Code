"""
Only for Part Two.
The changes to the definition of the puzzle made it necessary to have two
solutions.
(Hard to tell the virus to ignore the weakened/flagged requirements for part
 one, without a bunch of conditional if part == 1)
"""

class Virus:
    def __init__(self, pos):
        self.pos = pos
        self.directs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        #all possible directions
        self.didx = 0 #index for current direction
        self.direction = self.directs[self.didx]
        self.count = 0
        self.weakened = set()
        self.flagged = set()

    def turn(self):
        if self.pos in infected:
            self.didx = (self.didx + 1) % len(self.directs)
        elif self.pos in self.flagged:
            self.didx = (self.didx + 2) % len(self.directs)
        elif self.pos not in self.weakened:
            self.didx = (self.didx - 1) % len(self.directs)
        self.direction = self.directs[self.didx]
    
    def infect(self):
        if self.pos in infected:
            infected.remove(self.pos)
            self.flagged.add(self.pos)
        elif self.pos in self.flagged:
            self.flagged.remove(self.pos)
        elif self.pos in self.weakened:
            self.weakened.remove(self.pos)
            infected.add(self.pos)
            self.count += 1
        else:
            self.weakened.add(self.pos)
    
    def move(self):
        f = lambda a,b: a + b
        self.pos = tuple(map(f, self.pos, self.direction))
    
    def burst(self):
        self.turn()
        self.infect()
        self.move()

def open_file():
    #file = open("test.txt")
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global infected, virus
    infected = set()
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char == "#":
                pos = (x, y)
                infected.add(pos)
    middle = (x//2, y//2)
    virus = Virus(middle)

def run_iterations():
    for _ in range(10_000_000):
        virus.burst()
    print("Part Two:", virus.count)

day = 22
open_file()

format_data()

run_iterations()
#not particularly fast, but spits out the solution