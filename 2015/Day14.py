class Reindeer:
    def __init__(self, name, speed, last, rest):
        self.name = name
        self.speed = speed
        self.last = last
        self.rest = rest
        self.score = 0
        self.calculate_distance()
    
    def calculate_distance(self):
        self.period = self.last + self.rest
        self.intdist = self.speed * self.last
        numrests = seconds // self.period
        left = seconds % self.period
        if left > self.last:
            extra = self.intdist
        else:
            extra = left * self.speed
        self.distance = self.intdist * numrests + extra
    
    def current_distance(self, sec):
        numrests = sec // self.period
        left = sec % self.period
        if left > self.last:
            extra = self.intdist
        else:
            extra = left * self.speed
        self.currdist = self.intdist * numrests + extra

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global deers
    deers = []
    for line in inputs:
        name, *rest = line.split(" ")
        speed, *rest = rest[2:]
        last, *rest = rest[2:]
        rest = int(rest[6])
        speed, last = [int(speed), int(last)]
        deer = Reindeer(name, speed, last, rest)
        deers.append(deer)

def part_one():
    maxkey = lambda x: x.distance
    bestdeer = max(deers, key=maxkey)
    maxdist = bestdeer.distance
    print(f"Part One: {maxdist}")

def part_two():
    for i in range(seconds):
        sec = i + 1
        leading = []
        bestdist = 0
        for idx, deer in enumerate(deers):
            deer.current_distance(sec)
            if deer.currdist > bestdist:
                bestdist = deer.currdist
                leading = [idx]
            elif deer.currdist == bestdist:
                leading.append(idx)
        for idx in leading:
            deers[idx].score += 1
    maxscore = lambda x: x.score
    bestdeer = max(deers, key=maxscore)
    maxscore = bestdeer.score
    print(f"Part Two: {maxscore}")

day = 14
open_file()

seconds = 2503

format_data()

part_one()
part_two()