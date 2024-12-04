import string

file = open("Day6inputs.txt")
inputs = file.read()
file.close()

inputs = inputs.split("\n\n")
groups = []
for qs in inputs:
    groups.append(qs.split("\n"))

alphabet = list(string.ascii_lowercase)

common = []
for group in groups:
    count = 0
    for letter in alphabet:
        countletter = 0
        for g in group:
            if letter in g:
                countletter += 1
        if countletter == len(group):
            count += 1
    common.append(count)

print(sum(common))
