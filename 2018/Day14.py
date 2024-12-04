def part_one():
    inputs = int(instring)
    elfone = 0
    elftwo = 1
    scores = [3, 7]
    scorelen = len(scores)
    while scorelen < inputs + 10:
        recone = scores[elfone]
        rectwo = scores[elftwo]
        recsum = recone + rectwo
        if recsum//10 == 1:
            scores.append(1)
            scores.append(recsum % 10)
        else:
            scores.append(recsum % 10)
        scorelen = len(scores)
        elfone = (elfone + 1 + recone) % scorelen
        elftwo = (elftwo + 1 + rectwo) % scorelen
    print("Part One:", "".join(str(val) for val in scores[inputs:inputs+10]))

def part_two():
    lenstr = len(instring)
    elfone = 0
    elftwo = 1
    scores = [3, 7]
    found = 0
    scorelen = len(scores)
    while not found:
        recone = scores[elfone]
        rectwo = scores[elftwo]
        recsum = recone + rectwo
        if recsum//10 == 1:
            scores.append(1)
            scores.append(recsum % 10)
            scorelen = len(scores)
            string1 = "".join(str(val) for val in scores[-(lenstr+1):-1])
            
            if string1 == instring:
                print("Part Two:", scorelen - (lenstr+1))
                break
        else:
            scores.append(recsum % 10)
            scorelen = len(scores)
        string = "".join(str(val) for val in scores[-lenstr:])
        if string == instring:
            print("Part Two:", scorelen - (lenstr))
            break
        elfone = (elfone + 1 + recone) % scorelen
        elftwo = (elftwo + 1 + rectwo) % scorelen

instring = "170641"

part_one()
part_two()