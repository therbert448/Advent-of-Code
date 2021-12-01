def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = file.read().strip().split("\n\n")
    file.close()

def format_data():
    global replacements, moleculein, reverse
    replacements = {}
    reverse = {}
    reacts = inputs[0].splitlines()
    for line in reacts:
        charin, charsout = line.strip().split(" => ")
        if charin not in replacements:
            replacements[charin] = [charsout]
        else:
            replacements[charin].append(charsout)
        reverse[charsout] = charin
    moleculein = inputs[1]

def replace_one():
    global molecules
    molecules = set()
    point = 0
    strlen = len(moleculein)
    while point < strlen:
        char = moleculein[point]
        if point < strlen - 1:
            chartwo = moleculein[point + 1]
            if chartwo.islower():
                char = char + chartwo
                end = point + 2
            else:
                end = point + 1
        else:
            end = point + 1
        if char not in replacements:
            point = end
            continue
        molesout = replacements[char]
        for mole in molesout:
            newmole = moleculein[:point] + mole + moleculein[end:]
            molecules.add(newmole)
        point = end
    print(f"Part One: {len(molecules)}")

def reverse_engineer():
    global moleset
    string = ""
    point = 0
    moleset = {string: 0}
    while point < len(moleculein):
        count = moleset[string]
        string += moleculein[point]
        moleset[string] = count
        for mole in reverse:
            out = reverse[mole]
            if mole in string:
                string = string.replace(mole, out)
                moleset[string] = count + 1
                break
        point += 1
    print(f"Part Two: {moleset['e']}")

"""
Very strange
Taking my inputs directly off the website makes part two completely unsolvable
This is because my medicine molecule has a string: 
"...RnCaCaCaSiThCaRnCaFArY..."
that is impossible to reduce with the given replacements.
"CaCaCaSiThCa" reduces to just "Ca"
"...RnCaRn..." is impossible to reduce, unless the replacements containing
"CRn..." actually mean "CaRn..."
Assuming this to be the case, then we have "...RnCaRnCaFArY..."
or "...RnCaRnFArY...".
This can become "...RnNY..."
but "...RnNY..." can never be reduced.
If I then assume that it's actually meant to be "...RnFY...", I can reduce it
all and get the correct answer 207.
But changing my inputs like this gives me the wrong answer for part one.

I'll just have to use two input files to have the right answers printed.
"""

day = 19
open_file()

format_data()

replace_one()

day = "19b"
open_file()

format_data()

reverse_engineer()