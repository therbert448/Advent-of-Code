def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.read().strip()
    file.close()

def eval_string():
    global storage
    storage = eval(inputs)

def check_item(item):
    intsum = 0
    if isinstance(item, list):
        for iterable in item:
            intsum += check_item(iterable)
    elif isinstance(item, dict):
        if part == 2 and "red" in item.values():
            return 0
        for value in item.values():
            intsum += check_item(value)
    elif isinstance(item, int):
        intsum += item
        return intsum
    else:
        return 0
    return intsum

day = 12
open_file()

eval_string()

part = 1
intsum = check_item(storage)
print(f"Part One: {intsum}")

part = 2
intsum = check_item(storage)
print(f"Part Two: {intsum}")