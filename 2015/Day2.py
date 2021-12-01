def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def wrapping_paper_ribbon():
    totalpaper = 0
    totalribbon = 0
    for line in inputs:
        l, w, h = line.split("x")
        l, w, h = [int(l), int(w), int(h)]
        areas = [l*w, w*h, h*l]
        perims = [2*l + 2*w, 2*w + 2*h, 2*h + 2*l]
        vol = l*w*h
        paper = 2 * sum(areas) + min(areas)
        ribbon = min(perims) + vol
        totalpaper += paper
        totalribbon += ribbon
    print(f"Part One: {totalpaper}")
    print(f"Part Two: {totalribbon}")

day = 2
open_file()

wrapping_paper_ribbon()