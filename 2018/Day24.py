class Group:
    def  __init__(self, num, hp, attpower, atttype, init, weak, immune):
        self.num = num
        self.hp = hp
        self.attpower = attpower
        self.atttype = atttype
        self.init = init
        self.weak = weak
        self.immune = immune
        
    def eff_power(self):
        return self.num * self.attpower
    
    def act_pow(self, enemy):
        if self.atttype in enemy.weak:
            return self.eff_power() * 2
        elif self.atttype in enemy.immune:
            return 0
        else:
            return self.eff_power()

    def attack_enemy(self, enemy):
        power = self.act_pow(enemy)
        enemyhp = enemy.hp
        unitskilled = power//enemyhp
        if unitskilled > enemy.num:
            unitskilled = enemy.num
        enemy.num -= unitskilled
        return unitskilled

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.read().split("\n\n")
    file.close()

def format_data():
    global allgroups, imms, infs
    allgroups = set()
    imms = []
    infs = []
    for j, ii in enumerate(inputs):
        i = 0
        ii = ii.splitlines()[1:]
        for line in ii:
            line = line.strip()
            num, rest = line.split(" units each with ")
            num = int(num)
            hp, rest = rest.split(" hit points")
            hp = int(hp)
            wi, rest = rest.split(" with an attack that does ")
            weak, immune = [set(), set()]
            if "weak" in wi and "immune" in wi:
                wi = wi.strip(" ()").split("; ")
            elif "weak" in wi or "immune" in wi:
                wi = [wi.strip(" ()")]
            if wi != " ":
                for effect in wi:
                    eff, cause = effect.split(" to ")
                    cause = set([c for c in cause.split(", ")])
                    if eff == "weak":
                        weak = cause
                    else:
                        immune = cause
            attpower, *rest = rest.split(" ")
            attpower = int(attpower)
            attype = rest[0]
            init = int(rest[-1])
            group = Group(num, hp, attpower, attype, init, weak, immune)
            allgroups.add(group)
            if j == 0:
                idx = "imm" + str(i)
                group.idx = idx
                imms.append(group)
            else:
                idx = "inf" + str(i)
                group.idx = idx
                infs.append(group)
            i += 1

def target(p):
    if p in imms:
        enemies = list(infs)
    else:
        enemies = list(imms)
    posstargs = []
    for enemy in enemies:
        if enemy not in targeted and p.act_pow(enemy) != 0:
            posstargs.append(enemy)
    if not posstargs:
        p.target = None
    else:
        sortkey = lambda e: (p.act_pow(e), e.eff_power(), e.init)
        posstargs.sort(key=sortkey, reverse=True)
        targ = posstargs.pop(0)
        p.target = targ
        targeted.append(targ)

def attack(prime):
    targ = prime.target
    if targ != None:
        killed = prime.attack_enemy(targ)
        return killed
    return 0

def fight():   
    global targeted, killed
    targeted = []
    killed = 0
    left = [*imms, *infs]
    targord = [obj for obj in left]
    targord.sort(key=lambda g: (g.eff_power(), g.init), reverse=True)
    for prime in targord:
        target(prime)
    attord = [obj for obj in left]
    attord.sort(key=lambda g: (g.init), reverse=True)
    for prime in attord:
        killed += attack(prime)
    for obj in left:
        if obj.num == 0 and obj in imms:
            imms.remove(obj)
        elif obj.num == 0 and obj in infs:
            infs.remove(obj)

def run_rounds():
    stalemate = 0
    while imms and infs and not stalemate:
        fight()
        if killed == 0:
            stalemate = 1

def part_one():
    format_data()
    run_rounds()
    left = [*imms, *infs]
    finalunits = sum([g.num for g in left])
    print("Part One:", finalunits)

def part_two():
    boost = 0
    immwins = 0
    while not immwins:
        boost += 1
        format_data()
        for imm in imms:
            imm.attpower += boost
        run_rounds()
        if imms and not infs:
            immwins = 1
            break
    left = [*imms]
    finalunits = sum([g.num for g in left])
    print("Part Two:", finalunits, "\nBoost was", boost)

day = 24
open_file()

part_one()
part_two()