from itertools import permutations

class IntCode:
    def __init__(self, codes, points, sets, count, val, part):
        self.codes = codes
        self.points = points
        self.sets = sets
        self.count = count
        self.val = val
        self.part = part
    
    def halt_case(self):
        #print("Halt")
        self.point += 1
    
    def add_case(self):
        c = self.code[self.point:self.point+4]
        ocstr = str(c[0]).zfill(4)
        params = [ocstr[-3], ocstr[-4]]
        add = 0
        for i, p in enumerate(params):
            if p == "0":
                add += self.code[c[i+1]]
            elif p == "1":
                add += c[i+1]
        self.code[c[3]] = add
        self.point += 4
    
    def multiply_case(self):
        c = self.code[self.point:self.point+4]
        ocstr = str(c[0]).zfill(4)
        params = [ocstr[-3], ocstr[-4]]
        mult = 1
        for i, p in enumerate(params):
            if p == "0":
                mult *= self.code[c[i+1]]
            elif p == "1":
                mult *= c[i+1]
        self.code[c[3]] = mult
        self.point += 4
    
    def input_case(self):
        c = self.code[self.point:self.point+2]
        userin = int(input("Input: "))
        self.code[c[1]] = userin
        self.point += 2
        
    def input_case_auto(self, inval):
        c = self.code[self.point:self.point+2]
        self.code[c[1]] = inval
        self.point += 2
    
    def output_case(self):
        c = self.code[self.point:self.point+2]
        ocstr = str(c[0]).zfill(3)
        param = ocstr[-3]
        if param == "0":
            out = self.code[c[1]]
        elif param == "1":
            out = c[1]
        self.point += 2
        self.val = out
    
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
        if vals[0] == 0:
            self.point = vals[1]
        else:
            self.point += 3
    
    def less_than(self):
        c = self.code[self.point:self.point+4]
        ocstr = str(c[0]).zfill(4)
        params = [ocstr[-3], ocstr[-4]]
        vals = []
        for i, p in enumerate(params):
            if p == "0":
                vals.append(self.code[c[i+1]])
            elif p == "1":
                vals.append(c[i+1])
        if vals[0] < vals[1]:
            self.code[c[3]] = 1
        else:
            self.code[c[3]] = 0
        self.point += 4
    
    def equals(self):
        c = self.code[self.point:self.point+4]
        ocstr = str(c[0]).zfill(4)
        params = [ocstr[-3], ocstr[-4]]
        vals = []
        for i, p in enumerate(params):
            if p == "0":
                vals.append(self.code[c[i+1]])
            elif p == "1":
                vals.append(c[i+1])
        if vals[0] == vals[1]:
            self.code[c[3]] = 1
        else:
            self.code[c[3]] = 0
        self.point += 4
        
    def run(self):
        idx = self.count % len(self.sets)
        self.code = list(self.codes[idx])
        self.point = self.points[idx]
        setting = self.sets[idx]
        lencode = len(self.code)
        out = 0
        if self.count < len(self.sets):
            count2 = 0
        else:
            count2 = 1
        while self.point < lencode:
            ocstr = str(self.code[self.point]).zfill(2)
            opcode = ocstr[-2:]
            if opcode == "99":
                self.halt_case()
                return self.val
            elif opcode == "01":
                self.add_case()
            elif opcode == "02":
                self.multiply_case()
            elif opcode == "03":
                if count2 == 0:
                    inval = setting
                    count2 += 1
                else:
                    inval = self.val
                self.input_case_auto(inval)
            elif opcode == "04":
                self.output_case()
                if self.part == 2:
                    self.points[idx] = self.point
                    self.codes[idx] = self.code
                    self.count += 1
                    self.val = self.run()
                    return self.val
            elif opcode == "05":
                self.jump_true()
            elif opcode == "06":
                self.jump_false()
            elif opcode == "07":
                self.less_than()
            elif opcode == "08":
                self.equals()
        print("Code didn't end properly")
        return 0
    
def open_file():
    #file = open("test.txt")
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().strip()
    file.close()
    return inputs

def formatdata(inputs):
    global code
    code = [int(i) for i in inputs.split(",")]

def part_one(settings):
    outputs = []
    for setlist in settings:
        inval = 0
        for setting in setlist:
            codes = [code]
            points = [0]
            setlist = [setting]
            Code = IntCode(codes, points, setlist, 0, inval, 1)
            out = Code.run()
            inval = out
        outputs.append(out)
    maxout = max(outputs)
    return maxout

def part_two(settings):
    outputs = []
    for setlist in settings:
        codes = [code, code, code, code, code]
        points = [0, 0 ,0, 0, 0]
        Code = IntCode(codes, points, setlist, 0, 0, 2)
        out = Code.run()
        outputs.append(out)
    maxout = max(outputs)
    return maxout

def perms(setrange):
    settings = list(permutations(setrange))
    return settings  
    
day = 7
inputs = open_file()

formatdata(inputs)

setrange1 = [0, 1, 2, 3, 4]
setrange2 = [5, 6, 7, 8 ,9]

settings1 = perms(setrange1)
settings2 = perms(setrange2)

print(part_one(settings1))
print(part_two(settings2))