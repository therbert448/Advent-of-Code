def next_elf():
    global presents
    presents = {}
    for i in range(elves):
        elf = i+1
        nextelf = (elf % elves) + 1
        presents[elf] = nextelf      

def steal_presents():
    elf = 1
    while len(presents) != 1:
        nextelf = presents[elf]
        nextnextelf = presents[nextelf]
        presents[elf] = nextnextelf
        del presents[nextelf]
        elf = nextnextelf
    print("Part One:", *presents.keys())

def part_one():
    next_elf()
    steal_presents()

def part_two():
    """
    elves = 100000
    elflist = []
    for i in range(elves):
        elflist.append(i+1)
    idx = 0
    while len(elflist) != 1:
        nextidx = (idx + len(elflist)//2) % len(elflist)
        elflist.pop(nextidx)
        if nextidx < idx:
            idx = idx % len(elflist)
        else:
            idx = (idx + 1) % len(elflist)
    print(*elflist)
    """
    #Found the pattern, the answer is the number of elves, n, minus the 
    #maximum value of 3 ** i, for 3 ** i < n
    #So for 100 elves, the answer is 100 - 3**4 = 100 - 81 = 19
    #for 1000 elves, 1000 - 3**6 = 1000 - 729 = 271
    #10000 - 3**8 = 10000 - 6561 = 3439
    #100000 - 3**10 = 100000 - 59049 = 40951
    powthree = 1
    while powthree < elves:
        lastpower = powthree
        powthree *= 3
    answer = elves - lastpower
    print(f"Part Two: {answer}")

elves = 3017957

part_one()
part_two()