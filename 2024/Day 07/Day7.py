"""
Advent of Code
2024 Day 07

@author: Tom Herbert
"""
from time import time

day = 7

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    equations = []
    for line in inputs:
        result, values = line.strip().split(": ")
        values = [int(v) for v in values.split()]
        equations.append((int(result), values))
    return equations

def check_operators(equations, partTwo=False):
    newEquations = []
    for line in equations:
        result, vals, current = line
        val = vals.pop(-1)
        if not vals and val == current:
            return result
        elif not vals: continue
        if current - val >= 0:
            newCurrent = current - val
            newEquations.append([result, [v for v in vals], newCurrent])
        if not current % val:
            newCurrent = current//val
            newEquations.append([result, [v for v in vals], newCurrent])
        if partTwo:
            strCurr, strVal = str(current), str(val)
            if strCurr[-len(strVal):] == strVal:
                strCurr = strCurr[:-len(strVal)]
                if not strCurr: continue
                newEquations.append([result, [v for v in vals], int(strCurr)])
    if newEquations:
        return check_operators(newEquations, partTwo)
    return 0

equations = open_file(day)

t0 = time()
total = 0
for equation in equations:
    equation = [[equation[0], [v for v in equation[1]], equation[0]]]
    total += check_operators(equation)
print(f"Part One = {total}")
t1 = time()
print(f"took {round(t1-t0, 6)}s\n")

total = 0
for equation in equations:
    equation = [[equation[0], [v for v in equation[1]], equation[0]]]
    total += check_operators(equation, True)
print(f"Part Two = {total}")
t2 = time()
print(f"took {round(t2-t1, 6)}s")