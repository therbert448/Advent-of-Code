class Program:
    def __init__(self, register):
        self.register = register
        self.point = 0
        self.invals = []
        self.waiting = 0
        self.count = 0
        self.out = 0
    
    def add(self, reg, potreg):
        if isinstance(potreg, int):
            self.register[reg] += potreg
        else:
            self.register[reg] += self.register[potreg]
        self.point += 1
    
    def mul(self, reg, potreg):
        if isinstance(potreg, int):
            self.register[reg] *= potreg
        else:
            self.register[reg] *= self.register[potreg]
        self.point += 1
    
    def mod(self, reg, potreg):
        if isinstance(potreg, int):
            self.register[reg] %= potreg
        else:
            self.register[reg] %= self.register[potreg]
        self.point += 1
    
    def jgz(self, reg, potreg):
        if isinstance(potreg, int):
            jump = potreg
        else:
            jump = self.register[potreg]
        if isinstance(reg, int) and reg > 0:
            self.point += jump
        elif self.register[reg] > 0:
            self.point += jump
        else:
            self.point += 1

    def setx(self, reg, potreg):
        if isinstance(potreg, int):
            self.register[reg] = potreg
        else:
            self.register[reg] = self.register[potreg]
        self.point += 1

    def snd(self, reg, other):
        if isinstance(reg, int):
            val = reg
        else:
            val = self.register[reg]
        #print(val)
        other.invals.append(val)
        self.count += 1
        self.point += 1
    
    def rcv(self, reg):
        if self.invals:
            self.register[reg] = self.invals.pop(0)
            self.point += 1
        else:
            self.waiting = 1

def open_file():
    #file = open("test.txt")
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global steps, programs
    register = {}
    steps = []
    for line in inputs:
        step = line.split(" ")
        command = step[0]
        reg = step[1]
        try:
            reg = int(reg)
        except:
            if reg not in register:
                register[reg] = 0
        if command in ("snd", "rcv"):
            reg = [reg]
        else:
            potreg = step[2] #second value is a potential register
            try:
                potreg = int(potreg)
            except:
                if potreg not in register:
                    register[potreg] = 0
            reg = [reg, potreg]
        steps.append([command, *reg])
    programs = {}
    for i in range(2):
        programs[i] = Program(dict(register))
    programs[1].register["p"] = 1

def run_duet():
    stepnum = len(steps)
    while True:
        for i, program in programs.items():
            if program.waiting and program.invals:
                program.waiting == 0
            elif program.waiting:
                continue
            if program.point < 0 or program.point >= stepnum:
                program.out = 1
                continue
            step = steps[program.point]
            command = step[0]
            reg = step[1:]
            if command == "add":
                program.add(*reg)
            elif command == "mul":
                program.mul(*reg)
            elif command == "mod":
                program.mod(*reg)
            elif command == "jgz":
                program.jgz(*reg)
            elif command == "set":
                program.setx(*reg)
            elif command == "snd":
                other = programs[(i+1)%2]
                program.snd(*reg, other)
            elif command == "rcv":
                program.rcv(*reg)
        if programs[0].waiting and programs[1].waiting:
            break
        if programs[0].out and programs[1].out:
            break
    print("Part Two:", programs[1].count)
        

day = 18
open_file()

format_data()

run_duet()