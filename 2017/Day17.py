def fill_buffer():
    global buffer
    buffer = {0: 0}
    current = 0
    for i in range(2017):
        for _ in range(step):
            current = buffer[current]
        nextval = buffer[current]
        buffer[current] = i+1
        buffer[i+1] = nextval
        current = i+1
    print("Part One:", nextval)

def track_after_zero():
    point = 0
    bufferlen = 1
    nexttozero = 0
    for i in range(50_000_000):
        addval = i + 1
        point = ((point + step) % bufferlen) + 1
        if point == 1: #zero always at position zero, so position 1 is next
            nexttozero = addval
        bufferlen += 1
    print("Part Two:", nexttozero)

step = 348

fill_buffer()
track_after_zero()