#Both parts one and two
#Instead of a list of the full sequence, use a dictionary
#Every key is a cup in the sequence, the value is the next cup in the sequence
#To pop and insert cups, just change which cup the current cup points to

import time

class Cups:
    def __init__(self, order, part):
        self.order = [int(char) for char in str(order)] #Input into list
        self.length = len(self.order)
        self.current = self.order[0]
        self.cupdict = {} #For each cup in list, set its value to the next cup
        if part == 1:
            for i, cup in enumerate(self.order):
                self.cupdict[cup] = self.order[(i+1) % self.length]
        if part == 2:
            numcups = 1_000_000
            for i, cup in enumerate(self.order):
                if i+1 == self.length:
                    self.cupdict[cup] = i+2
                else:
                    self.cupdict[cup] = self.order[(i+1)]
            for i in range(self.length+1, numcups+1):
                if i % numcups == 0:
                    self.cupdict[i] = self.current
                else:
                    self.cupdict[i] = i + 1
            self.length = numcups
        
    def pop_three(self):
        self.links = [self.current]
        for i in range(4):
            nextcup = self.cupdict[self.links[i]]
            self.links.append(nextcup)

    def insert_three(self):
        current = self.current
        for i in range(1, 5):
            dest = (current-i) % self.length
            if dest == 0:
                dest = self.length
            if dest not in self.links[1:4]:
                after = self.cupdict[dest]
                self.cupdict[dest] = self.links[1]
                self.cupdict[self.links[3]] = after
                self.cupdict[self.links[0]] = self.links[4]
                break
    
    def run_round(self):
        self.pop_three()
        self.insert_three()
        self.current = self.cupdict[self.current]
        #print(self.order)
        
def part_one():
    for i in range(100):
        cups1.run_round()
    nextkey = 1
    string = ""
    for i in range(cups1.length-1):
        val = cups1.cupdict[nextkey]
        string += str(val)
        nextkey = val
    print("Answer to Part One =", string)

def part_two():
    for i in range(10_000_000):
        if i % 1_000_000 == 0:
            print(i//1_000_000) #Just to show progress
        cups2.run_round()
    nextkey = 1
    mult = 1
    for i in range(2):
        val = cups2.cupdict[nextkey]
        print(val)
        mult *= val
        nextkey = val
    print("Answer to Part Two =", mult)

t0 = time.perf_counter()
order = 398254716
cups1 = Cups(order, 1)
part_one() #Answer to Part One = 45798623
t1 = time.perf_counter()
cups2 = Cups(order, 2)
part_two() #Answer to Part Two = 235551949822
t2 = time.perf_counter()

print(f"Part One took {t1-t0:0.7f} seconds")
#Part One took 0.0008292 seconds
print(f"Part Two took {t2-t1:0.3f} seconds")
#Part Two took 32.837 seconds