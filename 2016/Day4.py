def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global realrooms
    realrooms = {}
    for line in inputs:
        *name, sectid = line.split("-")
        name = "".join(name)
        sectid, checksum = sectid.strip("]").split("[")
        sectid = int(sectid)
        counts = set()
        for char in name:
            count = name.count(char)
            counts.add((char, count))
        counts = sorted(counts, key=lambda x: (-x[1], x[0]))
        string = ""
        for i in range(5):
            string += counts[i][0]
        if string == checksum:
            realrooms[name] = sectid
    print(f"Part One: {sum(realrooms.values())}")

def decrypt():
    asca = 97
    alphlen = 26
    target = "northpoleobjectstorage"
    for name in realrooms:
        step = realrooms[name]
        realname = ""
        for char in name:
            ascchar = ord(char)
            letter = ascchar - asca
            newletter = (letter + step) % alphlen
            newletter = newletter + asca
            newchar = chr(newletter)
            realname += newchar
        if realname == target:
            print(f"Part Two: {step}")
            break

day = 4
open_file()

format_data()

decrypt()