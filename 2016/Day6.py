def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global cols
    strlen = len(inputs[0])
    cols = [""] * strlen
    for line in inputs:
        for i in range(strlen):
            cols[i] += line[i]
    finalstra = ""
    finalstrb = ""
    for col in cols:
        maxcount = 0
        mincount = -1
        for char in col:
            charcount = col.count(char)
            if charcount > maxcount:
                maxchar = char
                maxcount = charcount
            if charcount < mincount or mincount == -1:
                minchar = char
                mincount = charcount
        finalstra += maxchar
        finalstrb += minchar
    print(f"Part One: {finalstra}")
    print(f"Part Two: {finalstrb}")

day = 6
open_file()

format_data()