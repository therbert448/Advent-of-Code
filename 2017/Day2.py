def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line for line in file.readlines()]
    file.close()

def format_data():
    global rows
    rows = []
    for row in inputs:
        row = row.split("\t")
        introw = [int(r) for r in row]
        rows.append(introw)

def check_sum():
    checksum = 0
    for row in rows:
        rowrange = max(row) - min(row)
        checksum += rowrange
    print("Part One:", checksum)

def mod_pairs():
    divsum = 0
    for row in rows:
        for i, digit in enumerate(row):
            found = 0
            for j, divide in enumerate(row):
                if j == i:
                    continue
                if digit % divide == 0:
                    div = digit // divide
                    divsum += div
                    found = 1
                    break
            if found:
                break
    print("Part Two:", divsum)

day = 2
open_file()

format_data()

check_sum()
mod_pairs()