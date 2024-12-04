file = open("Day1inputs.txt")
inputs = file.readlines()
file.close()

for i in range(0, len(inputs)):
    inputs[i] = int(inputs[i])
del i

for i in range(0, len(inputs)):
    for j in range(i, len(inputs)):
        if i == j:
            continue
        for k in range(j, len(inputs)):
            if j == k:
                continue
            else:
                add = inputs[i] + inputs[j] + inputs[k]
                if add == 2020:
                    print(inputs[i])
                    print(inputs[j])
                    print(inputs[k])
                    product = inputs[i] * inputs[j] * inputs[k]
                    print(product)
