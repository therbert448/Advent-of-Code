def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global trianglesone, trianglestwo
    trianglesone = [] # valid triangles for part one
    trianglestwo = [] # valid triangles for part two
    cols = [[], [], []]
    for row, line in enumerate(inputs):
        line = line.split()
        tri = [int(i) for i in line]
        sortedtri = sorted(tri)
        a, b, c = sortedtri
        d, e, f = tri
        if row % 3 != 2:
            [cols[0].append(d), cols[1].append(e), cols[2].append(f)]
        else:
            for side, col in enumerate(cols):
                d, e = col
                f = tri[side]
                newtri = sorted([i for i in [d, e, f]])
                d, e, f = newtri
                if d + e > f:
                    trianglestwo.append(newtri)
            cols = [[], [], []]
        if a + b > c:
            trianglesone.append(sortedtri)
    print(f"Part One: {len(trianglesone)}")
    print(f"Part One: {len(trianglestwo)}")

day = 3
open_file()

format_data()