def open_file():
    file = open("Day" + str(day) + "inputsb.txt")
    inputs = file.read().strip()
    file.close()
    return inputs

def formatdata(rs):
    global rules
    global messages
    rules = {}
    rs = rs.split("\n")
    for line in rs:
        l = line.split(": ")
        l[1] = l[1].split(" | ")
        for i in range(len(l[1])):
            l[1][i] = l[1][i].split(" ")
        rules[l[0]] = l[1]
            
    messages = messages.split("\n")

def add_strings(aset, bset):
    cset = set()
    for a in aset:
        for b in bset:
            c = a + b
            cset.add(c)
    return cset
    
def correct_str(ruleno):
    rule = rules[ruleno]
    orset = set()
    for r in rule:
        strlist = []
        for rn in r:
            if rn not in ('"a"', '"b"'):
                strlist.append(correct_str(rn))
            else:
                char = rn.strip("\"")
                return char
        join = strlist[0]
        for s in strlist[1:]:
            join = add_strings(join, s)
        for j in join:
            orset.add(j)
    return orset

def check_messages(ruleno):
    strings = correct_str(ruleno)
    count = 0
    for mess in messages:
        if mess in strings:
            count += 1
    print(count)
    return strings

def part_two(): #Work through the messages given the input pattern
    a = "42"
    aset = list(correct_str(a))
    b = "31"
    bset = list(correct_str(b))
    newmes = list(messages)
    for m in messages:
        if len(m) % 8 != 0:
            newmes.remove(m)
            continue
        substrs = len(m)//8
        ms = []
        for i in range(substrs): 
            ms.append(m[i*8 : i*8 + 8])
        maxb = substrs - substrs//2 - 1
        if ms[-1] not in bset:
            newmes.remove(m)
            continue
        count = 1
        for j in range(1, maxb):
            if ms[-j] not in bset:
                break
            else:
                count += 1
        for i in range(substrs - count):
            if ms[i] not in aset:
                newmes.remove(m)
                break
    print(len(newmes))

day = 19
rs, messages = open_file().split("\n\n")

formatdata(rs)
#check_messages("0") #Part one for use with unaltered inputs (Day19inputs.txt)
part_two() #Runs with Day19inputsb.txt
