file = open("Day5inputs.txt")
inputs = file.readlines()
file.close()

ones = ["B", "R"]
zeros = ["F", "L"]

ids = []
for bpass in inputs:
    bpass = bpass.strip()
    binary = ""
    for letter in bpass:
        if letter in ones:
            binary = binary + "1"
        elif letter in zeros:
            binary = binary + "0"

    row = int(binary[0:7], 2)
    col = int(binary[7:], 2)
    seatID = (row * 8) + col
    ids.append(seatID)

print(max(ids))

for ticket in ids:
    if ticket == min(ids) or ticket == max(ids):
        continue
    if ticket + 1 in ids and ticket - 1 in ids:
        continue
    elif ticket + 1 not in ids:
        minid = ticket
    elif ticket - 1 not in ids:
        maxid = ticket

mytick = minid + 1

print(minid, mytick, maxid)
