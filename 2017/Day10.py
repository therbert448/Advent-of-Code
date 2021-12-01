def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global lengths, asclens
    string = file.read().strip()
    lengths = [int(length) for length in string.split(",")]
    asclens = [ord(char) for char in string]
    suffix = [17, 31, 73, 47, 23]
    for s in suffix:
        asclens.append(s)
    file.close()

def generate_list():
    global listlist
    listlist = [i for i in range(size)]

def hash_list(length, point, skip):
    rev = []
    for i in range(length):
        idx = (point+i) % size
        rev.append(listlist[idx])
    for i in range(length):
        idx = (point+i) % size
        listlist[idx] = rev.pop() 
    point = (point + length + skip) % size
    skip += 1
    return point, skip

def run_lengths():
    point = 0
    skip = 0
    for length in lengths:
        point, skip = hash_list(length, point, skip)
    mult = listlist[0] * listlist[1]
    print("Part One:", mult)

def run_hash():
    point = 0
    skip = 0
    for _ in range(64):
        for length in asclens:
            point, skip = hash_list(length, point, skip)

def xor(listlist):
    result = 0
    for x in listlist:
        result = result ^ x
    return result

def dense_hash():
    densehash = []
    length = 16
    for i in range(length):
        densehash.append(xor(listlist[(i*length):(i+1)*length]))
    return densehash

def hexa(densehash):
    finalhash = ""
    for d in densehash:
        inhex = str(hex(d)[2:]).zfill(2)
        finalhash += inhex
    print("Part Two:", finalhash)
    
def part_one():
    generate_list()
    run_lengths()

def part_two():
    generate_list()
    run_hash()
    densehash = dense_hash()
    hexa(densehash)

day = 10
open_file()

size = 256

part_one()
part_two()