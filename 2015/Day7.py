def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global steps
    steps = []
    for line in inputs:
        line = line.split(" ")
        if len(line) == 5:
            x, command, y, _, z = line
            xyz = [x, y, z]
            expr = command + "(*xyz)"
        elif len(line) == 4:
            command, x, _, z = line
            xyz = [x, z]
            expr = command + "(*xyz)"
        else:
            x, _, z = line
            xyz = [x, z]
            expr = "SET(*xyz)"
        steps.append((expr, *xyz))

def AND(x, y, z):
    try:
        valx = int(x)
    except:
        if x in wires:
            valx = wires[x]
        else:
            return False
    try:
        valy = int(y)
    except:
        if y in wires:
            valy = wires[y]
        else:
            return False
    val = valx & valy
    wires[z] = val
    return True

def OR(x, y, z):
    try:
        valx = int(x)
    except:
        if x in wires:
            valx = wires[x]
        else:
            return False
    try:
        valy = int(y)
    except:
        if y in wires:
            valy = wires[y]
        else:
            return False
    val = valx | valy
    wires[z] = val
    return True

def RSHIFT(x, y, z):
    try:
        valx = int(x)
    except:
        if x in wires:
            valx = wires[x]
        else:
            return False
    valy = int(y)
    val = valx >> valy
    wires[z] = val
    return True

def LSHIFT(x, y, z):
    try:
        valx = int(x)
    except:
        if x in wires:
            valx = wires[x]
        else:
            return False
    valy = int(y)
    val = valx << valy
    wires[z] = val
    return True

def NOT(x, z):
    try:
        valx = int(x)
    except:
        if x in wires:
            valx = wires[x]
        else:
            return False
    val = ~valx + 2**16
    wires[z] = val
    return True

def SET(x, z):
    if z == "b" and part == 2:
        return True
    try:
        valx = int(x)
    except:
        if x in wires:
            valx = wires[x]
        else:
            return False
    wires[z] = valx
    return True

def set_up_kit():
    format_data()
    global wires, part
    wires = {}
    instructions = list(steps)
    part = 1
    while instructions:
        for step in instructions:
            expr, *xyz = step
            check = eval(expr)
            if check:
                steps.remove(step)
        instructions = list(steps)
    print(f"Part One: {wires['a']}")
    format_data()
    wires = {"b": wires["a"]}
    instructions = list(steps)
    part = 2
    while instructions:
        for step in instructions:
            expr, *xyz = step
            check = eval(expr)
            if check:
                steps.remove(step)
        instructions = list(steps)
    print(f"Part Two: {wires['a']}")

day = 7
open_file()

set_up_kit()