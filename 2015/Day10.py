def read_string(string):
    point = 0
    strlen = len(string)
    newstring = ""
    while point < strlen:
        char = string[point]
        count = 0
        while point < strlen and string[point] == char:
            count += 1
            point += 1
        newstring += str(count) + char
    return newstring

def part_one():
    string = start
    for _ in range(40):
        string = read_string(string)
    print(f"Part One: {len(string)}")

def part_two():
    string = start
    for _ in range(50):
        string = read_string(string)
    print(f"Part Two: {len(string)}")

start = "1113222113"

part_one()
part_two()