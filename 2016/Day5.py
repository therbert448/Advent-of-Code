import hashlib

def passworda():
    count = 8
    i = 0
    pw = ""
    while count:
        string = instring + str(i)
        hashval = hashlib.md5(string.encode()).hexdigest()
        if hashval[0:5] == "00000":
            char = hashval[5]
            pw += char
            count -= 1
        i += 1
    print(f"Part One: {pw}")

def passwordb():
    count = 8
    i = 0
    pw = [0] * 8
    found = set()
    while count:
        string = instring + str(i)
        hashval = hashlib.md5(string.encode()).hexdigest()
        if hashval[0:5] == "00000":
            char = hashval[5]
            try:
                char = int(char)
                if 0 <= char < 8:
                    if char not in found:
                        pw[char] = hashval[6]
                        count -= 1
                        found.add(char)
            except:
                pass
        i += 1
    print(f'Part Two: {"".join(pw)}')

instring = "ojvtpuvg"

passworda()
passwordb()