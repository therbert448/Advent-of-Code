def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global string
    string = file.read().strip("^$")
    file.close()

#Finding the longest string that matches the RegEx works for the examples but
#not for the inputs. The furthest point can have multiple routes, so the only
#option is to map out the grid.
def map_out():
    poslist = [] #keep track of last positions before forks
    pos = (0, 0) #start from the centre
    global doorcount
    doorcount = {pos: 0} #keep track of minimum number of doors passed
    for char in string:
        if char == "(":
            poslist.append(pos) #save position before fork in path
        elif char == ")":
            pos = poslist.pop() #go back to the last position before the fork
            #from examples and cursory inspection of input, either a set of
            #brackets ends just before a |, in which case we'll automatically
            #return to the start of the fork, or the brackets will contain a
            #"skippable" detour.
            #We therefore do not need to keep track of the end positions of
            #every path in the brackets. This would add a lot more complexity.
            #If we had a situation like N(E|W)N, this may fall apart if we
            #can't cover every position
        elif char == "|":
            pos = poslist[-1] #return to fork for 2nd (or 3rd, etc.) branch
        else:
            steps = doorcount[pos] + 1
            pos = tuple(map(lambda a,b: a+b, pos, compass[char]))
            if pos not in doorcount:
                doorcount[pos] = steps
            elif doorcount[pos] > steps:
                doorcount[pos] = steps

day = 20
open_file()

compass = {"E": (1,0), "N": (0,1), "W": (-1,0), "S": (0,-1)}

map_out()
doors = list(doorcount.values())
print("Part One:", max(doors))
count = 0
for door in doors:
    if door >= 1000:
        count += 1
print("Part Two:", count)