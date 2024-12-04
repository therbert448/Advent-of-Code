def open_file(day):
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def formatdata(inputs):
    global adapt
    adapt = [int(i.strip()) for i in inputs]
    adapt.sort()

def count_differences():
    outlet = 0
    countdif = [0, 0, 0]
    for i in range(0, len(adapt)):
        if i == 0:
            dif = adapt[i] - outlet
        else:
            dif = adapt[i] - adapt[i-1]
        countdif[dif-1] += 1
    countdif[2] += 1
    prod = countdif[0] * countdif[2]
    return prod

def paths_to():
    pathsto = [1]
    
    for i in range(0, len(adapt)):
        if i == 0:
            pathsto.append(1)
            continue
        elif i == 1:
            dif1 = adapt[i] - adapt[i-1]
            dif2 = adapt[i]
            if dif2 <= 3:
                count = pathsto[i] + pathsto[i-1]
                pathsto.append(count)
            else:
                count = pathsto[i]
                pathsto.append(count)
            continue
        
        if i == 2:
            dif3 = adapt[i]
        else:
            dif3 = adapt[i] - adapt[i-3]
        
        dif1 = adapt[i] - adapt[i-1]
        dif2 = adapt[i] - adapt[i-2]
        
        if dif3 == 3:
            count = pathsto[i] + pathsto[i-1] + pathsto[i-2]
            pathsto.append(count)
        elif dif2 <= 3:
            count = pathsto[i] + pathsto[i-1]
            pathsto.append(count)
        else:
            count = pathsto[i]
            pathsto.append(count)
            
    return pathsto


            

day = 10
inputs = open_file(day)

formatdata(inputs)

prod = count_differences()

pathsto = paths_to()

print(prod)
print(pathsto[-1])
