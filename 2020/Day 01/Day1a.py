file = open("Day1inputs.txt")
inputs = file.readlines()
file.close()

for i in range(0, len(inputs)):
    inputs[i] = int(inputs[i])
del i

for i in range(0, len(inputs)):
    for j in range(0, len(inputs)):
        if i == j:
            continue
        else:
            add = inputs[i] + inputs[j]
            if add == 2020:
                print(inputs[i])
                print(inputs[j])
                product = inputs[i] * inputs[j]
                print(product)
