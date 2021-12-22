import time
import numpy as np

def game(n):
    memory = np.array([0] * n)
    dif = 0
    for i in range(n):
        if i < len(startns):
            nextnum = startns[i]
        else:
            nextnum = dif

        if memory[nextnum] == 0:
            dif = 0
        else:
            dif = i+1 - memory[nextnum]
        
        memory[nextnum] = i+1
    return nextnum

startns = [2, 20, 0, 4, 1, 17]
n1 = 2020
n2 = 30000000

t1 = time.perf_counter()
print(game(n1))
t2 = time.perf_counter()
print(game(n2))
t3 = time.perf_counter()

print(f"Part one took {t2 - t1:0.7f} seconds")
#Part one took 0.0048447 seconds
print(f"Part two took {t3 - t2:0.7f} seconds")
#Part two took 8.4844882 seconds
