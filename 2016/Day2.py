def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global steps
    steps = [line.strip() for line in file.readlines()]
    file.close()

def follow_steps(keypad, part):
    pos = (0, 0)
    code = ""
    for line in steps:
        for move in line:
            step = directs[move]
            newpos = tuple(map(lambda a,b : a + b, pos, step))
            if newpos in keypad:
                pos = newpos
        code += str(keypad[pos])
    print(f"Part {part}: {code}")

day = 2
open_file()

directs = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}

keypada = {(-1, 1) : 1, (0, 1) : 2, (1, 1) : 3,
           (-1, 0) : 4, (0, 0) : 5, (1, 0) : 6,
           (-1, -1): 7, (0, -1): 8, (1, -1): 9}

keypadb = {                           (0, 2) : 1,
                       (-1, 1) : 2,   (0, 1) : 3,   (1, 1) : 4,
           (-2, 0): 5, (-1, 0) : 6,   (0, 0) : 7,   (1, 0) : 8,   (2, 0): 9,
                       (-1, -1): "A", (0, -1): "B", (1, -1): "C",
                                      (0, -2): "D"                         }

follow_steps(keypada, "One")
follow_steps(keypadb, "Two")