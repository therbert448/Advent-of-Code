def print_grid(grid, xset, yset): #Print game grid (actually works as a game)
    minx, maxx = [min(xset), max(xset)] #corners
    miny, maxy = [min(yset), max(yset)]
    newgrid = []
    for i in range(miny, maxy+1):
        row = ""
        for j in range(minx, maxx+1):
            if (j, i) in grid:
                row += str(grid[(j, i)])
            else:
                row += " "
        newgrid.append(row) #fill a grid with strings
    [print(line) for line in newgrid] #print each line

class IntCode:
    def __init__(self, code):
        self.code = list(code)
        for i in range(1000):
            self.code.append(0)
        self.point = 0
        self.relbase = 0
        self.pos = (0, 0)
        self.xset = {self.pos[0]}
        self.yset = {self.pos[1]}
        self.grid = {self.pos: "D"}
        self.posset = {self.pos}
        self.indir = {1:"N", 2:"S", 3:"W", 4:"E"}
        self.outstat = {0, 1, 2}
        self.deadend = set()
        self.stepcount = {self.pos: 0}
        self.count = 0
    
    def move_dir(self, direct):
        dirs = {"N": (0,-1), "S": (0,1), "E": (1,0), "W": (-1,0)}
        move = dirs[direct]
        f = lambda a,b: a+b
        newpos = tuple(map(f, self.pos, move))
        return newpos
    
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
        userin = 0
        poslist = {}
        for d in self.indir:
            direct = self.indir[d]
            nextpos = self.move_dir(direct)
            poslist[d] = nextpos
            if nextpos not in self.posset:
                userin = d
                del poslist
                break
        if userin == 0:
            self.deadend.add(self.pos)
            newposlist = dict(poslist)
            for d in poslist:
                p = poslist[d]
                if self.grid[p] == "#":
                    del newposlist[d]
            for d in newposlist:
                p = newposlist[d]
                if p not in self.deadend:
                    userin = d
                    del poslist, newposlist
                    break
        if userin == 0:
            print("Full map covered")
            self.end = 1
            print_grid(self.grid, self.xset, self.yset)
            return
        if param == "0":
            self.code[c[1]] = userin
        elif param == "2":
            self.code[c[1] + self.relbase] = userin
        direct = self.indir[userin]
        self.newpos = self.move_dir(direct)
        self.xset.add(self.newpos[0])
        self.yset.add(self.newpos[1])
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
        if out not in self.outstat:
            print("Output not expected")
        elif out == 0:
            self.grid[self.newpos] = "#"
            if self.newpos not in self.posset:
                self.posset.add(self.newpos)
        elif out == 1:
            if self.newpos not in self.posset:
                self.posset.add(self.newpos)
                self.stepcount[self.newpos] = self.stepcount[self.pos] + 1
            self.grid[self.pos] = "."
            self.pos = self.newpos
            self.grid[self.pos] = "D"
        else:
            self.count += 1
            if self.newpos not in self.posset:
                self.posset.add(self.newpos)
                self.stepcount[self.newpos] = self.stepcount[self.pos] + 1
            if self.count == 1:
                print("Found the Oxygen System")
                self.pos = self.newpos
                self.grid = {self.pos: "X"}
                self.osys = self.stepcount[self.pos]
                print(self.osys)
                self.xset = {self.pos[0]}
                self.yset = {self.pos[1]}
                self.posset = {self.pos}
                self.deadend = set()
                self.stepcount = {self.pos: 0}
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
        self.end = 0
        while self.point < lencode and self.end == 0:
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
        print(max(self.stepcount.values()))
        return
    
def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().strip()
    file.close()
    return inputs

def formatdata(inputs):
    global code
    code = [int(i) for i in inputs.split(",")]        
    
day = 15
inputs = open_file()

formatdata(inputs)

Code = IntCode(code)
Code.run()