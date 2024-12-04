class Grid:
    def __init__(self, tiledict):
        self.tiledict = tiledict #dictionary of input tiles
    
    def all_bords(self, tile): #find borders of the tile
        tilegrid = self.tiledict[tile]
        t = tilegrid[0]     #top border
        b = tilegrid[-1]    #bottom border
        r = ""              #right border
        l = ""              #left border
        for line in tilegrid:
            l += line[0]
            r += line[-1]
        return t, b, r, l
    
    def get_borders(self):
        self.bdict = {} #dictionary containing list of borders for a tile
        for tile in self.tiledict:
            t, b, r, l = self.all_bords(tile)
            bordset = {t, b, r, l}
            self.bdict[tile] = bordset
    
    def find_borders(self):
        self.bordcount = {} #count how may tiles this tile shares a border with
        newborddict = {}
        for tile in self.bdict:
            newborddict[tile] = set()
            count = 0
            for tile2 in self.bdict:
                if tile == tile2:
                    continue
                for b in self.bdict[tile]:
                    if b in self.bdict[tile2] or b[::-1] in self.bdict[tile2]:
                        count += 1
                        newborddict[tile].add(b)
                        break
            self.bordcount[tile] = count
        self.bdict = newborddict
    
    def find_corners(self):
        mult = 1
        self.corners = []
        for tile in self.bordcount: #corners only have two neighbours
            if self.bordcount[tile] == 2:
                mult *= int(tile)
                self.corners.append(tile)
        del self.bordcount #don't need bord count any more
        print("Part One =", mult) #Output for part one
    
    def rotate_tile(self, tilegrid): #Rotate tile 90degs clockwise
        newgrid = [] 
        for i in range(len(tilegrid)):
            row = ""
            for j in range(len(tilegrid)):
                row = row + tilegrid[-(j+1)][i]
            newgrid.append(row)
        return newgrid

    def flip_vert(self, tilegrid): #flip tile vertically
        newgrid = []
        for i in range(len(tilegrid)):
            newgrid.append(tilegrid[-(i+1)])
        return newgrid

    def flip_horiz(self, tilegrid): #flip tile horizontally
        newgrid = []
        for i in range(len(tilegrid)):
            row = ""
            for j in range(len(tilegrid)):
                row = row + tilegrid[i][-(j+1)]
            newgrid.append(row)
        return newgrid
    
    def top_left(self): #Start laying out tiles, 
                        #starting with a corner tile in the top left
        tile = self.corners[0] #just pick the first corner tile
        tilegrid = self.tiledict[tile]
        bords = self.bdict[tile]
        t, b, r, l = self.all_bords(tile)
        #rotate tile until the shared borders are on the right and bottom
        if t in bords and r in bords: 
            tilegrid = self.rotate_tile(tilegrid)
        elif l in bords and t in bords:
            for i in range(2):
                tilegrid = self.rotate_tile(tilegrid)
        elif b in bords and l in bords:
            for i in range(3):
                tilegrid = self.rotate_tile(tilegrid)
        elif r in bords and b in bords:
            pass
        else:
            print("Completely wrong") #shared borders must not be opposite
        self.tiledict[tile] = tilegrid
        _, b, r, _ = self.all_bords(tile)
        self.pos = (0, 0)
        #trim tile of borders
        tilegrid = [tilegrid[i][1:9] for i in range(1,9)]
        self.bdict.pop(tile)    #remove tile from further searches
        posr = (self.pos[0] + 1, self.pos[1]) #position of tile to the right
        posb = (self.pos[0], self.pos[1] + 1) #position of tile underneath
        self.postile = {self.pos: tilegrid} #Save tile in dict of correct tiles
        self.posbord = {posr: {"L": r}, posb: {"T": b}}
        #Save right and bottom borders, to be checked when filling up the grid
    
    def next_grid(self):
        bords = self.posbord[self.pos] #borders to the left and/or top
        if "L" in bords and "T" not in bords: #top row case
            lb = bords["L"]
            for tile in self.bdict:
                bd = self.bdict[tile]
                if lb in bd or lb[::-1] in bd:
                    break #find tile that matches border to the left
            tilegrid = self.tiledict[tile]
            t, b, r, l = self.all_bords(tile)
            #rotate tile until left border matches left tile
            if t == lb or t[::-1] == lb:
                for i in range(3):
                    tilegrid = self.rotate_tile(tilegrid)
            elif r == lb or r[::-1] == lb:
                for i in range(2):
                    tilegrid = self.rotate_tile(tilegrid)
            elif b == lb or b[::-1] == lb:
                tilegrid = self.rotate_tile(tilegrid)
            self.tiledict[tile] = tilegrid
            _, _, _, l = self.all_bords(tile)
            if l != lb: #if border doesn't match, flip vertically
                tilegrid = self.flip_vert(tilegrid)
                self.tiledict[tile] = tilegrid
            _, b, r, _ = self.all_bords(tile)
        elif "T" in bords and "L" not in bords: #left column case
            tb = bords["T"]
            for tile in self.bdict:
                bd = self.bdict[tile]
                if tb in bd or tb[::-1] in bd:
                    break #find tile that matches border above
            tilegrid = self.tiledict[tile]
            t, b, r, l = self.all_bords(tile)
            #rotate tile until top border matches tile above
            if r == tb or r[::-1] == tb:
                for i in range(3):
                    tilegrid = self.rotate_tile(tilegrid)
            elif b == tb or b[::-1] == tb:
                for i in range(2):
                    tilegrid = self.rotate_tile(tilegrid)
            elif l == tb or l[::-1] == tb:
                tilegrid = self.rotate_tile(tilegrid)
            self.tiledict[tile] = tilegrid
            t, _, _, _ = self.all_bords(tile)
            if t != tb: #if border still doesn't match, flip horizontally
                tilegrid = self.flip_horiz(tilegrid)
            self.tiledict[tile] = tilegrid
            _, b, r, _ = self.all_bords(tile)
        else: #all other cases
            lb = bords["L"]
            tb = bords["T"]
            for tile in self.bdict:
                bd = self.bdict[tile]
                if lb in bd or lb[::-1] in bd:
                    break #only check for left border (only one possibility)
            tilegrid = self.tiledict[tile]
            t, b, r, l = self.all_bords(tile)
            #rotate tile until left border matches left tile
            if t == lb or t[::-1] == lb:
                for i in range(3):
                    tilegrid = self.rotate_tile(tilegrid)
            elif r == lb or r[::-1] == lb:
                for i in range(2):
                    tilegrid = self.rotate_tile(tilegrid)
            elif b == lb or b[::-1] == lb:
                tilegrid = self.rotate_tile(tilegrid)
            self.tiledict[tile] = tilegrid
            t, _, _, l = self.all_bords(tile)
            if l != lb: #if left border isn't correct, flip vertically
                tilegrid = self.flip_vert(tilegrid)
            self.tiledict[tile] = tilegrid
            _, b, r, _ = self.all_bords(tile)
        tilegrid = [tilegrid[i][1:9] for i in range(1,9)] #trim tile
        self.bdict.pop(tile) #remove tile from further searches
        posr = (self.pos[0] + 1, self.pos[1])
        posb = (self.pos[0], self.pos[1] + 1)
        self.postile[self.pos] = tilegrid #save correct tile
        if posr not in self.posbord:
            self.posbord[posr] = {"L": r}
        else:
            self.posbord[posr]["L"] = r
        if posb not in self.posbord:
            self.posbord[posb] = {"T": b}
        else:
            self.posbord[posb]["T"] = b
        self.posbord.pop(self.pos)
        
    def join_rows(self, poslist):
        self.image = []
        lenr = 8
        for i, line in enumerate(poslist):
            strlist = []
            for j in range(lenr):
                strlist.append("")
            for square in line:
                for k, string in enumerate(self.postile[square]):
                    strlist[k] += string
            for rowstr in strlist:
                self.image.append(rowstr)
    
    def find_coords(self):
        self.coords = []
        for i, line in enumerate(self.monster):
            for j, char in enumerate(line):
                if char == "#":
                    self.coords.append([i,j])
    
    def search_image(self):
        w = 20
        h = 3
        dim = 96
        px = 0
        py = 0
        imlist = [list(line) for line in self.image]
        while py <= dim - h:
            while px <= dim - w:
                subimage = [row[px:px+w] for row in self.image[py:py+h]]
                good = 1
                for c in self.coords:
                    if subimage[c[0]][c[1]] != "#":
                        good = 0
                        break
                if good == 1:
                    for c in self.coords:
                        if imlist[py + c[0]] [px + c[1]] == "0":
                            print("Overlap")
                        else:
                            imlist[py + c[0]] [px + c[1]] = "0"
                px += 1
            py += 1
            px = 0
        count = 0
        for line in imlist:
            count += line.count("#")
        print("Part Two =", count)
    
    def fill_grid(self):
        self.top_left()
        poslist = []
        for i in range(12):
            self.pos = (0, i)
            rowlist = []
            for j in range(12):
                if i == 0 and j == 0:
                    rowlist.append(self.pos)
                    self.pos = (self.pos[0] + 1, self.pos[1])
                    continue        
                rowlist.append(self.pos)        
                self.next_grid()
                self.pos = (self.pos[0] + 1, self.pos[1])
            poslist.append(rowlist)
        self.join_rows(poslist)
    
def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().strip()
    file.close()
    return inputs

def formatdata(tiles):
    global tiledict
    tiledict = {}
    for tile in tiles:
        tile = tile.split("\n")
        tileID = tile[0][-5:-1]
        tiledict[tileID] = tile[1:]
    return tiledict

def part_one():
    grid.get_borders()
    grid.find_borders()
    grid.find_corners()

def part_two():
    grid.fill_grid()
    grid.monster = ["                  # ",
                    "#    ##    ##    ###",
                    " #  #  #  #  #  #   "]
    grid.find_coords()
    for i in range(3):
        grid.image = grid.rotate_tile(grid.image)
    grid.search_image()
    
day = 20
tiles = open_file().split("\n\n")

tiledict = formatdata(tiles)

grid = Grid(tiledict)

part_one()

part_two()