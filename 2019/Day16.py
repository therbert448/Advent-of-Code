import math as maths

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().strip()
    file.close()
    return inputs

def formatdata(inputs):
    global elements
    elements = [int(i) for i in inputs]

def pattern_matrix():
    base = [0, 1, 0, -1]
    matrix = []
    for i in range(len(elements)):
        row = []
        for j in range(len(elements)+1):
            count = maths.ceil((j+1)/(i+1)) - 1
            row.append(base[count % 4])
        del row[0]
        matrix.append(row)
    return matrix

def mat_mult(els, mat):
    newels = []
    for i in range(len(els)):
        sumels = 0
        for j in range(len(els)):
            if j < i:
                continue
            mult = els[j] * mat[i][j]
            sumels += mult
        newels.append(abs(sumels) % 10)
    return newels

def sum_els(els):
    newels = []
    total = 0
    for i in range(len(els)):
        total += els[-(i+1)]
        newels.append(abs(total) % 10)
    newels = newels[::-1]
    return newels

def part_one():
    els = list(elements)
    mat = pattern_matrix()
    for i in range(100):
        els = mat_mult(els, mat)
    string = ""
    for i in range(8):
        string += str(els[i])
    print(string)
        
def part_two():
    offset = int(inputs[0:7])
    els = list(elements) * 10_000
    els = els[offset:]
    for i in range(100):
        print(i)
        els = sum_els(els)
    els = [str(i) for i in els[0:8]]
    print("".join(els))

day = 16
inputs = open_file()

formatdata(inputs)

part_two()