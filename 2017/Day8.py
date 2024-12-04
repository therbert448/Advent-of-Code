def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global registers, maxval
    registers = {}
    maxval = 0
    for line in inputs:
        jump, cond = line.split(" if ")
        jump = jump.replace("inc", "+").replace("dec", "-")
        rega, *jump = jump.split(" ")
        jump = " ".join(jump)
        jumpexpr = "registers[rega] " + jump
        regb, *cond = cond.split(" ")
        cond = " ".join(cond)
        condexpr = "registers[regb] " + cond
        if rega not in registers:
            registers[rega] = 0
        if regb not in registers:
            registers[regb] = 0
        if eval(condexpr):
            registers[rega] = eval(jumpexpr)
        if registers[rega] > maxval:
            maxval = registers[rega]
    print("Part One:", max(registers.values()))
    print("Part Two:", maxval)
    
day = 8
open_file()

format_data()