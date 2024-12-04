"""
Advent of Code
2021 Day 8

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [line.split("|") for line in file.readlines()]
    file.close()
    return inputs

def format_data():
    global signals
    signals = [[inOut.strip().split() for inOut in line] for line in inputs]

def part_one():
    unique = (2, 3, 4, 7)
    count = sum([sum([1 for s in l[1] if len(s) in unique]) for l in signals])
    print(f"Part One = {count}")
        
def part_two():
    count = 0
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    for line in signals:
        pattern, output = line
        pattern = ["".join(sorted(string)) for string in pattern]
        pattern.sort(key=len)
        counts = {c:sum([1 for s in pattern if c in s]) for c in letters}
        translate = {}
        for l, c in counts.items():
            if c in countToLetter:
                translate[l] = countToLetter[c]
            if c == 7 and l in pattern[2]:
                translate[l] = "d"
            elif c == 7:
                translate[l] = "g"
            if c == 8 and l in pattern[0]:
                translate[l] = "c"
            elif c == 8:
                translate[l] = "a"
        displays = ["".join(sorted([translate[c] for c in s])) for s in output]
        outString = ""
        for d in displays:
            outString += display[d]
        count += int(outString)
    print(f"Part Two = {count}")

day = 8
inputs = open_file()

format_data()

display = {"abcefg" : "0",
           "cf"     : "1",
           "acdeg"  : "2",
           "acdfg"  : "3",
           "bcdf"   : "4",
           "abdfg"  : "5",
           "abdefg" : "6",
           "acf"    : "7",
           "abcdefg": "8",
           "abcdfg" : "9"}
countToLetter = {4: "e",
                 6: "b",
                 9: "f"}

part_one()
part_two()