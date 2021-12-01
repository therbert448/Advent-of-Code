class Program:
    def __init__(self, name, num):
        self.name = name
        self.num = num   

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global programs, subprograms
    programs = {}
    subprograms = {}
    for line in inputs:
        above = []
        if "->" not in line:
            name, num = line.split(" ")
            num = int(num.strip("()"))
        else:
            line, above = line.split(" -> ")
            name, num = line.split(" ")
            num = int(num.strip("()"))
            above = above.split(", ")
            for a in above:
                subprograms[a] = name
        program = Program(name, num)
        programs[name] = program
        program.above = list(above)

def find_bottom():
    allps = set(programs.keys())
    subps = set(subprograms.keys())
    bottom = allps.symmetric_difference(subps)
    global name
    for name in bottom:
        print("Part One:", name)

def weigh_stacks(name):
    above = programs[name].above
    weights = []
    towerweights = {}
    lenabove = len(above)
    for a in above:
        weight = programs[a].num
        if programs[a].above:
            extraweight = weigh_stacks(a)
            if extraweight == -1:
                return -1
            towerweights[a] = extraweight
            weight += extraweight
        weights.append(weight)
    for i, w in enumerate(weights):
        count = weights.count(w)
        if count == lenabove:
            return sum(weights)
        elif count == 1:
            avweight = weights[(i+1) % lenabove]
            name = above[i]
            needweight = avweight - towerweights[name]
            print("Part Two:", needweight)
            return -1

def part_two():
    weigh_stacks(name)

day = 7
open_file()

format_data()

find_bottom()
part_two()