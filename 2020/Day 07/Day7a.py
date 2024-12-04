file = open("Day7inputs.txt")
inputs = file.readlines()
file.close()

def findouter(colour, ruledict):
    newcol = set(colour)
    for outerbag in ruledict:
        for innerbag in ruledict[outerbag]:
            for col in colour:
                if col in innerbag:
                    newcol.add(outerbag)
    if len(newcol) != len(colour):
        newcol = findouter(newcol, ruledict)
    return newcol

ruledict = {}
for line in inputs:
    rule = line.split(" contain ")
    out = rule[0].replace(" bags", "")
    inn = rule[1].replace(" bags.", "").replace(" bag.", "")
    inn = inn.replace(" bag, ", ";").replace(" bags, ", ";")
    inn = inn.strip()
    inn = inn.split(";")
    for i in range(0, len(inn)):
        if len(inn) == 1 and inn[i] == "no other":
            inn[i] = [0, ""]
        else:
            x = inn[i].find(" ")
            num = int(inn[i][0:x])
            bag = inn[i][x+1:]
            inn[i] = [num, bag]
    ruledict[out] = inn

colour = {"shiny gold"}

newcol = findouter(colour, ruledict)

print(len(newcol)-1)
