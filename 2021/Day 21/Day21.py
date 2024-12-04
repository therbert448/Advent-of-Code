"""
Advent of Code
2021 Day 21

@author: Tom Herbert
"""
import time

t0 = time.time()

def play_game(die, maxScore):
    scores = [0, 0]
    pos = list(start)
    rolls = 0
    turn = 0
    while max(scores) < maxScore:
        move = sum([((rolls + i) % die) + 1 for i in range(3)])
        pos[turn] = ((pos[turn] + move - 1) % 10) + 1
        scores[turn] += pos[turn]
        rolls += 3
        turn = 1 - turn
    result = min(scores) * rolls
    return result

def dirac(moveDistribution):
    playersPos = [{(start[0], 0): 1}, {(start[1], 0): 1}]
    playersWon = [0, 0]
    allOver = False
    turn = 0
    while not allOver:
        newPos = {}
        universes = sum(playersPos[1-turn].values())
        for posScore, freq in playersPos[turn].items():
            for move, count in moveDistribution.items():
                pos, score = posScore
                nextPos = ((pos + move - 1) % 10) + 1
                nextScore = score + nextPos
                if nextScore >= 21:
                    playersWon[turn] += freq * count * universes
                    continue
                if (nextPos, nextScore) not in newPos:
                    newPos[(nextPos, nextScore)] = freq * count
                else:
                    newPos[(nextPos, nextScore)] += freq * count
        if not newPos:
            allOver = True
        else:
            playersPos[turn] = dict(newPos)
        turn = 1 - turn
    return max(playersWon)

def part_one():
    die, maxScore = 100, 1000
    result = play_game(die, maxScore)
    print(f"Part One = {result}")

def part_two():
    moveDistribution = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    #27 possible rolls (3x 3 sided dice), sums of rolls distributed as above 
    result = dirac(moveDistribution)
    print(f"Part Two = {result}")

day = 21

start = [4, 3]

part_one()
t1 = time.time()
part_two()
t2 = time.time()

print(f"Part One takes {round(t1-t0, 3)} seconds")
print(f"Part Two takes {round(t2-t1, 3)} seconds")
print(f"Total Time = {round(t2-t0, 3)} seconds")