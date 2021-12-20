"""
Advent of Code
2021 Day 20

@author: Tom Herbert
"""

class Image:
    def __init__(self, grid, highlight = "#", infinite = "."):
        self.grid = set(grid)
        self.highlight = highlight
        self.infinite = infinite
        self.bounds()

    def bounds(self):
        self.xmin, self.xmax, self.ymin, self.ymax = [None] * 4
        for coords in self.grid:
            x, y = coords
            if self.xmin == None or x < self.xmin:
                self.xmin = x
            if self.xmax == None or x > self.xmax:
                self.xmax = x
            if self.ymin == None or y < self.ymin:
                self.ymin = y
            if self.ymax == None or y > self.ymax:
                self.ymax = y

    def translate(self, pos):
        x, y = pos
        binary = ""
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if (x+dx, y+dy) in self.grid:
                    if self.highlight == "#":
                        binary += "1"
                    else:
                        binary += "0"
                else:
                    if self.highlight == "#":
                        binary += "0"
                    else:
                        binary += "1"
        return int(binary, 2)

    def process_image(self):
        newGrid = set()
        if self.infinite == "." and translation[0] != ".":
            newHighlight = "."
            newInfinite = "#"
        elif self.infinite == "#" and translation[-1] == "#":
            newHighlight = "."
            newInfinite = "#"
        else:
            newHighlight = "#"
            newInfinite = "."
        for x in range(self.xmin-1, self.xmax+2):
            for y in range(self.ymin-1, self.ymax+2):
                pos = (x, y)
                idx = self.translate(pos)
                char = translation[idx]
                if char == newHighlight:
                    newGrid.add(pos)
        newImage = Image(newGrid, newHighlight, newInfinite)
        return newImage

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [part.strip() for part in file.read().split("\n\n")]
    file.close()
    return inputs

def format_data():
    global image, translation
    translation, grid = inputs
    coords = set()
    for y, line in enumerate(grid.splitlines()):
        for x, char in enumerate(line.strip()):
            if char == "#":
                coords.add((x, y))
    image = Image(coords)

def part_one():
    newImage = image
    for step in range(2):
        newImage = newImage.process_image()
    if newImage.highlight == "#":
        print(f"Part One = {len(newImage.grid)}")
    else:
        print("Infinite Pixels!")

def part_two():
    newImage = image
    for step in range(50):
        newImage = newImage.process_image()
    if newImage.highlight == "#":
        print(f"Part Two = {len(newImage.grid)}")
    else:
        print("Infinite Pixels!")

day = 20
inputs = open_file()

format_data()

part_one()
part_two()