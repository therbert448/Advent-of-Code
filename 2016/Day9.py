def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global string
    inputs = [line.strip() for line in file.readlines()]
    string = "".join(inputs)
    file.close()

def decompress():
    newstring = ""
    point = 0
    strlen = len(string)
    while point < strlen:
        char = string[point]
        if char == "(":
            end = string.index(")", point)
            marker = string[point+1:end]
            length, times = marker.split("x")
            length, times = [int(length), int(times)]
            idx = end + 1
            point = idx + length
            if point >= strlen:
                repeat = string[idx:] * times
            else:
                repeat = string[idx:point] * times
            newstring += repeat
        else:
            newstring += char
            point += 1
    print(f"Part One: {len(newstring)}")

def decompress2(string):
    newstring = 0
    point = 0
    strlen = len(string)
    while point < strlen:
        char = string[point]
        if char == "(":
            end = string.index(")", point)
            marker = string[point+1:end]
            length, times = marker.split("x")
            length, times = [int(length), int(times)]
            idx = end + 1
            point = idx + length
            if point >= strlen:
                totallength = decompress2(string[idx:])
            else:
                totallength = decompress2(string[idx:point])
            newstring += totallength * times
        else:
            newstring += 1
            point += 1
    return newstring

day = 9
open_file()

decompress()
fulllength = decompress2(string)
print(f"Part Two: {fulllength}")