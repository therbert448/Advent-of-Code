def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global steps
    steps = []
    for line in inputs:
        step = line.split(" ")
        command = step[0]
        x = step[1]
        if command == "cpy":
            try:
                x = int(x)
            except:
                pass
            y = step[2]
            xy = [x, y]
        elif command == "jnz":
            try:
                x = int(x)
            except:
                pass
            try:
                y = int(step[2])
            except:
                y = step[2]
            xy = [x, y]
        elif command == "tgl":
            xy = [x]
            expr = command + "(*xy, point)"
            steps.append([expr, *xy])
            continue
        else:
            xy = [x]
        expr = command + "(*xy)"
        steps.append([expr, *xy])

def initial_regs():
    global registers
    registers = {}
    for i in range(4):
        key = chr(97 + i)
        registers[key] = 0

def cpy(x, y):
    if isinstance(y, int):
        return 1
    if isinstance(x, int):
        val = x
    else:
        val = registers[x]
    registers[y] = val
    return 1

def inc(x):
    registers[x] += 1
    return 1

def dec(x):
    registers[x] -= 1
    return 1

def jnz(x, y):
    if isinstance(x, int):
        val = x
    else:
        val = registers[x]
    if isinstance(y, int):
        jump = y
    else:
        jump = registers[y]
    if val != 0:
        return jump
    else:
        return 1

def tgl(x, point):
    val = registers[x] + point
    if val < 0 or val >= steplen:
        return 1
    command = steps[val][0]
    if len(steps[val]) == 3 and "jnz" in command:
        command = "cpy(*xy)"
    elif len(steps[val]) == 3:
        command = "jnz(*xy)"
    elif "inc" in command:
        command = "dec(*xy)"
    elif "tgl" in command:
        return 1
    else:
        command = "inc(*xy)"
    steps[val][0] = command
    return 1

def run():
    global steplen
    point = 0
    steplen = len(steps)
    while 0 <= point < steplen:
        step = steps[point]
        expr, *xy = step
        point += eval(expr) 

def part_one():
    initial_regs()
    registers["a"] = 7
    run()
    print(f"Part One: {registers['a']}") #Part One: 10807
    """
    looking at the code and the answer helps us understand what it is doing
    this will help for part two
    for my input code it takes the initial value of register a (7 for part one)
    finds the factorial of this number (7! = 5040)
    then adds 73 * 79 = 5767
    5040 + 5767 = 10807
    """
    a = 1
    for i in range(7):
        a *= i+1
    a += 73 * 79
    print(f"Part One Simplified: {a}") #Part One Simplified: 10807

def part_two():
    """
    register a is now 12 to start with
    first part of code is setting "a" to 12!
    second part then adds 73 * 79
    """
    a = 1
    for i in range(12):
        a *= i+1
    a += 73 * 79
    print(f"Part Two: {a}") #Part Two: 479007367

day = 23
open_file()

format_data()

part_one()
part_two()