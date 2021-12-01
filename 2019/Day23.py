class IntCode:
    def __init__(self, code):
        self.codes = []
        self.inputs = {}
        self.incount = []
        self.outputs = {}
        self.points = []
        self.relbases = []
        self.halts = []
        self.noins = []
        for _ in range(1000):
            code.append(0)
        for i in range(50):
            self.codes.append([c for c in code])
            self.inputs[i] = []
            self.incount.append(0)
            self.outputs[i] = []
            self.points.append(0)
            self.relbases.append(0)
            self.halts.append(False)
            self.noins.append(0)
        self.NAT = []
    
    def halt_case(self):
        self.halts[self.idx] = True
        self.points[self.idx] += 1
    
    def add_case(self):
        idx = self.idx
        c = self.codes[idx][self.points[idx]:self.points[idx]+4]
        ocstr = str(c[0]).zfill(5)
        params = [ocstr[-3], ocstr[-4], ocstr[-5]]
        add = 0
        for i, p in enumerate(params[0:2]):
            if p == "0":
                add += self.codes[idx][c[i+1]]
            elif p == "1":
                add += c[i+1]
            elif p == "2":
                add += self.codes[idx][c[i+1] + self.relbases[idx]]
        if params[2] == "0":
            self.codes[idx][c[3]] = add
        elif params[2] == "2":
            self.codes[idx][c[3] + self.relbases[idx]] = add
        self.points[idx] += 4
    
    def multiply_case(self):
        idx = self.idx
        c = self.codes[idx][self.points[idx]:self.points[idx]+4]
        ocstr = str(c[0]).zfill(5)
        params = [ocstr[-3], ocstr[-4], ocstr[-5]]
        mult = 1
        for i, p in enumerate(params[0:2]):
            if p == "0":
                mult *= self.codes[idx][c[i+1]]
            elif p == "1":
                mult *= c[i+1]
            elif p == "2":
                mult *= self.codes[idx][c[i+1] + self.relbases[idx]]
        if params[2] == "0":
            self.codes[idx][c[3]] = mult
        elif params[2] == "2":
            self.codes[idx][c[3] + self.relbases[idx]] = mult
        self.points[idx] += 4
    
    def input_case(self):
        idx = self.idx
        c = self.codes[idx][self.points[idx]:self.points[idx]+2]
        ocstr = str(c[0]).zfill(3)
        param = ocstr[-3]
        incount = self.incount[idx]
        if incount == 0:
            userin = idx
            self.incount[idx] += 1
            self.noins[idx] = 0
        else:
            if not self.inputs[idx]:
                userin = -1
                self.noins[idx] = 1
            elif incount == 1:
                userin = self.inputs[idx][0][0]
                self.incount[idx] += 1
                self.noins[idx] = 0
            else:
                userin = self.inputs[idx][0][1]
                self.inputs[idx].pop(0)
                self.incount[idx] = 1
                self.noins[idx] = 0
        if param == "0":
            self.codes[idx][c[1]] = userin
        elif param == "2":
            self.codes[idx][c[1] + self.relbases[idx]] = userin
        self.points[idx] += 2
    
    def output_case(self):
        idx = self.idx
        c = self.codes[idx][self.points[idx]:self.points[idx]+2]
        ocstr = str(c[0]).zfill(3)
        param = ocstr[-3]
        if param == "0":
            out = self.codes[idx][c[1]]
        elif param == "1":
            out = c[1]
        elif param == "2":
            out = self.codes[idx][c[1] + self.relbases[idx]]
        self.outputs[idx].append(out)
        if len(self.outputs[idx]) == 3:
            address = self.outputs[idx][0]
            x = self.outputs[idx][1]
            y = self.outputs[idx][2]
            if address not in self.inputs:
                self.inputs[address] = []
            self.inputs[address].append([x, y])
            self.outputs[idx] = []
            if address == 255:
                self.NAT = [x, y]
                self.inputs[address] = []
        self.points[idx] += 2
    
    def jump_true(self):
        idx = self.idx
        c = self.codes[idx][self.points[idx]:self.points[idx]+3]
        ocstr = str(c[0]).zfill(4)
        params = [ocstr[-3], ocstr[-4]]
        vals = []
        for i, p in enumerate(params):
            if p == "0":
                vals.append(self.codes[idx][c[i+1]])
            elif p == "1":
                vals.append(c[i+1])
            elif p == "2":
                vals.append(self.codes[idx][c[i+1] + self.relbases[idx]])
        if vals[0] != 0:
            self.points[idx] = vals[1]
        else:
            self.points[idx] += 3
        
    def jump_false(self):
        idx = self.idx
        c = self.codes[idx][self.points[idx]:self.points[idx]+3]
        ocstr = str(c[0]).zfill(4)
        params = [ocstr[-3], ocstr[-4]]
        vals = []
        for i, p in enumerate(params):
            if p == "0":
                vals.append(self.codes[idx][c[i+1]])
            elif p == "1":
                vals.append(c[i+1])
            elif p == "2":
                vals.append(self.codes[idx][c[i+1] + self.relbases[idx]])
        if vals[0] == 0:
            self.points[idx] = vals[1]
        else:
            self.points[idx] += 3
    
    def less_than(self):
        idx = self.idx
        c = self.codes[idx][self.points[idx]:self.points[idx]+4]
        ocstr = str(c[0]).zfill(5)
        params = [ocstr[-3], ocstr[-4], ocstr[-5]]
        vals = []
        for i, p in enumerate(params[0:2]):
            if p == "0":
                vals.append(self.codes[idx][c[i+1]])
            elif p == "1":
                vals.append(c[i+1])
            elif p == "2":
                vals.append(self.codes[idx][c[i+1] + self.relbases[idx]])
        if vals[0] < vals[1]:
            if params[2] == "0":
                self.codes[idx][c[3]] = 1
            elif params[2] == "2":
                self.codes[idx][c[3] + self.relbases[idx]] = 1
        else:
            if params[2] == "0":
                self.codes[idx][c[3]] = 0
            elif params[2] == "2":
                self.codes[idx][c[3] + self.relbases[idx]] = 0
        self.points[idx] += 4
    
    def equals(self):
        idx = self.idx
        c = self.codes[idx][self.points[idx]:self.points[idx]+4]
        ocstr = str(c[0]).zfill(5)
        params = [ocstr[-3], ocstr[-4], ocstr[-5]]
        vals = []
        for i, p in enumerate(params[0:2]):
            if p == "0":
                vals.append(self.codes[idx][c[i+1]])
            elif p == "1":
                vals.append(c[i+1])
            elif p == "2":
                vals.append(self.codes[idx][c[i+1] + self.relbases[idx]])
        if vals[0] == vals[1]:
            if params[2] == "0":
                self.codes[idx][c[3]] = 1
            elif params[2] == "2":
                self.codes[idx][c[3] + self.relbases[idx]] = 1
        else:
            if params[2] == "0":
                self.codes[idx][c[3]] = 0
            elif params[2] == "2":
                self.codes[idx][c[3] + self.relbases[idx]] = 0
        self.points[idx] += 4
    
    def rel_change(self):
        idx =self.idx
        c = self.codes[idx][self.points[idx]:self.points[idx]+2]
        ocstr = str(c[0]).zfill(3)
        param = ocstr[-3]
        if param == "0":
            self.relbases[idx] += self.codes[idx][c[1]]
        elif param == "1":
            self.relbases[idx] += c[1]
        elif param == "2":
            self.relbase[idx] += self.codes[idx][c[1] + self.relbases[idx]]
        self.points[idx] += 2
        
    def run(self):
        lasty = 0
        while not all(self.halts):
            inwait = 0
            for i in range(50):
                if len(self.inputs[i]) > 0:
                    inwait += 1
            if all(self.noins) and self.NAT:
                y = self.NAT[1]
                if y == lasty:
                    print("Y:", y)
                    self.halts = [True for i in self.halts]
                self.inputs[0].append(self.NAT)
                self.NAT = []
                lasty = y
            for i in range(50):
                self.idx = i
                ocstr = str(self.codes[i][self.points[i]]).zfill(2)
                opcode = ocstr[-2:]
                if opcode == "99":
                    self.halt_case()
                elif opcode == "01":
                    self.add_case()
                elif opcode == "02":
                    self.multiply_case()
                elif opcode == "03":
                    self.input_case()
                elif opcode == "04":
                    self.output_case()
                elif opcode == "05":
                    self.jump_true()
                elif opcode == "06":
                    self.jump_false()
                elif opcode == "07":
                    self.less_than()
                elif opcode == "08":
                    self.equals()
                elif opcode == "09":
                    self.rel_change()
        print("All computers have halted")
        return
    
def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().strip()
    file.close()
    return inputs

def formatdata(inputs):
    global code
    code = [int(i) for i in inputs.split(",")]        
    
day = 23
inputs = open_file()

formatdata(inputs)

Code = IntCode(code)
Code.run()