file = open("Day7inputs.txt")
inputs = file.readlines()
file.close()

def numberofbags(bag, ruledict):
    total = 0
    innerbags = ruledict[bag]
    if len(innerbags) == 1 and innerbags[0][1] == "":
        return 0
    else:
        for b in innerbags:
            count = b[0] + b[0] * numberofbags(b[1], ruledict)
            total += count
        return total
    
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

bag = "shiny gold"

totalbags = numberofbags(bag, ruledict)

print(totalbags)

