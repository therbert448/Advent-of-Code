def factors(num):
    half = num//2
    triangle = num + ((half * (half+1))//2)
    if triangle < presents//10:
        return 0
    search = int(num**0.5)
    factset = {num}
    for i in range(1, search + 1):
        if num % i == 0:
            div = num//i
            factset.add(i)
            factset.add(div)
    presentcount = sum(factset) * 10
    return presentcount

def factors2(num):
    half = num//2
    triangle = num + ((half * (half+1))//2)
    if triangle < presents//11:
        return 0
    search = int(num**0.5)
    factset = {num}
    for i in range(1, search + 1):
        if num % i == 0:
            div = num//i
            if num <= i * 50:
                factset.add(i)
            if num <= div * 50:
                factset.add(div)
    presentcount = sum(factset) * 11
    return presentcount

def deliver_presents():
    global house
    house = 1
    delivered = 0
    while not delivered:
        numdelivered = factors(house)
        if numdelivered >= presents:
            delivered = 1
            break
        house += 1
    print(f"Part One: {house}")

def stopping_elves():
    global house
    house = 1
    delivered = 0
    while not delivered:
        numdelivered = factors2(house)
        if numdelivered >= presents:
            delivered = 1
            break
        house += 1
    print(f"Part Two: {house}")

presents = 34_000_000

deliver_presents()
stopping_elves()