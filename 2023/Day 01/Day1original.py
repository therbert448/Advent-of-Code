"""
Advent of Code
2022 Day 25

@author: Tom Herbert
"""

day = 1

words = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5',
         "six": '6', "seven": '7', "eight": '8', "nine": '9'}
firsts = {"o": ["one"], "t": ["two", "three"], "f": ["four", "five"],
          "s": ["six", "seven"], "e": ["eight"], "n": ["nine"]}
lasts = {"e": ["one", "three", "five", "nine"], "o": ["two"], "r": ["four"],
         "x": ["six"], "n": ["seven"], "t": ["eight"]}

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    return inputs

def part_one(inputs):
    total = 0
    for line in inputs:
        nums = [char for char in line if char.isnumeric()]
        total += int(nums[0] + nums[-1])
    print(f"Part One = {total}")

def part_two(inputs):
    total = 0
    for line in inputs:
        first, last = "", ""
        for i, char in enumerate(line):
            reverseLine, reverseChar = line[::-1], line[-i-1]
            if first: pass
            elif char.isnumeric():
                first = char
            elif char in firsts:
                for num in firsts[char]:
                    if line[i:i+len(num)] == num:
                        first = words[num]
                        break
            if last: pass
            elif reverseChar.isnumeric():
                last = reverseChar
            elif reverseChar in lasts:
                for num in lasts[reverseChar]:
                    if reverseLine[i:i+len(num)] == num[::-1]:
                        last = words[num]
                        break
            if first and last: break
        total += int(first + last)
    print(f"Part Two = {total}")

inputs = open_file(day)

part_one(inputs)
part_two(inputs)