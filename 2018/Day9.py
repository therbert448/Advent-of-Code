def play(marbles):
    clock = {0: [0, 0]}
    pscores = [0 for _ in range(players)]
    current = 0
    for i in range(marbles):
        marb = i + 1
        if marb % 23:
            rightone = clock[current][1]
            righttwo = clock[rightone][1]
            clock[rightone][1] = marb
            clock[righttwo][0] = marb
            clock[marb] = [rightone, righttwo]
            current = marb
        else:
            player = i % players
            pscores[player] += marb
            for _ in range(7):
                current = clock[current][0]
            left = clock[current][0]
            nextcurrent = clock[current][1]
            pscores[player] += current
            clock[left][1] = nextcurrent
            clock[nextcurrent][0] = left
            current = nextcurrent
    return max(pscores)         

players = 479
marbles1 = 71035
marbles2 = 7103500

print("Part One:", play(marbles1))
print("Part Two:", play(marbles2))