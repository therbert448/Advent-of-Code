import math as maths

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global mass
    mass = [int(line) for line in inputs]

def fuel_eq(mass):
    fuel = maths.floor(mass/3)-2
    if fuel < 0:
        fuel = 0
    return fuel

def part_one():
    fuel = list(map(fuel_eq, mass))
    output = sum(fuel)
    return output

def part_two(fuel):
    fuelsum = fuel
    addfuel = fuel_eq(fuel)
    if addfuel == 0:
        return fuelsum
    fuelsum += part_two(addfuel) 
    return fuelsum

day = 1
inputs = open_file()

formatdata(inputs)

fuel = part_one()
print(fuel)
fuels = list(map(part_two, mass))
fuelsnew = list(map(lambda a, b: a - b, fuels, mass))
print(sum(fuelsnew))