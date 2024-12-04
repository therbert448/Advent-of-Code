def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [line.strip() for line in file.readlines()]
    file.close()
    return inputs

def formatdata(inputs):
    global steps, ip
    steps = []
    ipline = inputs.pop(0).split(" ")
    ip = int(ipline[1])
    for line in inputs:
        step = [i for i in line.split(" ")]
        for i, val in enumerate(step):
            try:
                step[i] = int(val)
            except ValueError:
                pass
        steps.append(step)
        
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

def run_code(a):
    global reg
    reg = [a, 0, 0, 0, 0, 0]
    point = reg[ip]
    codelen = len(steps)
    #avals = set()
    while point < codelen:
        reg[ip] = point
        step = steps[point]
        code = step[0]
        expr = code + "(reg, step)"
        newreg = eval(expr)
        if point == 28:
            a = reg[3]
            print("Part One:", a)
            break
            """
            if a not in avals:
                avals.add(reg[3])
                lasta = a
            else:
                #This should work, but it takes forever to repeat a value.
                #Best bet is to figure out how the bori/bani commands work and
                #translate mathematically
                print("Part Two:", lasta)
                break
            """
        reg = newreg
        point = reg[ip] + 1

def part_one():
    a = 0 #7216956
    run_code(a)

def part_two():
    d = 1505483 #first value assigned to reg[3]
    c = 65536 #value at reg[2]
    loop = 0
    global dset
    dset = set()
    # c & 255 = 0, pretty much mod. 65536 % 256 = 0
    #bitwise 256 & 255 = 0. Yes that's it
    #This value is set to position e
    while not loop:
        e = int(c % 256) #for some reason this comes out as a float
        d += e # this is the next step, add result of the & to reg[3]
        #then d & 16777215, quick check shows this is == d % 2**24
        d = d % (2 ** 24)
        #then multiply d by 65899
        d *= 65899
        #then % 2**24 again
        d = d % (2 ** 24)
        #next is the bit that takes the longest time, reg[5] is incremented by
        #255 each loop until it is greater than reg[2]. When this happens c is 
        #divided by 256. The value at reg[3] is then multiplied by 65899 and 
        #moded again
        #After changing reg[3], if reg[2] is less than 256 we then check if 
        #reg[3]is equal to a.
        if c < 256: #Potential exit case
            if d not in dset:
                a = d
                dset.add(d)
            else:
                print("Part Two:", a)
                break
            #now I encounter my first bitwise or, and at the same time realise
            #I could have just used these operations instead of trying to
            #figure out what they mean in effect.
            c = d | 65536
            d = 1505483
            continue
        c = c/256      

day = 21
inputs = open_file()

formatdata(inputs)

part_one()
part_two()