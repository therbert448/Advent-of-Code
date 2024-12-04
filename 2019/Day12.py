class Moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = [0, 0, 0]
    
    def calc_vel(self, other):
        self.previous = 0
        for i, xyz in enumerate(self.pos):
            if xyz < other.pos[i]:
                self.vel[i] += 1
            elif xyz > other.pos[i]:
                self.vel[i] -= 1

    def change_pos(self):
        self.previous = 0
        for i in range(len(self.pos)):
            self.pos[i] += self.vel[i]        

def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x, y)
    return lcm

def open_file():
    #file = open("test.txt")
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global moons
    moons = []
    for line in inputs:
        line = line.strip("<>\n").split(", ")
        line = [int(l.strip("xyz=")) for l in line]
        moons.append(line)
    #print(moons)

def part_one():
    for i in range(10):
        for moon in Moons:
            for other in Moons:
                if other == moon:
                    continue
                moon.calc_vel(other)
        for moon in Moons:
            moon.change_pos()
    energy = 0
    for moon in Moons:
        pot = sum([abs(p) for p in moon.pos])
        kin = sum([abs(v) for v in moon.vel])
        energy += pot*kin
    print(energy)

def part_two():
    t = 0
    sx = ""
    sy = ""
    sz = ""
    for moon in Moons:
        sx += str(moon.pos[0]) + str(moon.vel[0])
        sy += str(moon.pos[1]) + str(moon.vel[1])
        sz += str(moon.pos[2]) + str(moon.vel[2])
    statesx = {sx}
    statesy = {sy}
    statesz = {sz}
    states = [0, 0, 0]
    while not all([s == 1 for s in states]):
        for moon in Moons:
            for other in Moons:
                if other == moon:
                    continue
                moon.calc_vel(other)
        for moon in Moons:
            moon.change_pos()
        sx = ""
        sy = ""
        sz = ""
        for moon in Moons:
            sx += str(moon.pos[0]) + str(moon.vel[0])
            sy += str(moon.pos[1]) + str(moon.vel[1])
            sz += str(moon.pos[2]) + str(moon.vel[2])
        if sx in statesx and states[0] == 0:
            states[0] = 1
            tx = t+1
        if sy in statesy and states[1] == 0:
            states[1] = 1
            ty = t+1
        if sz in statesz and states[2] == 0:
            states[2] = 1
            tz = t+1
        statesx.add(sx)
        statesy.add(sy)
        statesz.add(sz)
        t += 1
    print(tx)
    print(ty)
    print(tz)
    txy = compute_lcm(tx, ty)
    txyz = compute_lcm(txy, tz)
    print(txyz)

day = 12
inputs = open_file()

formatdata(inputs)

#Moons = [Moon(moon) for moon in moons]
#part_one()
Moons = [Moon(moon) for moon in moons]
part_two()