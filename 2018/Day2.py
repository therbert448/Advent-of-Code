def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global ids
    ids = set([line.strip() for line in inputs])

def part_one():
    twos = 0
    threes = 0
    for code in ids:
        chardict = {}
        for char in code:
            chardict[char] = code.count(char)
        if 2 in chardict.values():
            twos += 1
        if 3 in chardict.values():
            threes += 1
    mult = twos * threes
    print("Part One:", mult)
    
def part_two():
    idset = set()
    for code in ids:
        codeset = set()
        chars = [char for char in code]
        for i, char in enumerate(chars):
            newchars = list(chars)
            newchars.pop(i)
            string = "".join(newchars)
            if string in idset and string not in codeset:
                print("Part Two:", string)
                return
            else:
                codeset.add(string)
                idset.add(string)

day = 2
inputs = open_file()

formatdata(inputs)

part_one()
part_two()