def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().split("\n\n\n\n")
    file.close()
    return inputs

def formatdata(inputs):
    global steps
    steps = []
    commands = inputs[0].split("\n\n")
    for com in commands:
        com = [c.strip("]\n") for c in com.splitlines()]
        command = com[1]
        command = [int(c) for c in command.split(" ")]
        inreg = com[0].split("[")
        inreg = [int(i) for i in inreg[1].split(", ")]
        outreg = com[2].split("[")
        outreg = [int(o) for o in outreg[1].split(", ")]
        steps.append([command, inreg, outreg])
    comms = [i.strip() for i in inputs[1].splitlines()]
    global codes
    codes = []
    for c in comms:
        com = [int(cm) for cm in c.split(" ")]
        codes.append(com)

def addr(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = result[B]
    add = a + b
    result[C] = add
    return result

def addi(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = B
    add = a + b
    result[C] = add
    return result

def mulr(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = result[B]
    mul = a * b
    result[C] = mul
    return result

def muli(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = B
    mul = a * b
    result[C] = mul
    return result

def banr(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = result[B]
    ban = a & b
    result[C] = ban
    return result

def bani(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = B
    ban = a & b
    result[C] = ban
    return result

def borr(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = result[B]
    ban = a | b
    result[C] = ban
    return result

def bori(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = B
    ban = a | b
    result[C] = ban
    return result

def setr(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    result[C] = a
    return result

def seti(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = A
    #print(C)
    result[C] = a
    return result

def gtir(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = A
    b = result[B]
    if a > b:
        result[C] = 1
    else:
        result[C] = 0
    return result

def gtri(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = B
    if a > b:
        result[C] = 1
    else:
        result[C] = 0
    return result

def gtrr(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = result[B]
    if a > b:
        result[C] = 1
    else:
        result[C] = 0
    return result

def eqir(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = A
    b = result[B]
    if a == b:
        result[C] = 1
    else:
        result[C] = 0
    return result

def eqri(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = B
    if a == b:
        result[C] = 1
    else:
        result[C] = 0
    return result

def eqrr(reg, command):
    result = list(reg)
    _, A, B, C = command
    a = result[A]
    b = result[B]
    if a == b:
        result[C] = 1
    else:
        result[C] = 0
    return result

def find_opcodes():
    count = 0
    for step in steps:
        command = list(step[0])
        op = command[0]
        inreg = list(step[1])
        outreg = list(step[2])
        poscodes = []
        for code in opcodes[op]:
            expr = code + "(inreg, command)"
            newout = eval(expr)
            if tuple(newout) == tuple(outreg):
                poscodes.append(code)
        if len(poscodes) >= 3:
            count +=1
        if not poscodes:
            print("Run out of options?")
        else:
            opcodes[op] = list(poscodes)
    print("Part One:", count)

def count_nums(opcodes):
    opnums = list(opcodes.keys())
    numcount = []
    for o in opnums:
        numcount.append(len(opcodes[o]))
    return numcount

def count_codes(opcodes):
    codecount = []
    for code in oplist:
        count = 0
        for x in opcodes.values():
            if code in x:
                count += 1
        codecount.append(count)
    return codecount

def match_opcodes():
    numcount = count_nums(opcodes)
    codecount = count_codes(opcodes)
    correctpairs = {}
    while not all([c == 0 for c in codecount]):
        if 1 in numcount:
            nums = list(opcodes.keys())
            idx = numcount.index(1)
            number = nums[idx]
            code = opcodes[number][0]
            correctpairs[number] = code
            del opcodes[number]
            for num in opcodes:
                if code in opcodes[num]:
                    opcodes[num].remove(code)
        elif 1 in codecount:
            idx = codecount.index(1)
            code = oplist[idx]
            for num in opcodes:
                if code in opcodes[num]:
                    number = num
            correctpairs[number] = code
            del opcodes[number]
        else:
            break
        numcount = count_nums(opcodes)
        codecount = count_codes(opcodes)
    return correctpairs

def part_one():
    find_opcodes()

def part_two():
    correctpairs = match_opcodes()
    register = [0, 0, 0, 0]
    for c in codes:
        opcode = c[0]
        code = correctpairs[opcode]
        expr = code + "(register, c)"
        register = eval(expr)
    print("Part Two:", register[0])
        

day = 16
inputs = open_file()

oplist = ["addr", "addi", "mulr", "muli",
           "banr", "bani", "borr", "bori", 
           "setr", "seti", "gtir", "gtri",
           "gtrr", "eqir", "eqri", "eqrr"]

opcodes = {}
for i in range(16):
    opcodes[i] = [op for op in oplist]

formatdata(inputs)

part_one()
part_two()