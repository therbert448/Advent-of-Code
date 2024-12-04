"""
Advent of Code
2022 Day 11

@author: Tom Herbert
"""

day = 11

class Monkey:
    def __init__(self, items, operation, test, choices):
        self.items = items
        self.operation = operation
        self.test = test
        self.choices = choices
        self.inspected = 0
    
    def operate(self):
        old = self.worry
        new = eval(self.operation)
        self.worry = new
    
    def relief(self):
        if relief:
            self.worry = self.worry//3
        else:
            self.worry = self.worry % lcm
    
    def check(self):
        if self.worry % self.test:
            return False
        else:
            return True
        
    def throw(self, result):
        if result:
            nextMonkey = self.choices[0]
        else:
            nextMonkey = self.choices[1]
        monkeys[nextMonkey].items.append(self.worry)
    
    def inspect_and_throw(self):
        for i in range(len(self.items)):
            self.worry = self.items.pop(0)
            self.operate()
            self.relief()
            result = self.check()
            self.throw(result)
            self.inspected += 1
            

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = file.read().split("\n\n")
    return inputs

def new_monkeys():
    global monkeys
    monkeys = []
    for monkey in inputs:
        _, items, operation, test, *choices = monkey.strip().splitlines()
        items = [int(item) for item in items.split(": ")[-1].split(", ")]
        operation = operation.split(" = ")[-1]
        test = int(test.split(" ")[-1])
        choices = [int(line.split(" ")[-1]) for line in choices]
        newMonkey = Monkey(items, operation, test, choices)
        monkeys.append(newMonkey)

def part_one():
    global relief
    new_monkeys()
    relief = True
    Nrounds = 20
    for _ in range(Nrounds):
        for monkey in monkeys:
            monkey.inspect_and_throw()
    totalInspections = sorted([monkey.inspected for monkey in monkeys])
    monkeyBusiness = totalInspections[-1] * totalInspections[-2]
    print(f"Part One = {monkeyBusiness}")

def part_two():
    global relief, lcm
    new_monkeys()
    relief = False
    Nrounds = 10_000
    lcm = 1
    for monkey in monkeys:
        lcm *= monkey.test
    for _ in range(Nrounds):
        for monkey in monkeys:
            monkey.inspect_and_throw()
    totalInspections = sorted([monkey.inspected for monkey in monkeys])
    monkeyBusiness = totalInspections[-1] * totalInspections[-2]
    print(f"Part Two = {monkeyBusiness}")

inputs = open_file()

part_one()
part_two()
