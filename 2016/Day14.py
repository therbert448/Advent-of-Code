import hashlib

def find_keys(n):
    global i, hashes
    hashes = {}
    count = 0
    i = -1
    while count < 64:
        i += 1
        if i not in hashes:
            string = salt + str(i)
            for _ in range(n):
                string = hashlib.md5(string.encode()).hexdigest()
            hashes[i] = string
        else:
            string = hashes[i]
        quinset = set()
        hashlen = len(string)
        for j, char in enumerate(string):
            if j >= hashlen - 2:
                break
            if char == string[j+1] and char == string[j+2]:
                quin = char * 5
                quinset.add(quin)
                break
        if quinset:
            found = 0
            for j in range(1000):
                k = i + j + 1
                if k not in hashes:
                    string = salt + str(k)
                    for _ in range(n):
                        string = hashlib.md5(string.encode()).hexdigest()
                    hashes[k] = string
                else:
                    string = hashes[k]
                for quin in quinset:
                    if quin in string:
                        found = 1
                        break
                if found:
                    count += 1
                    break
    if n == 1:
        print(f"Part One: {i}")
    else:
        print(f"Part Two: {i}")

salt = "ngcjuoqr"

find_keys(1)
find_keys(2017)