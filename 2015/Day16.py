class Sue:
    def __init__(self, compounds):
        self.compounds = compounds

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global sues
    sues = {}
    for line in inputs:
        _, num, *rest = line.split(" ")
        num = int(num[:-1])
        rest = "{" + " ".join(rest) + "}"
        compounds = eval(rest)
        sue = Sue(compounds)
        sues[num] = sue

def find_sue():
    for num, sue in sues.items():
        rightsue = 1
        for comp, val in MFCSAMout.items():
            if comp not in sue.compounds:
                continue
            elif val != sue.compounds[comp]:
                rightsue = 0
                break
        if rightsue:
            print(f"Part One: {num}")
            break

def find_real_sue():
    for num, sue in sues.items():
        rightsue = 1
        for comp, val in MFCSAMout.items():
            if comp not in sue.compounds:
                continue
            elif comp == "cats" or comp == "trees":
                if sue.compounds[comp] <= val:
                    rightsue = 0
                    break
            elif comp == "pomeranians" or comp == "goldfish":
                if sue.compounds[comp] >= val:
                    rightsue = 0
                    break
            elif val != sue.compounds[comp]:
                rightsue = 0
                break
        if rightsue:
            print(f"Part Two: {num}")
            break

children = "children"
cats = "cats"
samoyeds = "samoyeds"
pomeranians = "pomeranians"
akitas = "akitas"
vizslas = "vizslas"
goldfish = "goldfish"
trees = "trees"
cars = "cars"
perfumes = "perfumes"

MFCSAMout = {children: 3,
             cats: 7,
             samoyeds: 2,
             pomeranians: 3,
             akitas: 0,
             vizslas: 0,
             goldfish: 5,
             trees: 3,
             cars: 2,
             perfumes: 1}

day = 16
open_file()

format_data()

find_sue()
find_real_sue()