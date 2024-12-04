"""
Advent of Code
2022 Day 25

@author: Tom Herbert
"""

day = 25

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    return inputs

def find_total():
    bf = {**baseFive}
    t = sum(sum(5**i * bf[c] for i, c in enumerate(l[::-1])) for l in inputs)
    return t

def convert_total(total):
    nBits = 0
    while True:
        nBits += 1
        newTotal = total + ((5**nBits)//2)
        if newTotal < 5**nBits:
            break
    string = ""
    reverseBaseFive = {v: k for k, v in baseFive.items()}
    for i in range(nBits, 0, -1):
        bit = newTotal//(5**(i-1)) - 2
        newTotal = newTotal % (5**(i-1))
        string += reverseBaseFive[bit]
    return string

def run():
    total = find_total()
    string = convert_total(total)
    print(f"Part One = {string}")

inputs = open_file()

baseFive = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}

run()