"""
Advent of Code
2022 Day 21

@author: Tom Herbert
"""

day = 21

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip().split(": ") for line in file.readlines()]
    return inputs

def format_data(): #split monkeys into ones that shout and ones that wait
    global yelled, operations
    yelled = {}
    operations = {}
    for line in inputs:
        name, toYell = line[0], line[1].split(" ")
        if len(toYell) == 1:
            yelled[name] = int(toYell[0])
        else:
            if toYell[1] == "/":
                toYell[1] += toYell[1]
            operations[name] = [*toYell]

def yell(name, operation): #if operation can be completed, update shouts
    a, op, b = operation
    if a in human or b in human:
        human.add(name)
        shouts[name] = "x"
        return
    a, b = shouts[a], shouts[b]
    operation = str(a) + op + str(b)
    shouts[name] = eval(operation)

def run_shouting(): #Get all monkeys to shout until root shouts
    opsLeft = {**operations}
    while end not in shouts:
        shoutsLeft = {}
        for name, operation in opsLeft.items():
            a, _, b = operation
            if a in shouts and b in shouts:
                yell(name, operation)
                if name == end:
                    break
            else:
                shoutsLeft[name] = operation
        opsLeft = {**shoutsLeft}

def find_x(monkey, x = None): 
    #Run down from root, reducing the x path down to x
    if monkey == "humn":
        return x
    if x == None: #Starting at root
        a, _, b = operations[monkey]
        if b in human: #find the side dependent on x
            x = shouts[a] #the side that resolves becomes equivalent to x path
            down = b      #this is the x path
        else:
            x = shouts[b]
            down = a
    else:
        a, op, b = operations[monkey]
        if b in human: #find the side dependent on x
            y = shouts[a] #the side that resolves becomes equivalent to x path
            down = b      #this is the x path
            if op == "//": #x path is denominator
                x = y//x #rearrange equation
            elif op == "-": #x path is being subtracted from a
                x = y - x #rearrange the equation
        else:
            y = shouts[b]
            down = a
            if op == "//": #x path is numerator
                x *= y #just multiply
            elif op == "-": #x path is having b subtracted from it 
                x += y #just add
        if op == "+": #order doesn't matter
            x -= y
        elif op == "*": #order doesn't matter
            x = x//y
    x = find_x(down, x)
    return x

def part_one():
    global shouts
    shouts = {**yelled}
    run_shouting()
    print(f"Part One = {shouts[end]}")

def part_two():
    global shouts
    shouts = {**yelled}
    shouts["humn"] = "x"
    human.add("humn")
    run_shouting()
    x = find_x(end)
    print(f"Part Two = {x}")

inputs = open_file()

format_data()

end = "root"
human = set()

part_one()
part_two()