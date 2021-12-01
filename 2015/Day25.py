def find_codeid():
    global codeid
    rowcol = row + column
    codeid = (rowcol * (rowcol - 1))//2 + 1 - row

def find_code():
    global code
    power = codeid - 1
    multiply = pow(mult, power, mod)
    code = (firstcode * multiply) % mod
    print(f"Christmas: {code}")

row = 2978
column = 3083

firstcode = 20151125
mult = 252533
mod = 33554393

find_codeid()
find_code()