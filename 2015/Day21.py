class Player:
    def __init__(self):
        self.hp = 100
        self.dead = 0
    
    def equip(self, items):
        self.damage = 0
        self.armour = 0
        for item in items:
            self.damage += item.damage
            self.armour += item.armour
    
    def attack(self, other):
        if self.dead:
            return
        if self.damage <= other.armour:
            other.hp -= 1
        else:
            damage = self.damage - other.armour
            other.hp -= damage
        if other.hp <= 0:
            other.dead = 1

class Boss:
    def __init__(self):
        self.hp = 104
        self.damage = 8
        self.armour = 1
        self.dead = 0
    
    def attack(self, other):
        if self.dead:
            return
        if self.damage <= other.armour:
            other.hp -= 1
        else:
            damage = self.damage - other.armour
            other.hp -= damage
        if other.hp <= 0:
            other.dead = 1

class Item:
    def __init__(self, cost, damage, armour):
        self.cost = cost
        self.damage = damage
        self.armour = armour

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.read().strip().split("\n\n")
    file.close()

def format_data():
    global weapons, armour, rings
    weapons, armour, rings = [{}, {}, {}]
    for i, group in enumerate(inputs):
        items = group.splitlines()[1:]
        for item in items:
            name, cost, dam, arm = item.strip().split()
            cost, dam, arm = [int(cost), int(dam), int(arm)]
            if i == 0:
                weapons[name] = Item(cost, dam, arm)
            elif i == 1:
                armour[name] = Item(cost, dam, arm)
            else:
                rings[name] = Item(cost, dam, arm)

def combinations():
    global combs
    combs = set()
    weaplist = list(weapons.values())
    armlist = list(armour.values())
    ringlist = list(rings.values())
    for i in range(len(weaplist)):
        weapon = [weaplist[i]]
        for j in range(len(armlist) + 1):
            if j == len(armlist):
                arm = []
            else:
                arm = [armlist[j]]
            for k in range(len(ringlist) + 1):
                if k == len(ringlist):
                    rs = []
                    equipment = tuple([*weapon, *arm, *rs])
                    combs.add(equipment)
                else:
                    rs = [ringlist[k]]
                    equipment = tuple([*weapon, *arm, *rs])
                    combs.add(equipment)
                    for l in range(k+1, len(ringlist)):
                        rs = [ringlist[k], ringlist[l]]
                        equipment = tuple([*weapon, *arm, *rs])
                        combs.add(equipment)

def run_battle(equipment):
    boss = Boss()
    player = Player()
    player.equip(equipment)
    alive = 1
    while alive:
        player.attack(boss)
        boss.attack(player)
        if player.dead or boss.dead:
            alive = 0
            break
    if boss.dead:
        return True
    else:
        return False

def try_combinations():
    global winning, losing
    winning = set()
    losing = set()
    for equipment in combs:
        cost = sum(item.cost for item in equipment)
        win = run_battle(equipment)
        if win:
            winning.add(cost)
        else:
            losing.add(cost)
    print(f"Part One: {min(winning)}")
    print(f"Part Two: {max(losing)}")

day = 21
open_file()

format_data()

combinations()

try_combinations()