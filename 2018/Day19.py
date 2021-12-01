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

def sum_factors(value):
    sqrt = int(value ** 0.5)
    factset = set()
    for i in range(1, sqrt+1):
        if value % i == 0:
            factset.add(i)
            f = value // i
            factset.add(f)
    return(sum(factset))

def run_code(a):
    global reg
    reg = [a, 0, 0, 0, 0, 0]
    point = reg[ip]
    codelen = len(steps)
    while point < codelen:
        reg[ip] = point
        step = steps[point]
        code = step[0]
        expr = code + "(reg, step)"
        newreg = eval(expr)
        """
        USE THIS TO SEE WHAT THE CODE IS DOING
        if newreg[0] != reg[0] and a == 0:
            print(point, step, reg, newreg)
            #Print when the value at register 0 changes
            #Doing this for part one shows that the result at reg[0] is the
            #sum of the factors of the value at reg[2]
            #When reg[0] starts with a value of 1, this value will be very
            #large, and so the code will take forever
        """
        if newreg[0] != reg[0]:
            value = newreg[2]
            break
            #Find the value at reg[2] when it's settled
            #Will be quicker to write my own function to find these factors
        reg = newreg
        point = reg[ip] + 1
    result = sum_factors(value)
    if a == 0:
        print("Part One:")
        print("Sum of factors of", value, "=", result)
    else:
        print("Part Two:")
        print("Sum of factors of", value, "=", result)

day = 19
inputs = open_file()

formatdata(inputs)

run_code(0) #Part one
run_code(1) #Part two