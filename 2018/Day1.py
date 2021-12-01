def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global expression, steps
    expression = "x" + "".join([line.strip() for line in inputs])
    steps = [line.strip() for line in inputs]

def part_one():
    x = 0
    print("Part One:", eval(expression))

def part_two():
    f = 0
    freqset = {f}
    found = 0
    while not found:
        for step in steps:
            express = "f" + step
            f = eval(express)
            if f in freqset:
                print("Part Two:", f)
                found = 1
                break
            else:
                freqset.add(f)

day = 1
inputs = open_file()

formatdata(inputs)

part_one()
part_two()
