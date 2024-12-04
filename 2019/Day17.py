class IntCode:
    def __init__(self, code):
        self.code = list(code)
        for i in range(10000):
            self.code.append(0)
        self.point = 0
        self.relbase = 0
        self.string = ""
        self.count = 0
        a, b, c, co, e, l, r = [65, 66, 67, 44, 10, 76, 82]
        self.rout = [a,co,b,co,a,co,c,co,b,co,c,co,b,co,c,co,a,co,c,e]
        self.A = [l,co,49,48,co,r,co,49,50,co,r,co,49,50,e]
        self.B = [r,co,54,co,r,co,49,48,co,l,co,49,48,e]
        self.C = [r,co,49,48,co,l,co,49,48,co,l,co,49,50,co,r,co,54,e]
        self.feed = [ord("n"), 10]
        self.lastout = ""
        self.printnow = 0
        self.linecount = 0
        self.outstring = ""
        self.instring = ""
        
    def halt_case(self):
        print(int(self.out))
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
        if self.count == 0:
            userin = self.rout.pop(0)
            self.instring += chr(userin)
            if userin == 10:
                self.count += 1
                print(self.instring)
                self.instring = ""
        elif self.count == 1:
            userin = self.A.pop(0)
            self.instring += chr(userin)
            if userin == 10:
                self.count += 1
                print(self.instring)
                self.instring = ""
        elif self.count == 2:
            userin = self.B.pop(0)
            self.instring += chr(userin)
            if userin == 10:
                self.count += 1
                print(self.instring)
                self.instring = ""
        elif self.count == 3:
            userin = self.C.pop(0)
            self.instring += chr(userin)
            if userin == 10:
                self.count += 1
                print(self.instring)
                self.instring = ""
        else:
            userin = self.feed.pop(0)
            self.instring += chr(userin)
            if userin == 10:
                self.count += 1
                print(self.instring)
                self.instring = ""
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
        if out == 10:
            self.string += "\n"
            if self.lastout == 10:
                self.linecount += 1
            self.lastout = out
            if self.linecount > 1:
                self.printnow = 1
        else:
            self.string += chr(out)
            self.lastout == chr(out)
            self.linecount = 0
        if self.printnow == 1:
            self.outstring += chr(out)
        self.out = out
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

def define_grid(Code):
    string = Code.string.splitlines()
    posdict = {}
    for i, line in enumerate(string):
        for j, char in enumerate(line):
            posdict[(j, i)] = char
    return posdict

def neighbours(pos):
    neighs = []
    steps = [(1,0), (0,1), (-1,0), (0,-1)]
    f = lambda a,b: a+b
    for step in steps:
        newpos = tuple(map(f, pos, step))
        neighs.append(newpos)
    return neighs

def find_intersects(Code):
    posdict = define_grid(Code)
    posset = set()
    for pos in posdict:
        if posdict[pos] != "#":
            continue
        neighs = neighbours(pos)
        count = 0
        for n in neighs:
            if n in posdict and posdict[n] == "#":
                count += 1
            else:
                break
        if count == 4:
            posset.add(pos)
    return posset

def calc_align_param(Code):
    posset = find_intersects(Code)
    total = 0
    for pos in posset:
        mult = pos[0] * pos[1]
        total += mult
    return total

def part_one():
    Code.run()
    total = calc_align_param(Code)
    print(total)
    
def part_two():
    Code2.run()
    
day = 17
inputs = open_file()

formatdata(inputs)

Code = IntCode(code)
part_one()
code[0] = 2
Code2 = IntCode(code)
part_two()