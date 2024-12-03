"""
Advent of Code
2024 Day 03

@author: Tom Herbert
"""

day = 3

def open_file(day):
    #filename = "test2.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        program = file.read()
    return program

def run_parts(program, part = "One"):
    point, total, flag = 0, 0, True
    while point < len(program):
        if program[point:point+4] == "do()":
            flag = True
            point += 4
            continue
        if program[point:point+7] == "don't()":
            flag = False
            if part == "One": flag = True
            point += 7
        if program[point:point+4] == "mul(":
            point += 4
            if not flag:
                continue
            idx = program[point:point+4].find(",")
            if idx == -1 or not program[point:point+idx].isnumeric():
                continue
            a = int(program[point:point+idx])
            point += idx + 1
            idx = program[point:point+4].find(")")
            if idx == -1 or not program[point:point+idx].isnumeric():
                continue
            b = int(program[point:point+idx])
            total += a * b
        point += 1
    print(f"Part {part} = {total}")

program = open_file(day)

run_parts(program)
run_parts(program, "Two")

# point = 0
# total = 0
# while point < len(program):
#     if program[point:point+4] == "mul(":
#         point += 4
#         idx = program[point:point+4].find(",")
#         if idx == -1 or not program[point:point+idx].isnumeric():
#             continue
#         a = int(program[point:point+idx])
#         point += idx + 1
#         idx = program[point:point+4].find(")")
#         if idx == -1 or not program[point:point+idx].isnumeric():
#             continue
#         b = int(program[point:point+idx])
#         total += a * b
#     point += 1

# print(total)
            
# point = 0
# total = 0
# flag = True
# while point < len(program):
#     if program[point:point+4] == "do()":
#         flag = True
#         point += 4
#         continue
#     if program[point:point+7] == "don't()":
#         flag = False
#         point += 7
#     if program[point:point+4] == "mul(":
#         point += 4
#         if not flag:
#             continue
#         idx = program[point:point+4].find(",")
#         if idx == -1 or not program[point:point+idx].isnumeric():
#             continue
#         a = int(program[point:point+idx])
#         point += idx + 1
#         idx = program[point:point+4].find(")")
#         if idx == -1 or not program[point:point+idx].isnumeric():
#             continue
#         b = int(program[point:point+idx])
#         total += a * b
#     point += 1

# print(total)