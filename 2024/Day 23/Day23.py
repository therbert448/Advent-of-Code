"""
Advent of Code
2024 Day 23

@author: Tom Herbert
"""
from time import time

day = 23

def open_file(day):
    filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [l.strip().split("-") for l in file.readlines()]
    pairs = set(tuple(sorted([comp for comp in pair])) for pair in inputs)
    return pairs

def grow_parties(parties):
    newParties = set()
    for party in parties:
        for computer in computers:
            if tuple(sorted([*party, computer])) in newParties: continue
            if all(tuple(sorted([computer, node])) in pairs for node in party):
                newParties.add(tuple(sorted([*party, computer])))
    return newParties

t0 = time()
pairs = open_file(day)
computers = set(comp for pair in pairs for comp in pair)

parties = grow_parties(pairs)
print(sum(1 for party in parties if any(node[0] == "t" for node in party)))
t1 = time()
print(round(t1-t0, 6))

while newParties := grow_parties(parties):
    parties = newParties
print(",".join(sorted(list(parties)[0])))
t2 = time()
print(round(t2-t1, 6))