class Program:
    def __init__(self):
        self.register = {}
        for i in range(8):
            self.register[chr(97 + i)] = 0
        self.point = 0
        self.count = 0

    def setx(self, reg, potreg):
        if isinstance(potreg, int):
            self.register[reg] = potreg
        else:
            self.register[reg] = self.register[potreg]
        self.point += 1
    
    def subx(self, reg, potreg):
        if isinstance(potreg, int):
            self.register[reg] -= potreg
        else:
            self.register[reg] -= self.register[potreg]
        self.point += 1
    
    def mulx(self, reg, potreg):
        self.count += 1
        if isinstance(potreg, int):
            self.register[reg] *= potreg
        else:
            self.register[reg] *= self.register[potreg]
        self.point += 1
    
    def jnzx(self, reg, potreg):
        if isinstance(potreg, int):
            jump = potreg
        else:
            jump = self.register[potreg]
        if isinstance(reg, int) and reg != 0:
            self.point += jump
        elif self.register[reg] != 0:
            self.point += jump
        else:
            self.point += 1

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global steps, program
    steps = []
    for line in inputs:
        step = line.split(" ")
        command = step[0]
        reg = step[1]
        expr = "program." + command + "x(*regs)"
        try:
            reg = int(reg)
        except:
            pass
        potreg = step[2]
        try:
            potreg = int(potreg)
        except:
            pass
        regs = [reg, potreg]
        steps.append([expr, *regs])
    program = Program()

def run_debug():
    format_data()
    numsteps = len(steps)
    while 0 <= program.point < numsteps:
        step = steps[program.point]
        expr = step[0]
        regs = step[1:]
        eval(expr)
    print("Part One:", program.count)
    
def run_program():
    format_data()
    program.register["a"] = 1
    for i in range(100):
        step = steps[program.point]
        expr = step[0]
        regs = step[1:]
        eval(expr)
        print(program.point, step, program.register.values()) 
        #try to figure out what it does by running it
        #ok that isn't so clear just looking at the registers
        #I'll break it down step by step below

def non_prime(val):
    sqrt = int(val ** 0.5) #only need to check up to the square root
    for i in range(2, sqrt+1): #ignore 1 as all primes are divisible by 1
        if val % i == 0:
            return 1 #has a factor so is non prime
    return 0 #couldn't find a factor, so is prime

def count_non_primes():
    start = 106500
    step = 17
    n = 1001
    count = 0
    for _ in range(n):
        count += non_prime(start)
        start += step
    print("Part Two:", count)

day = 23
open_file()

run_debug()
#run_program()
count_non_primes()

"""
0:  set b 65        =>      register b set to 65
1:  set c b         =>      set c to 65
2:  jnz a 2         =>      a is 1 so jump to 4 (not debug mode)
4:  mul b 100       =>      b x 100 = 6500
5:  sub b -100000   =>      add 100_000 to b = 106500
6:  set c b         =>      c also = 106500
7:  sub c -17000    =>      add 17000 to c = 123500
8:  set f 1         =>      f becomes 1
9:  set d 2         =>      d becomes 2
10: set e 2         =>      e becomes 2
11: set g d         =>      g becomes d = 2
12: mul g e         =>      g = g x e = 4
13: sub g b         =>      g - b = 4 - 106500
14: jnz g 2         =>      jump forward to 16
16: sub e -1        =>      add one to e = 3
17: set g e         =>      g becomes e = 3
18: sub g b         =>      g - b = 3 - 106500
19: jnz g -8        =>      jump back and start a loop
11: etc.

e will increase by one each loop.
if e x 2 == 106500, step 15 is run (f is set to 0)
f isn't used elsewhere in the loop, so can ignore.
The next non jump is when e == 106500, at which point:

20: sub d -1        =>      add one to d = 3
21: set g d         =>      g becomes d = 3
22: sub g b         =>      g = g - b = 3 - 106500
23: jnz g -13       =>      jump back to step 10

again increasing e, this time if e x 3 == 106500, f is set to 0 (again)
otherwise loop exits when e = 106500
d is increased each time e hits 106500, until d is 106500, then:

24: jnz f 2         =>      by this point f is definitely = 0
25: sub h -1        =>      h = 1
26: set g b         =>      g set to b = 106500
27: sub g c         =>      106500 - 123500 = -17000
28: jnz g 2         =>      jump to 30
30: sub b -17       =>      106500 + 17 = 106517
31: jnz 1 -23       =>      jump back to 8

f becomes 1 again, and it starts to become clear.
We're adding 17 to b = 106500 multiple times, until it reaches 123500 
(after 1001 full loops at which point we hit step 29 and escape).
Each time we increment values of d and e in turn to try to find factors for b.
If a factor is found (so b is not prime), f is set to 0.
If f is zero, we add 1 to h.
Counts the number of non primes between 106500 and 123500, incrementing 17
"""