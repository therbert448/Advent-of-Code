def formatdata(inputs):
    global pwrange
    pwrange = [int(val) for val in inputs.split("-")] 

  
def part_one():
    valid = []
    for i in range(pwrange[0], pwrange[1]+1):
        valstr = [val for val in str(i)]
        check1 = False
        check2 = False
        for j, char in enumerate(valstr):
            if j == 0:
                continue
            if char < valstr[j-1]:
                check1 = False
                break
            else:
                check1 = True
            if char == valstr[j-1]:
                check2 = True
        if check1 and check2:
            valid.append(i)
    return len(valid)

def part_two():
    valid = []
    for i in range(pwrange[0], pwrange[1]+1):
        valstr = [val for val in str(i)]
        check1 = False
        check2 = False
        strl = len(valstr)
        for j in range(1, strl):
            if valstr[j] < valstr[j-1]:
                check1 = False
                break
            else:
                check1 = True
            if valstr[j] == valstr[j-1] and valstr[j] == valstr[j-2]:
                continue
            elif valstr[j] == valstr[j-1] and valstr[j] != valstr[(j+1)%strl]:
                check2 = True
        if check1 and check2:
            valid.append(i)
    return len(valid)

inputs = "246515-739105"

formatdata(inputs)
print(part_one())
print(part_two())