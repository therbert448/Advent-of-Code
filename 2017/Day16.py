def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.read().strip().split(",")
    file.close()

def format_data():
    global steps
    steps = []
    for step in inputs:
        move = step[0]
        if move == "s":
            num = int(step[1:])
            steps.append([move, num])
        elif move == "x":
            a, b = step[1:].split("/")
            a, b = [int(a), int(b)]
            steps.append([move, a, b])
        else:
            a, b = step[1:].split("/")
            steps.append([move, a, b])

def generate_dancers():
    global dancers
    dancers = {}
    ascmin = 97
    for i in range(day):
        dancers[chr(ascmin + i)] = i

def dance():
    for step in steps:
        move = step[0]
        if move == "s":
            val = step[1]
            for d in dancers:
                dancers[d] = (dancers[d] + val) % day
        elif move == "x":
            a, b = step[1:]
            for key, val in dancers.items():
                if val == a:
                    akey = key
                elif val == b:
                    bkey = key
            dancers[akey] = b
            dancers[bkey] = a
        elif move == "p":
            akey, bkey = step[1:]
            a = dancers[akey]
            b = dancers[bkey]
            dancers[akey] = b
            dancers[bkey] = a

def part_one():
    generate_dancers()
    dance()
    keyorder = "".join(sorted(dancers, key=dancers.get))
    print("Part One:", keyorder)

def part_two():
    n = 1_000_000_000
    generate_dancers()
    keyorder = "".join(sorted(dancers, key=dancers.get))
    posdict = {keyorder: 0}
    for i in range(n):
        dance()
        i += 1
        keyorder = "".join(sorted(dancers, key=dancers.get))
        if keyorder in posdict:
            startloop = posdict[keyorder]
            endloop = i
            break
        else:
            posdict[keyorder] = i
    looplen = endloop - startloop
    offset = n % looplen
    for key, val in posdict.items():
        if val == offset:
            print("Part Two:", key)
            return

day = 16
open_file()

format_data()

part_one()
part_two()