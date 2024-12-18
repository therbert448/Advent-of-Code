"""
Advent of Code
2024 Day 13

@author: Tom Herbert
"""
from time import time

day = 13

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        blocks = [l.strip().splitlines() for l in file.read().split("\n\n")]
    games = []
    for block in blocks:
        matrix = []
        for i, line in enumerate(block):
            halves = line.strip().split(",")
            if i < 2:
                parts = [half.split("+") for half in halves]
                a, b = int(parts[0][1]), int(parts[1][1])
                matrix.append([a, b])
            else:
                parts = [half.split("=") for half in halves]
                a, b = int(parts[0][1]), int(parts[1][1])
                prize = [a, b]
        matrix = transpose(matrix)
        games.append([matrix, prize])
    return games

def transpose(M):
    m, n = 2, 2
    MT = [[M[i][j] for i in range(m)] for j in range(n)]
    return MT

games = open_file(day)

result = 0
for game in games:
    matrix, prize = game
    [a, b], [c, d] = matrix
    xPrize, yPrize = prize
    det = (a * d) - (b * c)
    if det == 0:
        print(matrix)
        continue
    A = ((d * xPrize) - (b * yPrize))/det
    B = ((a * yPrize) - (c * xPrize))/det
    if A % 1: A = False
    else: A = int(A)
    if B % 1: B = False
    else: B = int(B)
    if all([A, B]):
        result += (3 * A) + B
print(result)

add = 10000000000000
result = 0
for game in games:
    matrix, prize = game
    [a, b], [c, d] = matrix
    xPrize, yPrize = prize
    xPrize += add
    yPrize += add
    det = (a * d) - (b * c)
    if det == 0:
        print(matrix)
        continue
    A = ((d * xPrize) - (b * yPrize))/det
    B = ((a * yPrize) - (c * xPrize))/det
    if A % 1: A = False
    else: A = int(A)
    if B % 1: B = False
    else: B = int(B)
    if all([A, B]):
        result += (3 * A) + B
print(result)