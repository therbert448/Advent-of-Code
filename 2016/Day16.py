def dragon_curve(strlist, length):
    strlen = len(strlist)
    while strlen < length:
        a = list(strlist)
        b = ["1" if char == "0" else "0" for char in a[::-1]]
        strlist = [*a, "0", *b]
        strlen = len(strlist)
    return strlist[:length]

def checksum(strlist):
    checklen = len(strlist)
    while checklen % 2 == 0:
        newlen = checklen // 2
        checksum = []
        for i in range(newlen):
            idx = i * 2
            pair = strlist[idx:idx+2]
            if pair[0] == pair[1]:
                checksum.append("1")
            else:
                checksum.append("0")
        strlist = list(checksum)
        checklen = newlen
    return strlist

def part_one():
    string = "10001001100000001"
    strlist = [char for char in string]
    length = 272
    strlist = dragon_curve(strlist, length)
    checklist = checksum(strlist)
    check = "".join(checklist)
    print(f"Part One: {check}")

def part_two(): #Not too slow to need a different approach
    string = "10001001100000001"
    strlist = [char for char in string]
    length = 35651584
    strlist = dragon_curve(strlist, length)
    checklist = checksum(strlist)
    check = "".join(checklist)
    print(f"Part Two: {check}")

part_one()
part_two()