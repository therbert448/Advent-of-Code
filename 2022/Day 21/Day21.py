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

def yell(name, operation): #if operation can be completed, update shouted
    a, op, b = operation
    a, b = shouted[a], shouted[b]
    operation = str(a) + op + str(b)
    shouted[name] = eval(operation)

def run_shouting(): #Get all monkeys to shout until root shouts
    opsLeft = {k: v for k, v in operations.items()}
    while end not in shouted:
        newOpsLeft = {}
        for name, operation in opsLeft.items():
            a, _, b = operation
            if a in shouted and b in shouted:
                yell(name, operation)
                if name == end:
                    break
            else:
                newOpsLeft[name] = operation
        opsLeft = {**newOpsLeft}

def reduce_equations(): #Find monkeys dependent on humn, for all other monkeys
                        #calculate the number they will always shout
    while len(newOps) < len(inputs):
        for monkey in operations:
            a, op, b = operations[monkey]
            if (a in yelled or a in newOps) and (b in yelled or b in newOps):
                a = yelled[a] if a in yelled else newOps[a] 
                b = yelled[b] if b in yelled else newOps[b]
                if monkey == end:
                    newOps[monkey] = [a, b]
                    break
                else:
                    newOps[monkey] = "".join(["(", str(a), op, str(b), ")"])
                    if "x" in newOps[monkey]:
                        human.add(monkey)
                        newOps[monkey] = "x" 
                        #just need to store it's dependent on x
                    else:
                        newOps[monkey] = eval(newOps[monkey])
                        #evaluate the equation to store the result
        if end in newOps:
            break

def find_x(monkey, x): #Run down from root, reversing operations to find x, the
                       #number that humn has to shout
    if monkey == "humn":
        return x
    if x == None: #Starting at root
        a, _, b = operations[monkey]
        if b in human: #find the side dependent on x
            x = newOps[a] #the side that resolves becomes an estimate for x
            down = b #the side that's dependent on x will be checked next
        else:
            x = newOps[b]
            down = a
    else:
        a, op, b = operations[monkey]
        if op == "//": #if op is division, the order matters
            if b in human: #find the side dependent on x
                down = b #if x is on the denominator
                x = newOps[a]//x #rearrange equation
            else: 
                down = a
                x *= newOps[b] #else just multiply
        elif op == "-": #if op is subtraction, the order matters
            if b in human: #find the side dependent on x
                down = b
                x = newOps[a] - x #rearrange the equation
            else:
                down = a
                x += newOps[b] #else just add
        else: #order doesn't matter for + and *
            if b in human: #find the side dependent on x
                down = b
                y = newOps[a]
            else:
                down = a
                y = newOps[b]
            if op == "+":
                x -= y
            elif op == "*":
                x = x//y
    x = find_x(down, x)
    return x

def part_one():
    global shouted
    shouted = {k: v for k, v in yelled.items()}
    run_shouting()
    print(f"Part One = {shouted[end]}")

def part_two():
    global newOps, human
    newOps = {**yelled}
    human = set()
    yelled["humn"] = "x"
    reduce_equations()
    x = None
    x = find_x(end, x)
    print(f"Part Two = {x}")
    

inputs = open_file()

format_data()

end = "root"

part_one()
part_two()
