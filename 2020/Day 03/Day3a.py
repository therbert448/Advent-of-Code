file = open("Day3inputs.txt")
inputs = file.readlines()
file.close()

lengths = []
for i in range(0, len(inputs)):
    inputs[i] = inputs[i].strip()
    row = []
    lengths.append(len(inputs[i]))
    for j in range(0, len(inputs[i])):
        row.append(inputs[i][j])
    inputs[i] = row
    
del row, i

length = j + 1
maxrows = len(inputs)

col = 0
row = 0

count = 0
for i in range(0, maxrows-1):
    col = (col + 3) % 31
    row += 1
    if inputs[row][col] == "#":
        count += 1

print(count)
    
