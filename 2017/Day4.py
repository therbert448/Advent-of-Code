def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global phrases, valids
    phrases = []
    valids = []
    for line in inputs:
        phrase = line.split(" ")
        unique = set(phrase)
        if len(unique) == len(phrase):
            valids.append(phrase)
        phrases.append(phrase)
    print("Phase One:", len(valids))

def anagrams():
    mostvalid = []
    for line in valids:
        unique = set()
        for word in line:
            letters = tuple(sorted([char for char in word]))
            unique.add(letters)
        if len(unique) == len(line):
            mostvalid.append(line)
    print("Part Two:", len(mostvalid))

day = 4
open_file()

format_data()

anagrams()