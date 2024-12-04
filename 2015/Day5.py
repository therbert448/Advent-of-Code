def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def naughty_or_nice():
    global niceset
    niceset = set()
    for line in inputs:
        nice = 1
        for pair in bad:
            if pair in line:
                nice = 0
                break
        vowelcount = 0
        for vowel in vowels:
            vowelcount += line.count(vowel)
        if vowelcount < 3:
            nice = 0
        if not nice:
            continue
        nice = 0
        for double in doubles:
            if double in line:
                nice = 1
                break
        if nice:
            niceset.add(line)
    print(f"Part One: {len(niceset)}")

def naughty_or_nice2():
    global niceset
    niceset = set()
    for line in inputs:
        linelen = len(line)
        nice = [0, 0]
        for i, char in enumerate(line):
            if i + 2 < linelen:
                if char + line[i+1] in line[i+2:]:
                    nice[0] = 1
                if char == line[i+2]:
                    nice[1] = 1
        if all(nice):
            niceset.add(line)
    print(f"Part Two: {len(niceset)}")

day = 5
open_file()

bad = ("ab", "cd", "pq", "xy")
vowels = ("a", "e", "i", "o", "u")
doubles = []
for i in range(26):
    doub = chr(97 + i) * 2 #97 is ascii for "a"
    doubles.append(doub)

naughty_or_nice()
naughty_or_nice2()