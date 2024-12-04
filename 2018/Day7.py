def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def formatdata():
    global post, steps
    steps = set()
    post = {}
    for line in inputs:
        _, *midstr, _, _ = line.split(" ")
        midstr = " ".join(midstr)
        before, after = midstr.split(" must be finished before step ")
        if after not in post:
            post[after] = [before]
        else:
            post[after].append(before)
        if before not in steps:
            steps.add(before)
        if after not in steps:
            steps.add(after)

def run_through_steps():
    newsteps = set(steps) #list of all waiting steps
    sortsteps = sorted(newsteps) #list of steps in alphabetical order
    newpost = dict(post) #dict of blocked steps with tasks blocking them
    outstring = "" #order of tasks completed
    while newsteps: # while task still waiting
        for step in sortsteps: #look at each step alphabetically
            if step in newsteps and step not in newpost: #if task not blocked
                outstring += step #start the task
                newsteps.remove(step) #remove the task from waiting list
                for p in post: # remove the task from blocking other tasks
                    if p in newpost:
                        waiting = list(newpost[p])
                        if step in waiting:
                            waiting.remove(step)
                            if waiting:
                                newpost[p] = waiting
                            else:
                                del newpost[p]
                break
    print("Part One:", outstring)

def parallel_work():
    sortsteps = sorted(steps) #list of steps in alphabetical order
    newsteps = set(steps) #list of all waiting steps
    newpost = dict(post) #dict of blocked steps with the tasks blocking them
    elves = [0, 0, 0, 0, 0] #list of when elves will finish current task
    elftask = ["", "", "", "", ""] #what task each elf is currently doing
    t = 0 #start at 0 mins
    stepmins = {} #how long each task takes
    for i, step in enumerate(sortsteps):
        stepmins[step] = i + 61
    while newsteps: #while tasks still waiting
        stayatt = 0
        possteps = []
        for step in sortsteps: #find list of possible tasks
            if step not in newpost:
                possteps.append(step)
        for i, e in enumerate(elves): #check what each elf is doing
            if t == e and elftask[i] != "": #if elf has just finished task
                curstep = elftask[i]
                newsteps.remove(curstep) #remove task from waiting list
                for p in post: #remove task from blocking other tasks
                    if p in newpost:
                        waiting = list(newpost[p])
                        if curstep in waiting:
                            waiting.remove(curstep)
                            if waiting:
                                newpost[p] = waiting
                            else: #if a waiting task has nothing blocking it
                                del newpost[p] #remove it from blocked list
                elftask[i] = "" #current elf has no current task
                stayatt = 1 #don't increment time to reevaluate possible tasks
                break
            elif t >= e and possteps: #if an elf is waiting for a task
                newtask = possteps.pop(0) #remove a task from the poss list
                sortsteps.remove(newtask) #remove this task from future lists
                elftask[i] = newtask #elf is currently working on this task
                elves[i] = t + stepmins[newtask] #elf will finish task at this time
        if not stayatt:
            t += 1 #increment time if no elf has just finished a task
    print("Part Two:", t)
            
day = 7
open_file()

formatdata()

run_through_steps()
parallel_work()