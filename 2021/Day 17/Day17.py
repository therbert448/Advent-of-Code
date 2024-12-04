"""
Advent of Code
2021 Day 17

@author: Tom Herbert
"""

day = 17

xmin, xmax = [32, 65]
ymin, ymax = [-225, -177]

def part_one():
    velMaxY = abs(ymin) - 1
    disMaxY = velMaxY*(velMaxY+1)//2
    print(f"Part One = {disMaxY}")

def part_two():
    speeds = set()
    minxv = int(pow(2*xmin, 0.5))
    maxxv = xmax
    nMax = 2*abs(ymin)
    for n in range(nMax):
        n += 1
        for y in range(ymin, abs(ymin)):
            if n < y:
                dispy = y*(y+1)//2 - (y-n)*(y-n+1)//2
            else:
                dispy = y*(y+1)//2 - (n-y-1)*(n-y)//2
            if dispy < ymin or dispy > ymax:
                continue
            for x in range(minxv, maxxv+1):
                if n < x:
                    dispx = x*(x+1)//2 - (x-n)*(x-n+1)//2
                else:
                    dispx = x*(x+1)//2
                if dispx < xmin or dispx > xmax:
                    continue
                speeds.add((x, y))
    print(f"Part Two = {len(speeds)}")

part_one()
part_two()