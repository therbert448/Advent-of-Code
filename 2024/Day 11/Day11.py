"""
Advent of Code
2024 Day 11

@author: Tom Herbert
"""
from time import time

def blink(stone, blinksLeft):
    stoneStr = str(stone)
    digits = len(stoneStr)
    if stone in changes:
        newStones = changes[stone]
    else:
        if stone == 0:
            newStones = [1]
        elif not digits % 2:
            newStones = [int(stoneStr[:digits//2]), int(stoneStr[digits//2:])]
        else:
            newStones = [stone * 2024]
        changes[stone] = newStones
    blinksLeft -= 1
    if blinksLeft == 0:
        return len(newStones)
    total = 0
    for newStone in newStones:
        if (newStone, blinksLeft) not in totals:
            totals[(newStone, blinksLeft)] = blink(newStone, blinksLeft)
        total += totals[(newStone, blinksLeft)]
    return total

test1 = [0, 1, 10, 99, 999]
test2 = [125, 17]
Day11inputs = [27, 10647, 103, 9, 0, 5524, 4594227, 902936]

stones = Day11inputs
t0 = time()
changes = {}
totals = {}

blinks = 25
result = 0
for stone in stones:
    result += blink(stone, blinks)
print(f"Part One = {result}")
t1 = time()
print(f"...took {round(t1-t0, 6)}s\n")
result = 0
blinks = 75
for stone in stones:
    result += blink(stone, blinks)
print(f"Part Two = {result}")
t2 = time()
print(f"...took {round(t2-t1, 6)}s\n")