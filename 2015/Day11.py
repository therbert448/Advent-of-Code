def check_password(password):
    for char in bad:
        if char in password:
            return False
    doubcount = 0
    for double in doubles:
        if double in password:
            doubcount += 1
    if doubcount < 2:
        return False
    for i, char in enumerate(password):
        if i < len(password) - 2:
            a, b, c = [char, password[i+1], password[i+2]]
            if ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1:
                return True
    return False

def new_password(password):
    newpw = ""
    revpw = password[::-1]
    point = 0
    incrementing = 1
    while incrementing:
        char = revpw[point]
        num = ord(char)
        num += 1
        if num > 122:
            num = 97
        else:
            incrementing = 0
        newchar = chr(num)
        newpw += newchar
        point += 1
    newpw += revpw[point:]
    newpw = newpw[::-1]
    return newpw

def increment_password():
    newpw = "hxbxwxba"
    goodpassword = False
    while not goodpassword:
        newpw = new_password(newpw)
        goodpassword = check_password(newpw)
    print(f"Part One: {newpw}")
    goodpassword = False
    while not goodpassword:
        newpw = new_password(newpw)
        goodpassword = check_password(newpw)
    print(f"Part Two: {newpw}")

doubles = []
for i in range(26):
    double = chr(97 + i) * 2
    doubles.append(double)
bad = ("i", "o", "l")

increment_password()