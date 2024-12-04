def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global steps
    steps = []
    for line in inputs:
        command, *rest = line.split(" ")
        if "ji" in command:
            reg, val = rest
            reg = reg.strip(",")
            val = eval(val)
            ins = [reg, val]
        elif "j" in command:
            val = eval(*rest)
            ins = [val]
        else:
            reg = rest
            ins = [*reg]
        expr = command + "(*ins)"
        steps.append([expr, *ins])

def initial_registers():
    global registers
    registers = {"a": 0, "b": 0}

def hlf(reg):
    registers[reg] //= 2
    return 1

def tpl(reg):
    registers[reg] *= 3
    return 1

def inc(reg):
    registers[reg] += 1
    return 1

def jmp(val):
    return val

def jie(reg, val):
    if registers[reg] % 2 == 0:
        return val
    else:
        return 1

def jio(reg, val):
    if registers[reg] == 1:
        return val
    else:
        return 1

def run_steps(part):
    if part == 2:
        registers["a"] = 1
    point = 0
    lensteps = len(steps)
    while point < lensteps:
        step = steps[point]
        expr, *ins = step
        point += eval(expr)
    if part == 1:
        print(f"Part One: {registers['b']}")
    else:
        print(f"Part Two: {registers['b']}")

day = 23
open_file()

format_data()

part = 1
initial_registers()
run_steps(part)

part = 2
initial_registers()
run_steps(part)