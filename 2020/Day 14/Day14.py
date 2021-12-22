def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global program
    program = []
    for line in inputs:
        line = line.strip().split(" = ")
        if line[0] == "mask":
            mask = []
            for bit in line[1]:
                mask.append(bit)
            d = {line[0] : mask}
        else:
            address = int(line[0][3:].strip("[]"))
            value = int(line[1])
            d = [address, value]
        program.append(d)
    return

def part_one():
    mem = {}
    for line in program:
        if "mask" in line:
            mask = line["mask"]
        else:
            address = line[0]
            binary = bin(line[1])[2:]
            length = len(binary)
            brev = binary[::-1]
            blistr = [b for b in brev]
            maskrev = mask[::-1]
            for i in range(len(maskrev)):
                if i < length:
                    if maskrev[i] == "X":
                        continue
                    else:
                        bit = maskrev[i]
                        blistr[i] = bit
                else:
                    blistr.append("0")
                    if maskrev[i] == "1":
                        blistr[i] = "1"
            blist = blistr[::-1]       
            bstr = ""
            for b in blist:
                bstr = bstr + b
            decval = int(bstr, 2)
            mem[address] = decval
    summem = sum(mem.values())
    return summem

def part_two():
    mem = {}
    for line in program:
        if "mask" in line:
            mask = line["mask"]
            mask = [m.replace("0", "Y") for m in mask]
            countx = mask.count("X")
            nummasks = 2 ** countx
            masks = []
            for i in range(nummasks):
                m = list(mask)
                ibin = [ib for ib in bin(i)[2:]]
                leni = len(ibin)
                for j in range(countx):
                    k = countx - j - 1
                    idx = m.index("X")
                    if k >= leni:
                        m[idx] = "0"
                    else:
                        l = leni - k - 1
                        m[idx] = ibin[l]
                masks.append(m)
        else:
            address = line[0]
            binfix = bin(address)[2:]
            val = line[1]
            length = len(binfix)
            for mask in masks:
                brev = binfix[::-1]
                blistr = [b for b in brev]
                maskrev = mask[::-1]
                for i in range(len(maskrev)):
                    if i < length:
                        if maskrev[i] == "Y":
                            continue
                        else:
                            bit = maskrev[i]
                            blistr[i] = bit
                    else:
                        blistr.append("0")
                        if maskrev[i] == "1":
                            blistr[i] = "1"
                blist = blistr[::-1]       
                bstr = ""
                for b in blist:
                    bstr = bstr + b
                decval = int(bstr, 2)
                mem[decval] = val
    summem = sum(mem.values())
    return summem

day = 14
inputs = open_file()

formatdata(inputs)

print(part_one())
print(part_two())

