class Cookie:
    def __init__(self, mixture):
        cap, dur, flav, text, self.cals = [0, 0, 0, 0, 0]
        for name, val in mixture.items():
            ing = ings[name]
            cap += val * ing.cap
            dur += val * ing.dur
            flav += val * ing.flav
            text += val * ing.text
            self.cals += val * ing.cal
        if cap < 0:
            cap = 0
        if dur < 0:
            dur = 0
        if flav < 0:
            flav = 0
        if text < 0:
            text = 0
        self.score = cap * dur * flav * text

class Ingredient:
    def __init__(self, cap, dur, flav, text, cal):
        self.cap = cap
        self.dur = dur
        self.flav = flav
        self.text = text
        self.cal = cal

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global ings
    ings = {}
    for line in inputs:
        name, _, cp, _, d, _, f, _, t, _, cl = line.split(" ")
        name = name[:-1]
        cp = int(cp[:-1])
        d = int(d[:-1])
        f = int(f[:-1])
        t = int(t[:-1])
        cl = int(cl)
        ing = Ingredient(cp, d, f, t, cl)
        ings[name] = ing

def try_mixtures():
    teaspoons = 100
    bestcookie = -1
    bestlowcal = -1
    ingreds = sorted(ings.keys())
    mixture = {}
    for i in range(teaspoons + 1):
        mixture[ingreds[0]] = i
        for j in range(teaspoons + 1 - i):
            mixture[ingreds[1]] = j
            for k in range(teaspoons + 1 - (i+j)):
                mixture[ingreds[2]] = k
                mixture[ingreds[3]] = teaspoons - (i+j+k)
                cookie = Cookie(mixture)
                score = cookie.score
                if cookie.cals == 500 and score > bestlowcal:
                    bestlowcal = score
                if score > bestcookie:
                    bestcookie = score
    print(f"Part One: {bestcookie}")
    print(f"Part Two: {bestlowcal}")

day = 15
open_file()

format_data()

try_mixtures()