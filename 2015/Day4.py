import hashlib

def find_hash():
    i = 1
    foundone = 0
    foundtwo = 0
    while not foundone or not foundtwo:
        string = secretkey + str(i)
        hashval = hashlib.md5(string.encode()).hexdigest()
        if hashval[0:5] == "00000" and not foundone:
            part_one = i
            foundone = 1
        if hashval[0:6] == "000000" and not foundtwo:
            part_two = i
            foundtwo = 1
        i += 1
    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")

secretkey = "ckczppom"

find_hash()