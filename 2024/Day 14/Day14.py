"""
Advent of Code
2024 Day 14

@author: Tom Herbert
"""
from time import time

day = 14

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [l.strip().split() for l in file.readlines()]
    robots = []
    for line in inputs:
        pos, vel = line
        x, y = [int(v) for v in pos.split("=")[1].split(",")]
        vx, vy = [int(v) for v in vel.split("=")[1].split(",")]
        robots.append([(x, y), (vx, vy)])
    return robots

def plot_grid(i, bots):
    print(i)
    for y in range(ymax):
        line = ""
        for x in range(xmax):
            if (x, y) in bots:
                line += "#"
            else: line += " "
        print(line)

robots = open_file(day)
xmax, ymax = 101, 103
N = 100

finalRobs = [[0, 0], [0, 0]]
for bot in robots:
    (x, y), (vx, vy) = bot
    finalx = (x + (vx * N)) % xmax
    finaly = (y + (vy * N)) % ymax
    if finalx == xmax//2 or finaly == ymax//2:
        continue
    xhalf = int(finalx//(xmax/2))
    yhalf = int(finaly//(ymax/2))
    finalRobs[yhalf][xhalf] += 1
product = 1
for i in range(2):
    for j in range(2):
        product *= finalRobs[i][j]
print(product)

# tree = False
# i = 1
# while not tree:
#     finalBots = set()
#     for bot in robots:
#         (x, y), (vx, vy) = bot
#         finalx = (x + (vx * i)) % xmax
#         finaly = (y + (vy * i)) % ymax
#         finalBots.add((finalx, finaly))
#     if len(finalBots) == len(robots): 
#         plot_grid(i, finalBots)
#         break
#     i += 1

tree = False
i = 0
while not tree:
    i += 1
    finalRobs = [[0, 0], [0, 0]]
    finalBots = set()
    for bot in robots:
        (x, y), (vx, vy) = bot
        finalx = (x + (vx * i)) % xmax
        finaly = (y + (vy * i)) % ymax
        finalBots.add((finalx, finaly))
        if finalx == xmax//2 or finaly == ymax//2:
            continue
        xhalf = int(finalx//(xmax/2))
        yhalf = int(finaly//(ymax/2))
        finalRobs[yhalf][xhalf] += 1
    for x in range(2):
        for y in range(2):
            if finalRobs[y][x] > len(robots)//2:
                tree = True
plot_grid(i, finalBots)