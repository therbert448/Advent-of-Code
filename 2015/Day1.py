def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.read().strip()
    file.close()

def go_to_floor():
    floor = 0
    basement = 0
    for i, char in enumerate(inputs):
        if char == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1 and not basement:
            basement = i+1
    print(f"Part One: {floor}")
    print(f"Part Two: {basement}")

day = 1
open_file()

go_to_floor()