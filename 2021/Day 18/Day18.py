"""
Advent of Code
2021 Day 18

@author: Tom Herbert
"""

class SnailFish:
    def __init__(self, numbers):
        self.numbers = list(numbers)
    
    def add_snailfish(self, other):
        new = [[v, d+1] for v, d in self.numbers + other.numbers]
        newSnailfish = SnailFish(new)
        return newSnailfish
    
    def can_explode(self):
        for i, vals in enumerate(self.numbers[:-1]):
            _, dep = vals
            if dep > 4 and dep == self.numbers[i+1][1]:
                return True
        return False
    
    def can_split(self):
        for vals in self.numbers:
            val, _ = vals
            if val > 9:
                return True
        return False
    
    def explode(self):
        for idx, vals in enumerate(self.numbers[:-1]):
            val, dep = vals
            if dep > 4 and dep == self.numbers[idx+1][1]:
                break
        left, right = val, self.numbers[idx+1][0]
        if idx > 0:
            self.numbers[idx-1][0] += left
        if idx+2 < len(self.numbers):
            self.numbers[idx+2][0] += right
        new = [0, dep-1]
        self.numbers[idx] = new
        self.numbers.pop(idx+1)
    
    def split(self):
        for idx, vals in enumerate(self.numbers):
            val, dep = vals
            if val > 9:
                break
        left = val//2
        right = val - left
        self.numbers[idx] = [left, dep + 1]
        self.numbers.insert(idx+1, [right, dep + 1])
    
    def magnitude(self):
        mag = list(self.numbers)
        while len(mag) > 1:
            for i, vals in enumerate(mag[:-1]):
                val, dep = vals
                if dep == mag[i+1][1]:
                    idx = i
                    break
            left, right = val, mag[idx+1][0]
            score = 3*left + 2*right
            new = [score, dep-1]
            mag[idx] = new
            mag.pop(idx+1)
        return mag[0][0]

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [line.strip() for line in file.readlines()]
    file.close()
    return inputs

def format_data():
    global snailfish
    snailfish = []
    for line in inputs:
        levels = []
        sequence = []
        for char in line:
            if char == "[":
                levels.append(char)
            elif char == "]":
                levels.pop()
            elif char == ",":
                continue
            else:
                number = [int(char), len(levels)]
                sequence.append(number)
        snailfish.append(SnailFish(sequence))

def part_one():
    current = snailfish[0]
    for sf in snailfish[1:]:
        current = current.add_snailfish(sf)
        canExplode, canSplit = True, True
        while canExplode or canSplit:
            canExplode = current.can_explode()
            canSplit = current.can_split()
            if canExplode:
                current.explode()
            elif canSplit:
                current.split()
    score = current.magnitude()
    print(f"Part One = {score}")

def part_two():
    maxScore = 0
    for i, first in enumerate(snailfish):
        for j, second in enumerate(snailfish):
            if i == j:
                continue
            combined = first.add_snailfish(second)
            canExplode, canSplit = True, True
            while canExplode or canSplit:
                canExplode = combined.can_explode()
                canSplit = combined.can_split()
                if canExplode:
                    combined.explode()
                elif canSplit:
                    combined.split()
            score = combined.magnitude()
            if score > maxScore:
                maxScore = score
    print(f"Part Two = {maxScore}")

day = 18
inputs = open_file()

format_data()

part_one()
part_two()