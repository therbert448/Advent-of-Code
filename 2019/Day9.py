class IntCode:
    def __init__(self, code):
        self.code = list(code)
        for i in range(1000):
            self.code.append(0)
        self.point = 0
        self.relbase = 0
    
    def halt_case(self):
        print("Halt")
        self.point += 1
    
    def add_case(self):
        c = self.code[self.point:self.point+4]
        ocstr = str(c[0]).zfill(5)
        params = [ocstr[-3], ocstr[-4], ocstr[-5]]
        add = 0
        for i, p in enumerate(params[0:2]):
            if p == "0":
                add += self.code[c[i+1]]
            elif p == "1":
                add += c[i+1]
            elif p == "2":
                add += self.code[c[i+1] + self.relbase]
        if params[2] == "0":
            self.code[c[3]] = add
        elif params[2] == "2":
            self.code[c[3] + self.relbase] = add
        self.point += 4
    
    def multiply_case(self):
        c = self.code[self.point:self.point+4]
        ocstr = str(c[0]).zfill(5)
        params = [ocstr[-3], ocstr[-4], ocstr[-5]]
        mult = 1
        for i, p in enumerate(params[0:2]):
            if p == "0":
                mult *= self.code[c[i+1]]
            elif p == "1":
                mult *= c[i+1]
            elif p == "2":
                mult *= self.code[c[i+1] + self.relbase]
        if params[2] == "0":
            self.code[c[3]] = mult
        elif params[2] == "2":
            self.code[c[3] + self.relbase] = mult
        self.point += 4
    
    def input_case(self):
        c = self.code[self.point:self.point+2]
        ocstr = str(c[0]).zfill(3)
        param = ocstr[-3]
        userin = int(input("Input: "))
        if param == "0":
            self.code[c[1]] = userin
        elif param == "2":
            self.code[c[1] + self.relbase] = userin
        self.point += 2
    
    def output_case(self):
        c = self.code[self.point:self.point+2]
        ocstr = str(c[0]).zfill(3)
        param = ocstr[-3]
        if param == "0":
            out = self.code[c[1]]
        elif param == "1":
            out = c[1]
        elif param == "2":
            out = self.code[c[1] + self.relbase]
        print(out)
        self.point += 2
    
    def jump_true(self):
        c = self.code[self.point:self.point+3]
        ocstr = str(c[0]).zfill(4)
        params = [ocstr[-3], ocstr[-4]]
        vals = []
        for i, p in enumerate(params):
            if p == "0":
                vals.append(self.code[c[i+1]])
            elif p == "1":
                vals.append(c[i+1])
            elif p == "2":
                vals.append(self.code[c[i+1] + self.relbase])
        if vals[0] != 0:
            self.point = vals[1]
        else:
            self.point += 3
        
    def jump_false(self):
        c = self.code[self.point:self.point+3]
        ocstr = str(c[0]).zfill(4)
        params = [ocstr[-3], ocstr[-4]]
        vals = []
        for i, p in enumerate(params):
            if p == "0":
                vals.append(self.code[c[i+1]])
            elif p == "1":
                vals.append(c[i+1])
            elif p == "2":
                vals.append(self.code[c[i+1] + self.relbase])
        if vals[0] == 0:
            self.point = vals[1]
        else:
            self.point += 3
    
    def less_than(self):
        c = self.code[self.point:self.point+4]
        ocstr = str(c[0]).zfill(5)
        params = [ocstr[-3], ocstr[-4], ocstr[-5]]
        vals = []
        for i, p in enumerate(params[0:2]):
            if p == "0":
                vals.append(self.code[c[i+1]])
            elif p == "1":
                vals.append(c[i+1])
            elif p == "2":
                vals.append(self.code[c[i+1] + self.relbase])
        if vals[0] < vals[1]:
            if params[2] == "0":
                self.code[c[3]] = 1
            elif params[2] == "2":
                self.code[c[3] + self.relbase] = 1
        else:
            if params[2] == "0":
                self.code[c[3]] = 0
            elif params[2] == "2":
                self.code[c[3] + self.relbase] = 0
        self.point += 4
    
    def equals(self):
        c = self.code[self.point:self.point+4]
        ocstr = str(c[0]).zfill(5)
        params = [ocstr[-3], ocstr[-4], ocstr[-5]]
        vals = []
        for i, p in enumerate(params[0:2]):
            if p == "0":
                vals.append(self.code[c[i+1]])
            elif p == "1":
                vals.append(c[i+1])
            elif p == "2":
                vals.append(self.code[c[i+1] + self.relbase])
        if vals[0] == vals[1]:
            if params[2] == "0":
                self.code[c[3]] = 1
            elif params[2] == "2":
                self.code[c[3] + self.relbase] = 1
        else:
            if params[2] == "0":
                self.code[c[3]] = 0
            elif params[2] == "2":
                self.code[c[3] + self.relbase] = 0
        self.point += 4
    
    def rel_change(self):
        c = self.code[self.point:self.point+2]
        ocstr = str(c[0]).zfill(3)
        param = ocstr[-3]
        if param == "0":
            self.relbase += self.code[c[1]]
        elif param == "1":
            self.relbase += c[1]
        elif param == "2":
            self.relbase += self.code[c[1] + self.relbase]
        self.point += 2
        
    def run(self):
        lencode = len(self.code)
        while self.point < lencode:
            ocstr = str(self.code[self.point]).zfill(2)
            opcode = ocstr[-2:]
            if opcode == "99":
                self.halt_case()
                return
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
        print("Code didn't end properly")
        return
    
def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().strip()
    file.close()
    return inputs

def formatdata(inputs):
    global code
    code = [int(i) for i in inputs.split(",")]        
    
day = 9
inputs = open_file()

formatdata(inputs)

Code = IntCode(code)
Code.run()