def open_file(day):
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global instructs
    instructs = []
    for line in inputs:
        sep = line.strip().split(" ")
        sep[1] = int(sep[1])
        instructs.append(sep)

def changeoneline(numlines):
    linesleft = numlines
    pointer = 0
    pos = [pointer]
    acc = 0
    flag = 0
    endProgram = bool(0)
    while flag == 0:
        op = instructs[pointer][0]
        arg = instructs[pointer][1]
        
        if op == "jmp" and linesleft == 1:
            op = "nop"
            linesleft -= 1
        elif op == "nop" and linesleft == 1:
            op = "jmp"
            linesleft -= 1
        
        if op == "acc":
            acc += arg
            pointer += 1
        elif op == "jmp":
            pointer += arg
            linesleft -= 1
        elif op == "nop":
            pointer += 1
            linesleft -= 1
        else:
            flag = 1
            print("Format wrong")
        if pointer in pos:
            flag = 1
        else:
            pos.append(pointer)
            if pointer >= len(instructs):
                flag = 1
                endProgram = bool(1)
    if endProgram:
        return acc
    else:
        numlines += 1
        acc = changeoneline(numlines)
        return acc

day = 8
inputs = open_file(day)

formatdata(inputs)

numlines = 1
acc = changeoneline(numlines)

print(acc)
