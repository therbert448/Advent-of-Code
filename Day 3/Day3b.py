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

slopes = [[1, 1],
          [3, 1],
          [5, 1],
          [7, 1],
          [1, 2]]

counts = []
for i in range(0, len(slopes)):
    count = 0
    col = 0
    row = 0
    for j in range(0, maxrows-1):
        col = (col + slopes[i][0]) % 31
        row += slopes[i][1]
        if row > maxrows-1:
            break
        if inputs[row][col] == "#":
            count += 1
    counts.append(count)

print(counts)

product = 1
for c in counts:
    product = product * c

print(product)
