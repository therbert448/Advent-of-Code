def find_loops(key):
    subject = 7
    mod = 20201227
    current = subject % mod
    i = 0
    while True:
        if current == key:
            return i + 1
        else:
            current *= subject
            current = current % mod
            i += 1

def encrypt_key(key, loops):
    subject = key
    mod = 20201227
    current = 1
    for i in range(loops):
        current *= subject
        current = current % mod
    return current

card = 6930903
door = 19716708

cardloops = find_loops(card)
key = encrypt_key(door, cardloops)
print(key)