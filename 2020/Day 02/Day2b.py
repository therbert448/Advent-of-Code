file = open("Day2inputs.txt")
inputs = file.readlines()
file.close()
passwords = list(inputs)

for i in range(0, len(inputs)):
    inputs[i] = inputs[i].strip()
    passwords[i] = passwords[i].strip()
    inputs[i] = inputs[i].split(" ")
    inputs[i][0] = inputs[i][0].split("-")
    inputs[i][1] = inputs[i][1].strip(":")

del i

good = []
count = 0
for i in range(0, len(inputs)):
    pos1 = int(inputs[i][0][0]) - 1
    pos2 = int(inputs[i][0][1]) - 1
    char = inputs[i][1]
    string = inputs[i][2].strip()
    if i == 1:
        print(int(inputs[i][0][0]), pos1)
        print(int(inputs[i][0][1]), pos2)
        print(char)
        print(string)
        print(string[pos1])
        print(string[pos2])
    if string[pos1] == char:
        a = 1
    else:
        a = 0
    if string[pos2] == char:
        b = 1
    else:
        b = 0
    if a == b:
        good.append(0)
    else:
        count += 1
        good.append(1)
print(count)

del i

gpw = []

for i in range(0, len(passwords)):
    if good[i] == 1:
        gpw.append(passwords[i])
        #print(passwords[i])

print(inputs[0:10])
print(passwords[0:10])
print(gpw[0:10])
