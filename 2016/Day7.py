def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global addressesa, addressesb
    addressesa = set()
    addressesb = set()
    for line in inputs:
        valida = 0
        validb = 1
        bracks = 0
        strlen = len(line)
        aba, bab = [set(), set()]
        for i, char in enumerate(line):
            if char == "[":
                bracks = 1
                continue
            elif char == "]":
                bracks = 0
                continue
            if i < strlen - 3:
                if char != line[i+1]:
                    if line[i+1] == line[i+2] and char == line[i+3]:
                        if bracks:
                            validb = 0
                        else:
                            valida = 1
            if i < strlen - 2:
                if char != line[i+1]:
                    if char == line[i+2]:
                        if bracks:
                            ab = (line[i+1], char)
                            bab.add(ab)
                        else:
                            ab = (char, line[i+1])
                            aba.add(ab)
            else:
                break
        if valida and validb:
            addressesa.add(line)
        for ab in aba:
            if ab in bab:
                addressesb.add(line)
                break
    print(f"Part One: {len(addressesa)}")
    print(f"Part Two: {len(addressesb)}")

day = 7
open_file()

format_data()