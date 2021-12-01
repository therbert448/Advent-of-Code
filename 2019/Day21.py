class IntCode:
    def __init__(self, code, command):
        self.code = list(code)
        for i in range(10000):
            self.code.append(0)
        self.point = 0
        self.relbase = 0
        self.outstring = ""
        self.comcountline = 0
        self.comcountchar = 0
        self.command = command
        
    def halt_case(self):
        print("\nPart", part, ":", self.outstring, "\n")
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
        if self.outstring != "":
            print(self.outstring.strip())
        self.outstring = ""
        c = self.code[self.point:self.point+2]
        ocstr = str(c[0]).zfill(3)
        param = ocstr[-3]
        if self.comcountchar == 0:
            string = ""
            for char in self.command[self.comcountline]:
                string += chr(char)
            print(string.strip())
        userin = self.command[self.comcountline][self.comcountchar]
        if userin == 10:
            self.comcountline += 1
            self.comcountchar = 0
        else:
            self.comcountchar += 1
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
        try:
            self.outstring += chr(out)
        except:
            self.outstring = out
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
    
day = 21
inputs = open_file()

formatdata(inputs)

A,B,C,D,J,K,L,N,O,R,T,W,sp,nl = [65,66,67,68,74,75,76,78,79,82,84,87,32,10]
command = [[N, O, T, sp, A, sp, J, nl],
           [N, O, T, sp, B, sp, T, nl],
           [O, R, sp, T, sp, J, nl],
           [N, O, T, sp, C, sp, T, nl],
           [O, R, sp, T, sp, J, nl],
           [A, N, D, sp, D, sp, J, nl],
           [W, A, L, K, nl]]

global part
part = "1"

Code = IntCode(code, command)
Code.run()

E,F,G,H,I,U = [69,70,71,72,73,85]

command = [[N, O, T, sp, A, sp, J, nl],
           [N, O, T, sp, B, sp, T, nl],
           [O, R, sp, T, sp, J, nl],
           [N, O, T, sp, C, sp, T, nl],
           [O, R, sp, T, sp, J, nl],
           [A, N, D, sp, D, sp, J, nl],
           [N, O, T, sp, J, sp, T, nl],
           [O, R, sp, E, sp, T, nl],
           [O, R, sp, H, sp, T, nl],
           [A, N, D, sp, T, sp, J, nl],
           [R, U, N, nl]]

part = "2"

Code = IntCode(code, command)
Code.run()