"""
Advent of Code
2022 Day 13

@author: Tom Herbert
"""

day = 13

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = file.read().split("\n\n")
    pairs = []
    for line in inputs:
        left, right = line.splitlines()
        left, right = eval(left), eval(right)
        pairs.append([left, right])
    return pairs

def compare(left, right):
    leftType, rightType = type(left), type(right)
    if leftType != rightType: #make integer into a list
        if leftType != list:
            left = [left]
            leftType = type(left)
        else:
            right = [right]
    if leftType == list: #compare lists
        left = [v for v in left]
        right = [v for v in right]
        while left and right: #compare each term in both lists
            newLeft, newRight = left.pop(0), right.pop(0)
            inOrder = compare(newLeft, newRight)
            if inOrder == None: #both elements in each list were equal
                continue
            else:
                return inOrder
        if not left and not right: #both lists were the same length and equal
            return None
        else: #if left ran out first, then it's in order
            return bool(right)
    else: #compare integers
        if left == right: #move on if integers are equal
            return None
        else: #left should be less than right
            return bool(left < right)

def part_one():
    indices = []
    for i, pair in enumerate(pairs):
        left, right = pair
        inOrder = compare(left, right)
        if inOrder:
            indices.append(i+1) #indexing starts at 1
    print(f"Part One = {sum(indices)}")

def part_two():
    packets = []
    for pair in pairs:
        for packet in pair:
            packets.append(packet)
    a, b = [[2]], [[6]]
    acount, bcount = 1, 2 #indexing starts at 1, a is less than b
    for packet in packets: #count number of packets less than a and b
        lowerThanA = compare(packet, a)
        lowerThanB = compare(packet, b)
        if lowerThanA: #anything lower than a is also lower than b
            acount += 1
            bcount += 1
        elif lowerThanB:
            bcount += 1
    result = acount * bcount
    print(f"Part Two = {result}")

pairs = open_file()

part_one()
part_two()