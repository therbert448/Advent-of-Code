"""
Advent of Code
2021 Day 7

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    crabs = [int(val) for val in file.read().split(",")]
    file.close()
    return crabs

def part_one():
    #optimal crab meeting point at median of values
    #when even number of values, any value between the two central values works
    crabs.sort()
    medidx = (len(crabs) - 1)//2
    median = crabs[medidx]
    fuel = sum([abs(crab - median) for crab in crabs])
    print(f"Part One = {fuel}")

def part_two():
    #optimal crab rendez-vous near the mean of values
    mean = sum(crabs)//len(crabs) #// for floor of mean
    triangle = lambda x: int(x*(x+1)/2)
    fuel = sum([triangle(abs(crab-mean)) for crab in crabs])
    mean += 1 #also check ceil of mean
    if fuel > sum([triangle(abs(crab-mean)) for crab in crabs]):
        fuel = sum([triangle(abs(crab-mean)) for crab in crabs])
    print(f"Part Two = {fuel}")

day = 7
crabs = open_file()

part_one()
part_two()