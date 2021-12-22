def open_file(day):
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global code
    code = [int(i.strip()) for i in inputs]

def find_first_wrong():
    prelen = 25
    n = len(code) - prelen
    codelist = list(code)
    for i in range(0, n):
        preamble = set(codelist[0:prelen])
        checkval = codelist[prelen]
        good = 0
        for a in preamble:
            b = checkval - a
            if b in preamble and b != a:
                good = 1
                break
        if good != 1:
            return checkval
        del codelist[0]
    return "End of Code"

def find_weakness(invalid):
    idx = code.index(invalid)
    for i in range(0, idx - 2):
        maxlen = idx - i
        for j in range(2, maxlen):
            sublist = code[i:i+j]
            subsum = sum(sublist)
            if subsum == invalid:
                weakness = min(sublist) + max(sublist)
                return weakness
    return "All sets checked"

day = 9
inputs = open_file(day)

formatdata(inputs)

invalid = find_first_wrong()
weakness = find_weakness(invalid)

print(invalid)
print(weakness)
