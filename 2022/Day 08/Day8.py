"""
Advent of Code
2022 Day 8

@author: Tom Herbert
"""

day = 8

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [[int(v) for v in l.strip()] for l in file.readlines()]
    return inputs

def check_visible():
    visible = set()
    length, width = len(inputs), len(inputs[0])
    for l in range(length):
        for w in range(width):
            coords = (w, l)
            if w in (0, width-1) or l in (0, length-1):
                visible.add(coords)
            else:
                value = inputs[l][w]
                left = inputs[l][:w]
                right = inputs[l][w+1:]
                top = [inputs[i][w] for i in range(l)]
                bottom = [inputs[i][w] for i in range(l+1, length)]
                if value > min(map(max, [left, right, top, bottom])):
                    visible.add(coords)
    return visible

def scenic_score():
    scores = {}
    length, width = len(inputs), len(inputs[0])
    for l in range(length):
        for w in range(width):
            coords = (w, l)
            if w in (0, width-1) or l in (0, length-1):
                scores[coords] = 0
                continue
            value = inputs[l][w]
            maxScores = [w, width - w - 1, l, length - l - 1]
            left = inputs[l][w-1::-1]
            right = inputs[l][w+1:]
            top = [inputs[i][w] for i in range(l-1, -1 ,-1)]
            bottom = [inputs[i][w] for i in range(l+1, length)]
            slices = [left, right, top, bottom]
            score = 1
            for i, row in enumerate(slices):
                for j, tree in enumerate(row):
                    if tree >= value:
                        maxScores[i] = j+1
                        break
            score = 1
            for sco in maxScores:
                score *= sco
            scores[coords] = score
    return scores

def part_one():
    visible = check_visible()
    print(f"Part One = {len(visible)}")

def part_two():
    scores = scenic_score()
    print(f"Part Two = {max(scores.values())}")

inputs = open_file()

part_one()
part_two()