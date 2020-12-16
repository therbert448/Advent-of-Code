def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().split("\n\n")
    file.close()
    return inputs

def formatdata(inputs):
    global rules #first part of inputs containing rules
    global myticket #my ticket values
    global tix #values from tickets near me
    global listranges #list of the range pairs from the rules
    rules = {}
    tix = []
    listranges = []
    #format rules
    r = inputs[0].splitlines()
    for line in r:
        rspl = line.split(": ")
        field = rspl[0]
        ranges = rspl[1].split(" or ")
        for idx, ran in enumerate(ranges):
            ranges[idx] = ran.split("-")
            ranges[idx] = [int(val) for val in ranges[idx]]
        rules[field] = ranges
    for val in rules.values():
        for pair in val:
            listranges.append(pair)
    #format my ticket        
    mt = inputs[1].splitlines()[1].split(",")
    myticket = [int(field) for field in mt]
    #format all other tickets
    for line in inputs[2].splitlines()[1:]:
        linelist = [int(val) for val in line.split(",")]
        tix.append(linelist)
    return

def count_fields(fields, tixlen):
    #count how many fields the ith number on a ticket is valid for
    fieldcount = []
    for i in range(tixlen):
        count = 0
        for f in fields:
            if i in fields[f]:
                count += 1
        fieldcount.append(count)
    return fieldcount

def count_possible(fields):
    #count how many values on a ticket could belong to a given field
    poscount = []
    for f in fields:
        poscount.append(len(fields[f]))
    return poscount
        
def part_one():
    sumerr = 0
    idxset = set()
    for idx, ticket in enumerate(tix):
        for val in ticket:
            good = 0
            for pair in listranges:
                if val in range(pair[0], pair[1]+1):
                    good = 1
                    break
            if good == 0:
                sumerr += val
                idxset.add(idx)
    idxes = sorted(idxset)[::-1]
    newtix = list(tix)
    for i in idxes:
        del newtix[i] 
    return sumerr, newtix

def part_two(newtix):
    fields = {} #stores every possible ticket value index for a given field
    tixlen = len(myticket)
    for f in rules:
        fields[f] = [i for i in range(tixlen)]
        for ticket in newtix:
            for i, val in enumerate(ticket):
                if i not in fields[f]:
                    continue
                good = 0
                for pair in rules[f]:
                    if val in range(pair[0], pair[1]+1):
                        good = 1
                        break
                if good == 0:
                    fields[f].remove(i)

    fieldcount = count_fields(fields, tixlen)
    poscount = count_possible(fields)
    fkeys = list(fields.keys())
    correctfields = {} #new dict to store the correct ticket to field mapping
    while not all([c == 0 for c in fieldcount]):
        if 1 in poscount: 
            #if a field can only be 1 value on the ticket, it must be that
            field = fkeys[poscount.index(1)]
            idx = fields[field][0]
            correctfields[field] = [idx]
            fields.pop(field) #remove confirmed field
            for f in fields:
                if idx in fields[f]:
                    fields[f].remove(idx) 
                    #remove all other occurances of the value
        elif 1 in fieldcount:
            #if a value on the ticket only matches one field, it must be that
            idx = fieldcount.index(1)
            for f in fields:
                if idx in fields[f]:
                    field = f
            correctfields[field] = [idx]
            fields.pop(field) #remove confirmed field
        else:
            break
        fieldcount = count_fields(fields, tixlen)
        poscount = count_possible(fields)
        #update counts for next iteration
        fkeys = list(fields.keys())              

    mytickdict = {}
    for f in correctfields:
        mytickdict[f] = myticket[correctfields[f][0]]
    
    proddep = 1
    string = "departure"
    for f in mytickdict:
        if string in f:
            proddep *= mytickdict[f]
            
    return proddep      

day = 16
inputs = open_file()

formatdata(inputs)

sumerr, newtix = part_one()
print(sumerr)
proddep = part_two(newtix)
print(proddep)