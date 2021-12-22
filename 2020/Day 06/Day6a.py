import string

file = open("Day6inputs.txt")
inputs = file.read()
file.close()

inputs = inputs.split("\n\n")

alphabet = list(string.ascii_lowercase)

groupqs = []
for group in inputs:
    count = 0
    for letter in alphabet:
        if letter in group:
            count += 1
    groupqs.append(count)

print(sum(groupqs))
