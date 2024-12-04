def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global memory
    memory = [int(digit) for digit in file.read().strip().split("\t")]
    file.close()

def reallocate():
    redcycles = 0
    state = tuple(memory)
    states = {state: redcycles}
    length = len(memory)
    loop = 0
    while not loop:
        maxblocks = max(memory)
        idx = memory.index(maxblocks)
        memory[idx] = 0
        idx += 1
        for _ in range(maxblocks):
            idx = idx % length
            memory[idx] += 1
            idx += 1
        redcycles += 1
        state = tuple(memory)
        if state in states:
            print("Part One:", redcycles)
            loopsize = redcycles - states[state]
            print("Part Two:", loopsize)
            loop = 1
            break
        else:
            states[state] = redcycles
    

day = 6
open_file()

reallocate()