from itertools import permutations

def open_file():
    #file = open("test.txt")
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().strip()
    file.close()
    return inputs

def formatdata(inputs):
    global code
    code = [int(i) for i in inputs.split(",")]

def halt_case(pointer, amp):
    #print("Halt amplifier", amp)
    pointer += 1
    return pointer

def add_case(newcode, pointer):
    c = newcode[pointer:pointer+4]
    ocstr = str(c[0]).zfill(4)
    params = [int(ocstr[-3]), int(ocstr[-4])]
    add = 0
    for i, p in enumerate(params):
        if p == 0:
            add += newcode[c[i+1]]
        elif p ==1:
            add += c[i+1]
    newcode[c[3]] = add
    pointer += 4
    return newcode, pointer

def multiply_case(newcode, pointer):
    c = newcode[pointer:pointer+4]
    ocstr = str(c[0]).zfill(4)
    params = [int(ocstr[-3]), int(ocstr[-4])]
    mult = 1
    for i, p in enumerate(params):
        if p == 0:
            mult *= newcode[c[i+1]]
        elif p ==1:
            mult *= c[i+1]
    newcode[c[3]] = mult
    pointer += 4
    return newcode, pointer

def input_case_auto(newcode, pointer, setting):
    c = newcode[pointer:pointer+2]
    userin = setting
    newcode[c[1]] = userin
    pointer += 2
    return newcode, pointer

def input_case(newcode, pointer, val, amp):
    c = newcode[pointer:pointer+2]
    #print(f"Input for amplifier {amp} = {val}")
    userin = val
    newcode[c[1]] = userin
    pointer += 2
    return newcode, pointer

def output_case(newcode, pointer):
    c = newcode[pointer:pointer+2]
    ocstr = str(c[0]).zfill(3)
    param = int(ocstr[-3])
    if param == 0:
        out = newcode[c[1]]
    elif param == 1:
        out = c[1]
    pointer += 2
    return newcode, pointer, out

def jump_true(newcode, pointer):
    c = newcode[pointer:pointer+3]
    ocstr = str(c[0]).zfill(4)
    params = [int(ocstr[-3]), int(ocstr[-4])]
    if params[0] == 0:
        check = newcode[c[1]]
    elif params[0] == 1:
        check = c[1]
    if check != 0:
        if params[1] == 0:
            pointer = newcode[c[2]]
        elif params[1] == 1:
            pointer = c[2]
    else:
        pointer += 3
    return newcode, pointer

def jump_false(newcode, pointer):
    c = newcode[pointer:pointer+3]
    ocstr = str(c[0]).zfill(4)
    params = [int(ocstr[-3]), int(ocstr[-4])]
    if params[0] == 0:
        check = newcode[c[1]]
    elif params[0] == 1:
        check = c[1]
    if check == 0:
        if params[1] == 0:
            pointer = newcode[c[2]]
        elif params[1] == 1:
            pointer = c[2]
    else:
        pointer += 3
    return newcode, pointer

def less_than(newcode, pointer):
    c = newcode[pointer:pointer+4]
    ocstr = str(c[0]).zfill(4)
    params = [int(ocstr[-3]), int(ocstr[-4])]
    vals = []
    for i, p in enumerate(params):
        if p == 0:
            vals.append(newcode[c[i+1]])
        elif p ==1:
            vals.append(c[i+1])
    if vals[0] < vals[1]:
        newcode[c[3]] = 1
    else:
        newcode[c[3]] = 0
    pointer += 4
    return newcode, pointer

def equals(newcode, pointer):
    c = newcode[pointer:pointer+4]
    ocstr = str(c[0]).zfill(4)
    params = [int(ocstr[-3]), int(ocstr[-4])]
    vals = []
    for i, p in enumerate(params):
        if p == 0:
            vals.append(newcode[c[i+1]])
        elif p ==1:
            vals.append(c[i+1])
    if vals[0] == vals[1]:
        newcode[c[3]] = 1
    else:
        newcode[c[3]] = 0
    pointer += 4
    return newcode, pointer

def intcode(codes, setlist, amplist, points, count, val):
    idx = count % 5
    setting = setlist[idx]
    amp = amplist[idx]
    ampcode = codes[idx]
    newcode = list(ampcode)
    pointer = points[idx]
    lencode = len(code)
    out = 0
    if count < 5:
        count2 = 0
    else:
        count2 = 1
    while pointer < lencode:
        ocstr = str(newcode[pointer]).zfill(2)
        opcode = ocstr[-2:]
        if opcode == "99":
            halt_case(pointer, amp)
            return val
        elif opcode == "01":
            newcode, pointer = add_case(newcode, pointer)
        elif opcode == "02":
            newcode, pointer = multiply_case(newcode, pointer)
        elif opcode == "03":
            if count2 == 0:
                #print("Setting for amp ", amp, "=", setting)
                newcode, pointer = input_case_auto(newcode, pointer, setting)
                count2 += 1
            else:
                newcode, pointer = input_case(newcode, pointer, val, amp)
        elif opcode == "04":
            newcode, pointer, out = output_case(newcode, pointer)
            #print("Output of amplifier ", amp, "=", out)
            val = out
            points[idx] = pointer
            codes[idx] = newcode
            count += 1
            out = intcode(codes, setlist, amplist, points, count, val)
            return out
        elif opcode == "05":
            #print("Pointer before jump =", pointer)
            newcode, pointer = jump_true(newcode, pointer)
            #print("Pointer after jump =", pointer)
        elif opcode == "06":
            newcode, pointer = jump_false(newcode, pointer)
        elif opcode == "07":
            newcode, pointer = less_than(newcode, pointer)
        elif opcode == "08":
            newcode, pointer = equals(newcode, pointer)
    print("Code didn't end properly")
    return out

def run_settings(settings):
    outputs = []
    amplist = ["A", "B", "C", "D", "E"]
    count = 0
    for setlist in settings:
        codes = [code, code, code, code, code]
        points = [0, 0 ,0, 0, 0]
        out = intcode(codes, setlist, amplist, points, count, 0)
        outputs.append(out)
    maxout = max(outputs)
    return maxout

def perms():
    sets = [5, 6, 7, 8, 9]
    settings = list(permutations(sets))
    return settings
    
        
    
day = 7
inputs = open_file()

formatdata(inputs)

settings = perms()

print(run_settings(settings))