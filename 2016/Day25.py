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

def out(x):
    global flag, end
    try:
        val = int(x)
    except:
        val = registers[x]
    if val != 0 and val != 1:
        print(f"Not {a}")
        flag = 1
        return 1
    elif len(outs) > 10:
        print(f"Day 25: {a}")
        flag = 1
        end = 1
        return 1
    elif outs:
        if outs[-1] != val:
            outs.append(val)
        else:
            print(f"Not {a}")
            flag = 1
            return 1
    else:
        if val == 1:
            print(f"Not {a}")
            flag = 1
            return 1
        else:
            outs.append(val)
    return 1

def run():
    global steplen, flag, end, a, outs
    end = 0
    a = 0
    while not end:
        initial_regs()
        registers["a"] = a
        point = 0
        flag = 0
        outs = []
        steplen = len(steps)
        while 0 <= point < steplen and not flag:
            step = steps[point]
            expr, *xy = step
            point += eval(expr)
        a += 1

def christmas():
    run()

day = 25
open_file()

format_data()

christmas()