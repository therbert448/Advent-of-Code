class Node:
    def __init__(self, pos, size, used, avail, usepc):
        self.pos = pos
        self.size = size
        self.used = used
        self.avail = avail
        self.usepc = usepc
    
    def viable_pair(self, other):
        if self.pos == other.pos:
            return False
        if self.used == 0:
            return False
        if self.used > other.avail:
            return False
        return True

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()[2:]]
    file.close()

def format_data():
    global nodes, x, y
    nodes = {}
    for line in inputs:
        line = line.split()
        _, x, y = line[0].split("-")
        x, y = [int(x[1:]), int(y[1:])]
        size = int(line[1][:-1])
        used = int(line[2][:-1])
        avail = int(line[3][:-1])
        usepc = int(line[4][:-1])
        pos = (x, y)
        nodes[pos] = Node(pos, size, used, avail, usepc)

def viable_pairs():
    global pairs
    pairs = set()
    for nodeA in nodes:
        A = nodes[nodeA]
        for nodeB in nodes:
            B = nodes[nodeB]
            if A.viable_pair(B):
                pairs.add((A, B))
    print(f"Part One: {len(pairs)}")

def print_grid():
    global string
    string = ""
    for i in range(y+1):
        for j in range(x+1):
            pos = (j, i)
            used = str(nodes[pos].used)
            size = str(nodes[pos].size)
            string += used + "/" + size + "\t"
        string += "\n"
    #part two is easiest just by looking at the grid of nodes
    #find the node with 0 used, then find the path to the top right corner
    #there is a wall of nodes with unshiftable data to avoid
    #easier to do this visually rather than through code
    #then calculate the number of steps
    empty = (3, 20)
    stepstopleft = sum(empty)
    #the "wall" forces me to go along the left edge of the grid, so may as well
    #count the steps to the top left corner (which will be my goal later)
    stepstopright = stepstopleft + x
    #moving from the top left to top right is simply x steps (x is the length
    #of the row - 1)
    stepsback = stepstopright + (5 * (x-1))
    #to move the relevant data forward one step requires 5 steps (see example)
    #getting the empty space to the top right corner moved the data one step
    #already, so only x-1 steps left for the data to move
    print(f"Part Two: {stepsback}")

day = 22
open_file()

format_data()

viable_pairs()
print_grid()