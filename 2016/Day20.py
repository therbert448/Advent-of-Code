def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global ranges
    ranges = []
    for line in inputs:
        minval, maxval = line.split("-")
        minval, maxval = [int(minval), int(maxval)]
        ranges.append((minval, maxval))
    ranges.sort()

def find_min_IP():
    global possIPs
    currentIP = 0
    possIPs = set()
    while currentIP <= maxIP:
        for minmax in ranges:
            lower, upper = minmax
            if lower <= currentIP <= upper:
                currentIP = upper + 1
        if currentIP > maxIP:
            break
        possIPs.add(currentIP)
        currentIP += 1
    print(f"Part One: {min(possIPs)}")
    print(f"Part Two: {len(possIPs)}")
            

day = 20
open_file()

format_data()

maxIP = 4294967295

find_min_IP()