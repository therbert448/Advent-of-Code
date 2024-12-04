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

print(count)
