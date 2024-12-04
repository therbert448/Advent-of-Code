#pretty slow, but I learned about Python generators, which may come in handy
#Can't think how to significantly speed it up without skipping generator
#outputs

def A_Gen(part):
    genA = 277
    while True:
        genA = (genA * multA) % modmain
        if part == 1:
            yield genA
        elif part == 2:
            if not genA % 4:
                yield genA
    
def B_Gen(part):
    genB = 349
    while True:
        genB = (genB * multB) % modmain
        if part == 1:
            yield genB
        elif part == 2:
            if not genB % 8:
                yield genB

def run_sequence(part):
    if part == 1:
        n = 40_000_000
    else:
        n = 5_000_000
    global count
    count = 0
    A = A_Gen(part)
    B = B_Gen(part)
    for i in range(n):
        genA = next(A)
        genB = next(B)
        checkA = genA % modcheck
        checkB = genB % modcheck
        if checkA == checkB:
            count += 1
    if part == 1:
        print("Part One:", count)
    else:
        print("Part Two:", count)

multA = 16807
multB = 48271
modmain = 2147483647
modcheck = 2 ** 16

run_sequence(1)
run_sequence(2)