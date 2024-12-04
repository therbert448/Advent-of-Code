"""
Advent of Code
2022 Day 7

@author: Tom Herbert
"""

day = 7

class Directory:
    def __init__(self, currentPath):
        self.path = "/".join(currentPath)
        self.total = 0
    
    def add_files(self, files):
        self.files = {name: size for [size, name] in files}
    
    def add_directories(self, dirs):
        self.dirs = ["/".join([self.path, name]) for name in dirs]
    
    def find_size(self):
        if self.total:
            return self.total
        fileSizes = sum(self.files.values())
        dirSizes = sum(directories[dire].find_size() for dire in self.dirs)
        self.total = fileSizes + dirSizes
        return self.total

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = file.read()
    return inputs

def format_data():
    global directories
    directories = {}
    currentPath = []
    for line in inputs.strip("$ ").split("$"):
        path = "/".join(currentPath)
        line = line.strip().split("\n")
        if len(line) == 1:
            nextDir = line[0].split(" ")[1]
            if nextDir == "..":
                currentPath.pop()
            else:
                currentPath.append(nextDir)
                path = "/".join(currentPath)
                if path not in directories:
                    directories[path] = Directory(currentPath)
        else:
            files, dirs = [], []
            for content in line[1:]:
                typeSize, name = content.split(" ")
                if typeSize.isnumeric():
                    files.append([int(typeSize), name])
                else:
                    dirs.append(name)
                    newPath = "/".join([path, name])
                    if newPath not in directories:
                        directories[newPath] = Directory([*currentPath, name])
            directories[path].add_files(files)
            directories[path].add_directories(dirs)

def part_one():
    dirSizes = [dire.find_size() for dire in directories.values()]
    result = sum(v for v in dirSizes if v <= 100_000)
    print(f"Part One = {result}")

def part_two():
    totalSize = directories["/"].total
    toDelete = abs(40_000_000 - totalSize)
    dirSizes = [dire.total for dire in directories.values()]
    deleted = min(v for v in dirSizes if v >= toDelete)
    print(f"Part Two = {deleted}")

inputs = open_file()

format_data()

part_one()
part_two()