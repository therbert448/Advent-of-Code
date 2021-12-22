import time

def game(n):
    memory = {}
    startl = len(startns)
    nextnum = 0
    for i in range(startl):
        thisnum = startns[i]
        memory[thisnum] = i
    
    if thisnum in memory:
        nextnum = i - memory[thisnum]
    else:
        nextnum = 0
    
    for i in range(startl, n):
        thisnum = nextnum
        if thisnum in memory:
            nextnum = i - memory[thisnum]
        else:
            nextnum = 0
        memory[thisnum] = i
    
    return thisnum

startns = [2, 20, 0, 4, 1, 17]
n1 = 2020
n2 = 30000000

t1 = time.perf_counter()
print(game(n1))
t2 = time.perf_counter()
print(game(n2))
t3 = time.perf_counter()

print(f"Part one took {t2 - t1:0.7f} seconds")
#Part one took 0.0204481 seconds
print(f"Part two took {t3 - t2:0.7f} seconds")
#Part two took 9.6940081 seconds