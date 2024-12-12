"""
Advent of Code
2024 Day 05

@author: Tom Herbert
"""

day = 5

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        rules, pages = file.read().split("\n\n")
    rules = [line.split("|") for line in rules.splitlines()]
    rules = set([tuple([int(v) for v in line[::-1]]) for line in rules])
    pages = [[int(v) for v in line.split(",")] for line in pages.splitlines()]
    return rules, pages

rules, pages = open_file(day)

total = 0
broken = []
for update in pages:
    valid = True
    for i, pageOne in enumerate(update):
        for pageTwo in update[i+1:]:
            if (pageOne, pageTwo) in rules:
                valid = False
                break
        if not valid:
            broken.append(update)
            break
    if valid: total += update[len(update)//2]
print(total)

total = 0
for update in broken:
    valid = False
    while not valid:
        valid = True
        for i, pageOne in enumerate(update):
            for j, pageTwo in enumerate(update[i+1:]):
                if (pageOne, pageTwo) in rules:
                    update[i] = pageTwo
                    update[i+j+1] = pageOne
                    valid = False
                break
            if not valid: break
    total += update[len(update)//2]
print(total)