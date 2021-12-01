def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global registers, steps
    registers = {}
    steps = []
    for line in inputs:
        step = line.split(" ")
        command = step[0]
        reg = step[1]
        try:
            reg = int(reg)
        except:
            if reg not in registers:
                registers[reg] = 0
        if command in ("snd", "rcv"):
            expr = command + "x(*reg)"
            reg = [reg]
        else:
            potreg = step[2] #second value is a potential register
            try:
                potreg = int(potreg)
            except:
                if potreg not in registers:
                    registers[potreg] = 0
            reg = [reg, potreg]
            expr = command + "x(*reg)"
        steps.append([expr, *reg])

def setx(reg, potreg):
    if isinstance(potreg, int):
        registers[reg] = potreg
    else:
        registers[reg] = registers[potreg]

def addx(reg, potreg):
    if isinstance(potreg, int):
        registers[reg] += potreg
    else:
        registers[reg] += registers[potreg]

def mulx(reg, potreg):
    if isinstance(potreg, int):
        registers[reg] *= potreg
    else:
        registers[reg] *= registers[potreg]
        
def modx(reg, potreg):
    if isinstance(potreg, int):
        registers[reg] %= potreg
    else:
        registers[reg] %= registers[potreg]

def jgzx(reg, potreg):
    if isinstance(reg, int):
        if reg <= 0:
            return 1
        else:
            if isinstance(potreg, int):
                jump = potreg
            else:
                jump = registers[potreg]
            return jump
    elif registers[reg] <= 0:
        return 1
    if isinstance(potreg, int):
        jump = potreg
    else:
        jump = registers[potreg]
    return jump

def sndx(reg):
    return registers[reg]

def rcvx(reg):
    if registers[reg] == 0:
        return None
    else:
        return lastsound

def run_duet():
    global lastsound
    lastsound = None
    numsteps = len(steps)
    point = 0
    while 0 <= point < numsteps:
        step = steps[point]
        expr = step[0]
        reg = step[1:]
        if "snd" in expr:
            lastsound = eval(expr)
        elif "jgz" in expr:
            point += eval(expr)
            continue
        elif "rcv" in expr:
            recover = eval(expr)
            if recover != None:
                print("Part One:", recover)
                break
        else:
            eval(expr)
        point += 1

day = 18
open_file()

format_data()

run_duet()