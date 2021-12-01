def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().strip()
    file.close()
    return inputs

def formatdata(inputs):
    global code
    code = [int(i) for i in inputs.split(",")]
    
def run_1202(a, b):
    newcode = list(code)
    newcode[1] = a
    newcode[2] = b
    codelen = 4
    length = len(newcode)
    opcodes = length//codelen
    for i in range(opcodes):
        startpos = i * codelen
        c = newcode[startpos:startpos + codelen]
        if c[0] == 99:
            return newcode[0]
        elif c[0] == 1:
            newcode[c[3]] = newcode[c[1]] + newcode[c[2]]
        elif c[0] == 2:
            newcode[c[3]] = newcode[c[1]] * newcode[c[2]]
        else:
            print("Code didn't end properly")
            return -1

def part_two():
    for i in range(100):
        for j in range(100):
            output = run_1202(i, j)
            if output == -1:
                print("Can't finish part two")
                return -1
            elif output == 19690720:
                return i * 100 + j

day = 2
inputs = open_file()

formatdata(inputs)
print(run_1202(12, 2))
print(part_two())