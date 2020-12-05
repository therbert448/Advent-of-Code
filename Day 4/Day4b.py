file = open("Day4inputs.txt")
inputs = file.read()
file.close()

inputs = inputs.split("\n\n")

#print(inputs[0:10])

passports = []
for i in inputs:
    i = i.split()
    f = {}
    for j in range(0, len(i)):
        i[j] = i[j].split(":")
        f[i[j][0]] = i[j][1]
    passports.append(f)

del i, j, f

fields = ["byr",
          "iyr",
          "eyr",
          "hgt",
          "hcl",
          "ecl",
          "pid",
          "cid"]

count = 0
good = []
gpp = []
for p in passports:
    countfield = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(fields)):
        if fields[i] in p:
            countfield[i] = 1
    check = sum(countfield)
    if check == 8:
        count += 1
        good.append(1)
        gpp.append(p)
    elif check == 7 and countfield[-1] == 0:
        count += 1
        good.append(1)
        gpp.append(p)
    else:
        good.append(0)

del count, p, i


count = 0
goodvalid = []
gvpp = []

#print(gpp[0]["hgt"][-2:])

hcllist = ["0",
           "1",
           "2",
           "3",
           "4",
           "5",
           "6",
           "7",
           "8",
           "9",
           "a",
           "b",
           "c",
           "d",
           "e",
           "f"]

ecllist = ["amb",
           "blu",
           "brn",
           "gry",
           "grn",
           "hzl",
           "oth"]

for p in gpp:
    byr = int(p[fields[0]])
    if byr > 2002 or byr < 1920:
        goodvalid.append(0)
        continue
    iyr = int(p[fields[1]])
    if iyr > 2020 or iyr < 2010:
        goodvalid.append(0)
        continue
    eyr = int(p[fields[2]])
    if eyr > 2030 or eyr < 2020:
        goodvalid.append(0)
        continue
    hgt = p[fields[3]]
    if "in" in hgt or "cm" in hgt:
        unit = hgt[-2:]
        value = int(hgt[0: -2])
    else:
        goodvalid.append(0)
        continue
    if unit == "in" and (value > 76 or value < 59):
        goodvalid.append(0)
        continue
    elif unit == "cm" and (value > 193 or value < 150):
        goodvalid.append(0)
        continue
    hcl = p[fields[4]]
    if len(hcl) != 7 or hcl[0] != "#":
        goodvalid.append(0)
        continue
    flag = 0
    for i in range(1, len(hcl)):
        if hcl[i] in hcllist:
            continue
        else:
            goodvalid.append(0)
            flag = 1
            break
    if flag == 1:
        continue
    ecl = p[fields[5]]
    if ecl in ecllist:
        pass
    else:
        goodvalid.append(0)
        continue
    pid = p[fields[6]]
    if len(pid) != 9:
        goodvalid.append(0)
        continue
    try:
        pid = int(pid)
    except:
        goodvalid.append(0)
        continue
    count += 1
    goodvalid.append(1)
    gvpp.append(p)

print(count)
print(gvpp[0:3])




    
