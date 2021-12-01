class Virus:
    def __init__(self, pos):
        self.pos = pos
        self.directs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        #all possible directions
        self.didx = 0 #index for current direction
        self.direction = self.directs[self.didx]
        self.count = 0

    def turn(self):
        if self.pos in infected:
            self.didx = (self.didx + 1) % len(self.directs)
        else:
            self.didx = (self.didx - 1) % len(self.directs)
        self.direction = self.directs[self.didx]
    
    def infect(self):
        if self.pos in infected:
            infected.remove(self.pos)
        else:
            infected.add(self.pos)
            self.count += 1
    
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
    for _ in range(10_000):
        virus.burst()
    print("Part One:", virus.count)

day = 22
open_file()

format_data()

run_iterations()