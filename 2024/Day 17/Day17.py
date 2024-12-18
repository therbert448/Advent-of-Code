"""
Advent of Code
2024 Day 17

@author: Tom Herbert
"""
from time import time

day = 17

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        registers, program = file.read().split("\n\n")
    registers = [int(l.strip().split()[-1]) for l in registers.splitlines()]
    program = [int(v) for v in program.strip().split()[-1].split(",")]
    return registers, program

def combo(operand, registers):
    if operand < 4:
        return operand
    elif operand == 7:
        print("Error")
        quit()
    else:
        return registers[operand-4]

def adv(operand, registers):
    registers[0] = registers[0]//(2**combo(operand, registers))
    return registers

def bxl(operand, registers):
    registers[1] = registers[1] ^ operand
    return registers

def bst(operand, registers):
    registers[1] = combo(operand, registers) % 8
    return registers

def jnz(operand, registers, pointer):
    if registers[0]:
        pointer = operand
    return pointer

def bxc(registers):
    registers[1] = registers[1] ^ registers[2]
    return registers

def out(operand, registers, toPrint):
    toPrint.append(combo(operand, registers) % 8)
    return toPrint

def bdv(operand, registers):
    registers[1] = registers[0]//(2**combo(operand, registers))
    return registers

def cdv(operand, registers):
    registers[2] = registers[0]//(2**combo(operand, registers))
    return registers

def run_instruction(opcode, operand, registers, pointer, toPrint):
    if opcode == 0:
        registers = adv(operand, registers)
    if opcode == 1:
        registers = bxl(operand, registers)
    if opcode == 2:
        registers = bst(operand, registers)
    if opcode == 3:
        pointer = jnz(operand, registers, pointer)
    if opcode == 4:
        registers = bxc(registers)
    if opcode == 5:
        toPrint = out(operand, registers, toPrint)
    if opcode == 6:
        registers = bdv(operand, registers)
    if opcode == 7:
        registers = cdv(operand, registers)
    return registers, pointer, toPrint

def reverse_loop(currentReg, idx, program):
    a, b = currentReg
    if idx == 0:
        for i in range(8):
            newB = i ^ 5
            newA = (a * 8) + i
            newC = newA//(2**newB)
            newB = (newB ^ newC) ^ 6
            if newB % 8 != b:
                continue
            return newA
    goal = program[idx-1]
    for i in range(8):
        newB = i ^ 5
        newA = (a * 8) + i
        newC = newA//(2**newB)
        newB = (newB ^ newC) ^ 6
        if newB % 8 != b:
            continue
        newReg = [newA, goal]
        result = reverse_loop(newReg, idx-1, program)
        if result: return result
    return False

regs, program = open_file(day)

point = 0
toPrint = []
while point < len(program):
    opc, oper = program[point:point+2]
    point += 2
    regs, point, toPrint = run_instruction(opc, oper, regs, point, toPrint)
print("Part One =",",".join([str(v) for v in toPrint]))

idx = len(program) - 1
currentReg = [0, program[-1]]
a = reverse_loop(currentReg, idx, program)
print(f"Part Two = {a}")

regs = [a, 0, 0] 
point = 0
toPrint = []
while point < len(program):
    opc, oper = program[point:point+2]
    point += 2
    regs, point, toPrint = run_instruction(opc, oper, regs, point, toPrint)
print("\nCheck Part Two:")
print(",".join([str(v) for v in toPrint]))
print(",".join([str(v) for v in program]))   