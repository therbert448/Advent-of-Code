def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    startmap = file.readlines()
    file.close()
    return startmap

def formatdata(inputs):
    global steps
    steps = []
    for line in inputs:
        if "cut" in line:
            cut, val = line.split(" ")
            val = int(val)
            steps.append([cut, val])
        elif "new" in line:
            steps.append(["deal", "new"])
        else:
            deal, val = line.split(" with increment ")
            steps.append([deal, int(val)])

def apply_step_card(pos, N, step):
    move = step[0]
    if move == "cut":
        val = step[1]
        newpos = (pos - val) % N
    elif move == "deal" and step[1] == "new":
        newpos = N - pos - 1
    else:
        val = step[1]
        newpos= (pos * val) % N
    return newpos

def shuffle_card(pos, N):
    newpos = pos
    for step in steps:
        newpos = apply_step_card(newpos, N, step)
    return newpos

def step_to_equation(step, A, B, N):
    move = step[0]
    if move == "cut":
        val = step[1]
        B = (B + val) % N
    elif move == "deal" and step[1] == "new":
        A = -A
        B = N - B - 1
    else:
        val = step[1]
        z = pow(val, N-2, N)
        A = A*z % N
        B = B*z % N
    return A, B

def inverse_steps(N):
    A = 1
    B = 0
    for step in steps[::-1]:
        A, B = step_to_equation(step, A, B, N)
    return A, B
 
def apply_equation(A, B, N, n): #apply equation n times and find the new A, B
    #recursive, breaking down n as much as possible
    #A(Ax + B) + B = A**2x + AB + B
    #If I know the AB pair after n shuffles, then applying the equation with
    #this AB pair will give me the AB pair after 2n shuffles.
    #n+1 shuffles means apply the original AB pair for one shuffle to the AB
    #pair for n shuffles.
    #Helps break the original n down to ~log2(n) equations
    if n == 0: #no need to apply equation, A = 1 and B = 0
        return 1, 0
    elif n % 2 == 0: #even number of applications left
        A, B = [(A**2) % N, ((A*B)+B) % N]
        A, B = apply_equation(A, B, N, n//2)
        return A, B
    else: #odd number left
        a, b = apply_equation(A, B, N, n-1)
        A, B = [(A*a) % N, ((A*b)+B) % N]
        return A, B

def part_one():
    N = 10_007
    card = 2019
    newcard = shuffle_card(card, N)
    A, B = inverse_steps(N)
    print(((newcard * A) + B) % N)
    return newcard        

def part_two():
    N = 119315717514047
    n = 101741582076661
    finalpos = 2020
    A, B = inverse_steps(N)
    A, B = apply_equation(A, B, N, n)
    print(((finalpos * A) + B) % N)

day = 22
inputs = open_file()

formatdata(inputs)

p1 = part_one()
print(p1)
part_two()