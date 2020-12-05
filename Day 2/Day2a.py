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
for i in range(0, len(inputs)):
    minc = int(inputs[i][0][0])
    maxc = int(inputs[i][0][1])
    char = inputs[i][1]
    string = inputs[i][2]
    count = 0
    for letter in string:
        if letter == char:
            count += 1
    if count <= maxc and count >= minc:
        good.append(1)
    else:
        good.append(0)

del i, count

count = 0

gpw = []

for i in range(0, len(passwords)):
    if good[i] == 1:
        count += 1
        gpw.append(passwords[i])
        #print(passwords[i])

print(gpw[0:10])
print(count)
