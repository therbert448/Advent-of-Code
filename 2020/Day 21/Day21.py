def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global allergens
    global foods
    global alltofoo
    allergens = set()
    foods = []
    alltofoo = []
    for line in inputs:
        line = line.split(" (contains ")
        food = line[0].strip().split(" ")
        foods.append(food)
        aller = line[1].strip(")\n").split(", ")
        adict = {}
        for a in aller:
            allergens.add(a)
            adict[a] = set()
            for f in food:
                adict[a].add(f)
        alltofoo.append(adict)

def count_allergens(setdict, allyfood):
    allcount = {}
    for food in allyfood:
        count = 0
        for a in setdict:
            if food in setdict[a]:
                count += 1
        allcount[food] = count
    return allcount

def count_foods(setdict):
    foodcount = {}
    for a in setdict:
        foodcount[a] = len(setdict[a])
    return foodcount

def part_one():
    foodset = set()
    for line in foods:
        for food in line:
            foodset.add(food)
    global setdict
    global allyfood
    setdict = {}
    allyfood = set()
    for a in allergens:
        setA =set(foodset)
        for line in alltofoo:
            if a in line:
                setB = set(line[a])
                setA = setA.intersection(setB)
        setdict[a] = setA
        allyfood.update(setA)
    nonally = foodset.difference(allyfood)
    count = 0
    for f in nonally:
        for line in foods:
            if f in line:
                count += 1
    print("Part One = ", count)
            
def part_two():
    allcount = count_allergens(setdict, allyfood)
    foodcount = count_foods(setdict)
    matchpairs = {}
    allvals = list(allcount.values())
    allkeys = list(allcount.keys())
    foodvals = list(foodcount.values())
    foodkeys = list(foodcount.keys())
    while not all([c == 0 for c in allvals]):
        if 1 in foodvals:
            allergen = foodkeys[foodvals.index(1)]
            food = setdict[allergen].pop()
            matchpairs[allergen] = food
            setdict.pop(allergen) #remove confirmed field
            for a in setdict:
                if food in setdict[a]:
                    setdict[a].remove(food)
        elif 1 in allvals:
            food = allkeys[allvals.index(1)]
            for a in setdict:
                if food in setdict[a]:
                    allergen = a
                    break
            matchpairs[allergen] = food
            setdict.pop(allergen) #remove confirmed field
        else:
            print("Stopped prematurely")
        allcount = count_allergens(setdict, allyfood)
        foodcount = count_foods(setdict)
        allvals = list(allcount.values())
        allkeys = list(allcount.keys())
        foodvals = list(foodcount.values())
        foodkeys = list(foodcount.keys())       
    sortall = sorted(list(matchpairs.keys()))
    candanging = "" #Canonical Dangerous Ingredient List
    for a in sortall:
        food = matchpairs[a]
        candanging += food + ","
    candanging = candanging.strip(",")
    print("Part Two =", candanging)
    
day = 21
inputs = open_file()

formatdata(inputs)
   
part_one()
part_two()