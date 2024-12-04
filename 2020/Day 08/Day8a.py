file = open("Day8inputs.txt")
inputs = file.readlines()
file.close()

instructs = []
for line in inputs:
    sep = line.strip().split(" ")
    sep[1] = int(sep[1])
    instructs.append(sep)

pointer = 0
pos = [pointer]
acc = 0
flag = 0

while flag == 0:
    op = instructs[pointer][0]
    arg = instructs[pointer][1]
    if op == "acc":
        acc += arg
        pointer += 1
    elif op == "jmp":
        pointer += arg
    elif op == "nop":
        pointer += 1
    else:
        flag = 1
        print("Format incorrect")
    if pointer in pos:
        flag = 1
    else:
        pos.append(pointer)

print(acc)

