def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global stream
    stream = file.read().strip()
    file.close()

def find_groups():
    global groupcount, garbcount
    groupcount = 0  #sum of group levels for part one
    garbcount = 0   #sum of characters in garbage for part two
    gcount = 0      #intermediate sum for each piece of garbage
    point = 0       #points to current char in the stream
    level = 0       #how many groups in
    garbage = 0     #flag for if we're in garbage
    streamlen = len(stream)
    while point < streamlen: #whilst we're still going through the stream
        char = stream[point] #which character are we looking at
        if garbage: #we're in garbage
            if char == "!": #cancel chars by skipping the char
                point += 2
                continue
            elif char == ">": #if we're legitimately at the end of the garbage
                garbcount += gcount #add the garbage char count
                garbage = 0 #set garbage flag back to 0
                point += 1
                continue
            gcount += 1 #if not ! or >, count the character
            point += 1
            continue
        if char == "{": #opening of new group, increase the level
            level += 1
            groupcount += level #for each group add the level to group sum
        elif char == "}":
            level -= 1 #end of group, decrease the level
        elif char == "<":
            garbage = 1 #entered garbage, set flag to ignore characters within
            gcount = 0 #start the intermediate garbage character count
        point += 1
    print("Part One:", groupcount)
    print("Part Two:", garbcount)

day = 9
open_file()

find_groups()