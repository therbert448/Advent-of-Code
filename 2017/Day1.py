def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.read().strip()
    file.close()

def format_data():
    global digits
    digits = []
    for digit in inputs:
        digits.append(int(digit))

def find_pairs(part):
    global pairs
    pairs = []
    length = len(digits)
    for i, digit in enumerate(digits):
        if part == 1:
            nexti = (i + 1) % length
        else:
            nexti = (i + length//2) % length
        if digit == digits[nexti]:
            pairs.append(digit)
        else:
            pairs.append(0)

def part_one():
    find_pairs(1)
    print("Part One:", sum(pairs))

def part_two():
    find_pairs(2)
    print("Part Two:", sum(pairs))

day = 1
open_file()

format_data()

part_one()
part_two()