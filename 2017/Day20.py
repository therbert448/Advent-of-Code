class Particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a
        self.mandist = -1
    
    def man_dist(self):
        self.mandist = sum([abs(xyz) for xyz in self.p])
    
    def step(self):
        for i, a in enumerate(self.a):
            self.v[i] += a
            self.p[i] += self.v[i]
        self.man_dist()

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global particles
    particles = []
    for i, line in enumerate(inputs):
        p, v, a = line.split(">, ")
        p = [int(val) for val in p.strip("p=<").split(",")]
        v = [int(val) for val in v.strip("v=<").split(",")]
        a = [int(val) for val in a.strip("a=<>").split(",")]
        part = Particle(p, v, a)
        part.man_dist()
        particles.append(part)

def run_steps():
    format_data()
    global mini, mindist
    for i in range(1000): # 1000 is enough steps to find the closest particle
        mini = -1
        mindist = -1
        for i, part in enumerate(particles):
            part.step()
            if mindist == -1 or part.mandist < mindist:
                mini = i #which particle is the closest after all moves
                mindist = part.mandist
        if mini != -1:
            lasti = mini
    print("Part One:", lasti)

def run_collisions():
    format_data()
    for _ in range(1000): # 1000 is enough steps to find all collisions
        posid = {} #keep a record of which particle is at a given location
        colset = set() #keep a record of all particles that collide
        for i, part in enumerate(particles):
            part.step()
            pos = tuple(part.p)
            if pos not in posid: #position doesn't already have a particle
                posid[pos] = i
            else: #collision
                colset.add(i) #most recent particle to arrive
                colset.add(posid[pos]) #first particle to arrive
        for collision in sorted(colset, reverse=True):
            #Can't pop from beginning of list, otherwise everything moves left
            particles.pop(collision)
    print("Part Two:", len(particles))

#Could try something fancy to end the loops once all particles are diverging
#That would be the end of the search for both closest particle to origin, and
#the particles left after collision
#Too much faff though, when a loop of 1000 iterations is enough.     

day = 20
open_file()

format_data()

run_steps()
run_collisions()