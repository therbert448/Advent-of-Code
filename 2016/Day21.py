def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global steps
    steps = []
    for line in inputs:
        command, *rest = line.split(" ")
        if command == "swap":
            if rest[0] == "position":
                command = "swappos(*ins, word)"
                ins = [int(rest[1]), int(rest[-1])]
            else:
                command = "swaplet(*ins, word)"
                ins = [rest[1], rest[-1]]
        elif command == "rotate":
            if rest[0] == "based":
                command = "rotatebase(*ins, word, rev)"
                ins = [rest[-1]]
            else:
                command += "(*ins, word, rev)"
                ins = [rest[0], int(rest[1])]
        elif command == "reverse":
            command += "(*ins, word)"
            ins = [int(rest[1]), int(rest[-1])]
        else:
            command += "(*ins, word, rev)"
            ins = [int(rest[1]), int(rest[-1])]
        steps.append([command, ins])

def swappos(x, y, word):
    letx = word[x]
    lety = word[y]
    word[x] = lety
    word[y] = letx
    return word

def swaplet(x, y, word):
    idxx = word.index(x)
    idxy = word.index(y)
    word[idxx] = y
    word[idxy] = x
    return word

def rotate(lr, x, word, rev):
    if lr == "right" and not rev:
        x = -x
    elif lr == "left" and rev:
        x = -x
    word = [*word[x:], *word[:x]]
    return word

def rotatebase(x, word, rev):
    if not rev:
        step = -1
        idx = word.index(x) * -1
        word = [*word[step:], *word[:step]]
        word = [*word[idx:], *word[:idx]]
        if abs(idx) >= 4:
            word = [*word[step:], *word[:step]]
        return word
    else:
        step = 1
        word = [*word[step:], *word[:step]]
        count = 0
        idx = word.index(x)
        if count != idx:
            found = 0
        else:
            found = 1
        while not found:
            word = [*word[step:], *word[:step]]
            count += 1
            idx = word.index(x)
            if count < 5 and count == idx:
                found = 1
            elif count >= 5 and count == idx + 1:
                found = 1
        return word
        

def reverse(x, y, word):
    word = [*word[:x], *word[x:y+1][::-1], *word[y+1:]]
    return word

def move(x, y, word, rev):
    if not rev:
        char = word.pop(x)
        word.insert(y, char)
    else:
        char = word.pop(y)
        word.insert(x, char)
    return word

def run_steps_forwards():
    word = [char for char in "abcdefgh"]
    rev = 0
    for step in steps:
        expr, ins = step
        word = eval(expr)
    print(f"Part One: {''.join(word)}")

def run_steps_backwards():
    word = [char for char in "fbgdceah"]
    rev = 1
    for step in steps[::-1]:
        expr, ins = step
        word = eval(expr)
    print(f"Part Two: {''.join(word)}")

day = 21
open_file()

format_data()

run_steps_forwards()
run_steps_backwards()