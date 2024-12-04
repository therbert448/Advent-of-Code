def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global expressions
    expressions = []
    lines = [i.strip().replace(" ","") for i in inputs]
    for line in lines:
        expression = []
        for char in line: #Input only contains single digit integers
            if char not in ("(", ")", "+", "*"):
                char = int(char)
            expression.append(char)
        expressions.append(expression)    

def find_paren_pair(substr):
    #When open parenthesis present, find corresponding close parenthesis
    start = substr.index("(")+1
    count = 1
    for i in range(len(substr[start:])):
        end = start + i
        if substr[end] == "(":
            #If there's another "(" before a ")", we need to skip the next ")"
            count += 1
        elif substr[end] == ")":
            count -= 1
            if count == 0:
                return end #Return index of corresponding ")"
    print("Parentheses don't match up")
    return
        
def solve_expr(substr):
    point = 0
    if substr[point] == "(":
        #If "(" at start, resolve the parentheses first
        end = find_paren_pair(substr[point:])
        total = solve_expr(substr[point+1:point+end])
        point += end
    else:
        total = substr[point] #Running total of sums and multiplications
    while point < len(substr)-1:
        case = substr[point + 1] #Always an operator between numbers
        point += 2
        valb = substr[point] #Value to add or multiply to total
        if valb == "(": #If parentheses present, resolve the brackets
            end = find_paren_pair(substr[point:])
            valb = solve_expr(substr[point+1:point+end])
            #Output from the parenthesis, to be added or multiplied to total
            point += end
            #Move pointer to after the parentheses
        if case == "+":
            total += valb
        elif case == "*":
            total *= valb
        else:
            print("Wrong operator used")
    return total

def solve_expr2(substr):
    point = 0
    sums = [] #List to keep a record of (sum) values between muliply operators
    if substr[point] == "(": #As part one
        end = find_paren_pair(substr[point:])
        subsum = solve_expr2(substr[point+1:point+end])
        point += end
    else:
        subsum = substr[point]
    while point < len(substr)-1:
        case = substr[point + 1]
        point += 2
        valb = substr[point]
        if valb == "(":
            end = find_paren_pair(substr[point:])
            valb = solve_expr2(substr[point+1:point+end])
            point += end
        if case == "+":
            subsum += valb
        elif case == "*": #Skip the multiplication step
            sums.append(subsum) #Save the running total up to the "*"
            subsum = valb #Start new running total with value to right of "*"
        else:
            print("Wrong operator used")
    sums.append(subsum)
    #Save last running total value
    total = 1
    for s in sums:
        total *= s
    #Multiply every term in sums (finally applying the multiply operators)
    return total

def it_expr(expressions):
    totals1 = list(map(solve_expr, expressions)) #Part one
    totals2 = list(map(solve_expr2, expressions)) #Part two
    return totals1, totals2

day = 18
inputs = [i.strip() for i in open_file()]

formatdata(inputs)

totals1, totals2 = it_expr(expressions)
print(sum(totals1)) #67800526776934
print(sum(totals2)) #340789638435483