def total_items(floors): 
    #need all items on top floor, so need to know how many items there are
    count = 0
    for floor in floors:
        count += len(floor)
    return count

def identify_state(floors, lift):
    state = []
    for floor in range(numfloors):
        s = [0, 0, 0]
        #number of pairs, number of loose generators, number of loose chips
        for item in floors[floor]:
            if item[1] == "M":
                if item[0] + "G" in floors[floor]:
                    s[0] += 1
                else:
                    s[2] += 1
            elif item[0] + "M" not in floors[floor]:
                s[1] += 1
        state.append(tuple(s))
    state = tuple([*state, lift])
    return state

def try_move(nextfloor, floors, lift, *items):
    #floors is the current state of all items
    #lift is the current position of the lift
    #nextfloor is where the lift is moving to
    #*items are the one or two items being carried in the lift
    newfloors = [set(floor) for floor in floors]
    #copy the old floor layout to make changes
    for item in items:
        #remove each item from the previous floor and put it on the new floor
        newfloors[lift].remove(item)
        newfloors[nextfloor].add(item)
    for itema in newfloors[lift]:
        #check that removing items hasn't made the previous floor invalid
        if "M" in itema and itema[0] + "G" not in newfloors[lift]:
            #if a chip hasn't been paired with its generator on this floor
            for itemb in newfloors[lift]:
                if "G" in itemb:
                    #and another generator is present
                    #the chip will be fried, so invalid state
                    return False
    for itema in newfloors[nextfloor]:
        #same thing with the new floor
        if "M" in itema and itema[0] + "G" not in newfloors[nextfloor]:
            for itemb in newfloors[nextfloor]:
                if "G" in itemb:
                    return False
    #if we haven't returned False by this stage, then this state is valid
    #return the new floor layout
    return newfloors
                

def run_lift():
    global states, allitems
    floors = [set(floor) for floor in initialfloors]
    allitems = total_items(floors) #total number of items to move
    lift = 0 #lift starts on ground floor
    states = {} #keep a record of all previously seen states
    steps = 0 #count the number of steps up to each state
    state = identify_state(floors, lift)
    states[state] = steps
    currentstate = [[floors, lift]] 
    #what's on each floor and where the lift is
    #can have multiple current states, this is a list of all states reachable
    #in the same number of steps
    alltop = 0
    while not alltop:
        steps += 1
        nextstate = [] #which states are we going to start in next round
        for currentfloors in currentstate:
            #for each of the possible starting states
            floors, lift = currentfloors
            #what is on each floor and where is the lift
            if lift == 0: #lift on ground floor, can only move up
                nextfloors = [1]
            elif lift == 3: #lift on top floor, can only move down
                nextfloors = [2]
            else: #lift in the middle, can move up or down
                nextfloors = [lift-1, lift+1]
            itemsset = set() #set of all items and item pairs to move
            #so we don't end up testing the same pair twice
            for itema in floors[lift]:
                #pick up a single item from the current floor
                if itema in itemsset:
                    continue
                itemsset.add(itema)
                for nextfloor in nextfloors:
                    newfloors = try_move(nextfloor, floors, lift, itema)
                    #try to move that one item up or down
                    #could refine this and only ever move down with one item
                    #we should never move one item up
                    if newfloors:
                        #if the move is not invalid
                        topfloor = newfloors[3]
                        #check if all the items will be on the top floor
                        if len(topfloor) == allitems and allitems == 10:
                            #10 items for part one
                            print(f"Part One: {steps}")
                            alltop = 1
                            #end the loop
                            return
                        elif len(topfloor) == allitems and allitems == 14:
                            #14 items for part two
                            print(f"Part Two: {steps}")
                            alltop = 1
                            #end the loop
                            return
                        state = identify_state(newfloors, nextfloor)
                        #translate floor layout into a state
                        if state not in states:
                            #if we haven't seen this state before
                            states[state] = steps
                            #keep a record of this state
                            nextstate.append([newfloors, nextfloor])
                            #add this state to our list of starting points
                            #for the next round
                for itemb in floors[lift]:
                    #pick up another item, try to move a pair
                    if itema == itemb:
                        #can't pick up the same item twice
                        continue
                    items = tuple(sorted([itema, itemb]))
                    #make a note of the pair so we don't try moving it again
                    if items in itemsset:
                        continue
                    itemsset.add(items)
                    for nextfloor in nextfloors:
                        newfloors = try_move(nextfloor, floors, lift, *items)
                        #try to move the pair
                        if newfloors:
                            #if it's a valid move
                            topfloor = newfloors[3]
                            #check the top floor to see if we can stop moving
                            if len(topfloor) == allitems and allitems == 10:
                                print(f"Part One: {steps}")
                                alltop = 1
                                return
                            elif len(topfloor) == allitems and allitems == 14:
                                print(f"Part Two: {steps}")
                                alltop = 1
                                return
                            state = identify_state(newfloors, nextfloor)
                            #save the new state if we haven't seen it before
                            if state not in states:
                                states[state] = steps
                                nextstate.append([newfloors, nextfloor])
        currentstate = list(nextstate)

def part_one():
    global initialfloors
    initialfloors = [{"EG", "EM"},
                     {"AG", "BG", "CG", "DG"},
                     {"AM", "BM", "CM", "DM"},
                     set()]
    run_lift()

def part_two():
    global initialfloors
    initialfloors = [{"EG", "EM", "FG", "FM", "HG", "HM"},
                     {"AG", "BG", "CG", "DG"},
                     {"AM", "BM", "CM", "DM"},
                     set()]
    #two new pairs for part two, final pair is HG/HM, because GG/GM would
    #cause problems
    run_lift()

numfloors = 4 #fixed number of floors

part_one()
part_two()