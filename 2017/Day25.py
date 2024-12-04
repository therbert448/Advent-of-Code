class Turing_Machine:
    def __init__(self):
        self.point = 0
        self.state = "A"
        self.ones = set()
        self.n = 12667664
    
    def A(self):
        if self.point in self.ones:
            self.ones.remove(self.point)
            self.point -= 1
            self.state = "C"
        else:
            self.ones.add(self.point)
            self.point += 1
            self.state = "B"
    
    def B(self):
        if self.point in self.ones:
            self.point += 1
            self.state = "D"
        else:
            self.ones.add(self.point)
            self.point -= 1
            self.state = "A"
    
    def C(self):
        if self.point in self.ones:
            self.ones.remove(self.point)
            self.state = "E"
        else:
            self.state = "B"
        self.point -= 1
    
    def D(self):
        if self.point in self.ones:
            self.ones.remove(self.point)
            self.state = "B"
        else:
            self.ones.add(self.point)
            self.state = "A"
        self.point += 1
    
    def E(self):
        if self.point in self.ones:
            self.state = "C"
        else:
            self.ones.add(self.point)
            self.state = "F"
        self.point -= 1

    def F(self):
        if self.point in self.ones:
            self.state = "A"
        else:
            self.ones.add(self.point)
            self.state = "D"
        self.point += 1
    
    def run(self):
        for _ in range(self.n):
            expr = "self." + self.state + "()"
            eval(expr)
        print("Part One:", len(self.ones))

machine = Turing_Machine()
machine.run()