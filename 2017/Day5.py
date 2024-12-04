def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global jumps
    jumps = [int(line.strip()) for line in file.readlines()]
    file.close()

def follow_steps(part):
    point = 0
    stepcount = 0
    length = len(jumps)
    while point < length:
        jump = jumps[point]
        if part == "One" or jumps[point] < 3:
            jumps[point] += 1
        else:
            jumps[point] -= 1
        point += jump
        stepcount += 1
    print("Part", part,":", stepcount)

day = 5
open_file()
follow_steps("One")
open_file()
follow_steps("Two")