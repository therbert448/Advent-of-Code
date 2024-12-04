def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global rects
    rects = {}
    for line in inputs:
        rect = line.split(" @ ")
        pos, size = rect[1].split(": ")
        pos = tuple(pos.split(","))
        size = tuple(size.split("x"))
        rects[rect[0]] = (pos, size)

def part_one():
    global dupset
    posset = set()
    dupset = set()
    for rect in rects.values():
        pos = rect[0]
        dim = rect[1]
        for w in range(int(dim[0])):
            for h in range(int(dim[1])):
                x = int(pos[0]) + w
                y = int(pos[1]) + h
                coord = (x, y)
                if coord in posset:
                    dupset.add(coord)
                else:
                    posset.add(coord)
    print("Part One:", len(dupset))

def part_two():
    for code, rect in rects.items():
        good = 1
        pos = rect[0]
        dim = rect[1]
        for w in range(int(dim[0])):
            for h in range(int(dim[1])):
                x = int(pos[0]) + w
                y = int(pos[1]) + h
                coord = (x, y)
                if coord in dupset:
                    good = 0
                    break
            if good == 0:
                break
        if good == 1:
            print("Part Two:", code)
            return

day = 3
inputs = open_file()

formatdata(inputs)

part_one()
part_two()