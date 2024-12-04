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
            binary = binary.zfill(36)
            blist = list(binary)
            for i in range(len(mask)):
                if mask[i] != "X":
                    blist[i] = mask[i]     
            bstr = "".join(blist)
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
                ibin = list(bin(i)[2:].zfill(countx))
                for j in range(countx):
                    idx = m.index("X")
                    m[idx] = ibin[j]
                masks.append(m)
        else:
            address = line[0]
            binary = bin(address)[2:].zfill(36)
            val = line[1]
            for mask in masks:
                blist = list(binary)
                for i in range(len(mask)):
                    if mask[i] != "Y":
                        blist[i] = mask[i]       
                bstr = "".join(blist)
                decval = int(bstr, 2)
                mem[decval] = val
    summem = sum(mem.values())
    return summem

day = 14
inputs = open_file()

formatdata(inputs)

print(part_one())
print(part_two())


