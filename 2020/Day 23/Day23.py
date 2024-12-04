#Part one only
#Uses a list to store the sequence of cups
#Pops out 3 cups and then inserts the 3 cups at a new location each round

class Cups:
    def __init__(self, order, part):
        self.order = [int(char) for char in str(order)]
        self.idx = 0
        self.three_out = []
        self.length = len(self.order)
    
    def pop_three(self):
        current = self.order[self.idx]
        for i in range(3):
            newidx = (self.idx+1) % len(self.order)
            self.three_out.append(self.order.pop(newidx))
            self.idx = self.order.index(current)

    def insert_three(self):
        current = self.order[self.idx]
        for i in range(1, 5):
            dest = (current-i) % self.length
            if dest == 0:
                dest = self.length
            if dest in self.order:
                destidx = self.order.index(dest)
                break
        for i in range(1, 4):
            self.order.insert(destidx+i, self.three_out.pop(0))
        self.idx = self.order.index(current)
    
    def run_round(self):
        self.pop_three()
        self.insert_three()
        self.idx = (self.idx + 1) % self.length
        #print(self.order)
        
def part_one():
    for i in range(100):
        cups1.run_round()
    startidx = cups1.order.index(1)
    string = ""
    for i in range(1, cups1.length):
        idx = (startidx + i) % cups1.length
        string += str(cups1.order[idx])
    print(string)
    
order = 398254716
cups1 = Cups(order, 1)
part_one()