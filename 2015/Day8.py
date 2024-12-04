def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    codelen = 0
    stringlen = 0
    newstringlen = 0
    for line in inputs:
        linelen = len(line)
        codelen += linelen
        for char in line:
            if char == "\"":
                linelen += 1
            elif char == "\\":
                linelen += 1
        newstringlen += linelen + 2
        stringlen += len(eval(line))
    difference = codelen - stringlen
    print(f"Part One: {difference}")
    difference2 = newstringlen - codelen
    print(f"Part Two: {difference2}")

day = 8
open_file()

format_data()