import math as maths

class Reaction:
    def __init__(self, out, ing):
        self.produces = out[0]
        self.chem = out[1]
        self.ings = list(ing)
        self.needed = 0
        self.total = 0
        self.count = 0

def open_file():
    #file = open("test.txt")
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global reacts
    reacts = {}
    for line in inputs:
        ing, out = line.strip().split(" => ")
        ing = ing.split(", ")
        for i, x in enumerate(ing):
            ing[i] = x.split(" ")
            ing[i][0] = int(ing[i][0])
        out = out.split(" ")
        out[0] = int(out[0])
        reacts[out[1]] = Reaction(out, ing)
    reacts["ORE"] = 0
    reacts["FUEL"].needed = 1

def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x, y)
    return lcm

def calc_needed(fuel):
    reaction = reacts[fuel]
    needed = reaction.needed
    prod = reaction.produces
    numreacts = maths.ceil(needed/prod)
    created = numreacts * prod
    reaction.needed -= created
    reaction.total += created
    reaction.count += numreacts
    for i in reaction.ings:
        if i[1] == "ORE":
            reacts["ORE"] += i[0] * numreacts
            return
        else:
            nextreact = reacts[i[1]]
            nextreact.needed += i[0] * numreacts
            calc_needed(i[1])
    return

def part_two():
    n = 1_000_000_000_000
    minfuel = int(n/reacts["ORE"]) #theoretical min fuel
    formatdata(inputs)
    reacts["FUEL"].needed = minfuel
    calc_needed("FUEL")
    perc = reacts["ORE"]/n #ore used for min fuel is what % of 1 trillion?
    print("Answer to Part Two =", int(minfuel/perc))
    #Divide min fuel by % of a trillion ores for the answer
# ** Works because the value of "minfuel" is sufficiently large compared to
#    the original 1 unit of fuel that the contributions of all the remainders
#    of all the ingredients are sufficiently evened out. The rounding of the
#    non integers filters this small error out **

day = 14
inputs = open_file()

formatdata(inputs)

calc_needed("FUEL")
print("Answer to Part One =", reacts["ORE"])
part_two()