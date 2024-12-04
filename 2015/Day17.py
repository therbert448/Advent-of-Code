def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global containers
    containers = [int(line.strip()) for line in file.readlines()]
    file.close()

def cont_combs(eggnogleft, contsleft, count):
    combcount = 0
    if eggnogleft in contsleft:
        combcount += contsleft.count(eggnogleft)
        count += 1
        if count not in contcount:
            contcount[count] = combcount
        else:
            contcount[count] += combcount
        count -= 1
    newcontsleft = list(contsleft)
    count += 1
    for cont in contsleft:
        newcontsleft.remove(cont)
        neweggnogleft = eggnogleft - cont
        combcount += cont_combs(neweggnogleft, newcontsleft, count)
    return combcount

def fill_containers():
    count = 0
    combcount = cont_combs(eggnog, containers, count)
    print(f"Part One: {combcount}")
    for k, v in contcount.items():
        if k == min(contcount.keys()):
            print(f"Part Two: {v}")

day = 17
open_file()

eggnog = 150

contcount = {}

fill_containers()