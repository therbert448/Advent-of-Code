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
            y = int(step[2])
            xy = [x, y]
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
    if val != 0:
        return y
    else:
        return 1

def run():
    global point
    point = 0
    steplen = len(steps)
    while 0 <= point < steplen:
        step = steps[point]
        expr, *xy = step
        point += eval(expr)    

def fibonacci(n):
    a, b = [1, 1]
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return c

def part_one():
    initial_regs()
    run()
    print(f"Part One: {registers['a']}")

def part_two():
    #When c is set to 1, the code finds the fibonacci sequence, starting with
    #2 and then the 32 numbers after.
    #We then add 11 * 18 to the final number
    value = fibonacci(33)
    value += 11 * 18
    print(f"Part Two: {value}")

day = 12
open_file()

format_data()

part_one()
part_two()