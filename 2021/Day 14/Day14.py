"""
Advent of Code
2021 Day 14

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().split("\n\n")
    file.close()
    return inputs

def format_data():
    global template, rules
    rules = {}
    string, lines = inputs
    template = string.strip()
    for line in lines.splitlines():
        pair, insert = line.strip().split(" -> ")
        rules[pair] = insert

def count_pairs(template):
    pair_counts = {}
    for i in range(len(template)-1):
        pair = template[i:i+2]
        if pair not in pair_counts:
            pair_counts[pair] = 1
        else:
            pair_counts[pair] += 1
    return pair_counts

def count_chars(polymer):
    chars = set([c for c in polymer])
    letterCounts = {c:polymer.count(c) for c in chars}
    return letterCounts

def insertion(pairCounts, letterCounts):
    newCounts = {}
    for pair, count in pairCounts.items():
        first, second = pair
        if pair in rules:
            newChar = rules[pair]
            pairOne = first + newChar
            pairTwo = newChar + second
            for newPair in [pairOne, pairTwo]:
                if newPair not in newCounts:
                    newCounts[newPair] = count
                else:
                    newCounts[newPair] += count
            if newChar not in letterCounts:
                letterCounts[newChar] = count
            else:
                letterCounts[newChar] += count
    return newCounts, letterCounts

def part_one():
    pairCounts = count_pairs(template)
    letterCounts = count_chars(template)
    for _ in range(10):
        pairCounts, letterCounts = insertion(pairCounts, letterCounts)
    score = max(letterCounts.values()) - min(letterCounts.values())
    print(f"Part One = {score}")

def part_two():
    pairCounts = count_pairs(template)
    letterCounts = count_chars(template)
    for _ in range(40):
        pairCounts, letterCounts = insertion(pairCounts, letterCounts)
    score = max(letterCounts.values()) - min(letterCounts.values())
    print(f"Part Two = {score}")

day = 14
inputs = open_file()

format_data()

part_one()
part_two()