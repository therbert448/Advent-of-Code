"""
Advent of Code
2022 Day 9

@author: Tom Herbert
"""

day = 9

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip().split(" ") for line in file.readlines()]
    dirs = [[l[0], int(l[1])] for l in inputs]
    return dirs

def add(a, b): return a + b

def subtract(a, b): return a - b

def move_tail(H, T):
    following = H
    for i, tail in enumerate(T):
        gap = tuple(map(subtract, following, tail))
        if gap in adj:
            following = tail
            continue
        elif following == tail:
            following = tail
            continue
        if 0 in gap:
            scale = max([max(gap), abs(min(gap))])
            step = (gap[0]//scale, gap[1]//scale)
            tail = tuple(map(add, tail, step))
        else:
            step = (gap[0]//abs(gap[0]), gap[1]//abs(gap[1]))
            tail = tuple(map(add, tail, step))
        T[i] = tail
        following = tail
    return T

def move_head(move, H, T):
    dire, step = move
    for _ in range(step):
        H = tuple(map(add, H, moves[dire]))
        T = move_tail(H, T)
        visited[0].add(T[0])
        visited[1].add(T[-1])
    return H, T

def part_one_and_two():
    global visited
    H, T = (0, 0), [(0, 0)] * 9
    visited = [{(0, 0)}, {(0, 0)}]
    for move in dirs:
        H, T = move_head(move, H, T)
    print(f"Part One = {len(visited[0])}")
    print(f"Part Two = {len(visited[1])}")

dirs = open_file()

moves = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
adj = {(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)}

part_one_and_two()