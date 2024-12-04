def set_up_grid():
    maxx, maxy = [300, 300]
    global fcs, csum
    fcs = []
    csum = {}
    for y in range(maxy):
        y += 1
        row = []
        for x in range(maxx):
            x += 1
            pos = (x, y)
            rackID = x + 10
            power = (((((rackID * y) + serialN) * rackID) % 1000) // 100) - 5
            row.append(power)
            if (x, y-1) in csum:
                powsum = csum[(x, y-1)] + sum(row)
            else:
                powsum = sum(row)
            csum[pos] = powsum
        fcs.append(row)

def slice_nxn():
    maxpow = -100
    for n in range(300):
        n += 1
        maxx, maxy = [301-n, 301-n]
        for x in range(maxx):
            for y in range(maxy):
                cornpos = (x+1, y+1, n)
                br = (x+n, y+n)
                bl = (x, y+n)
                tr = (x+n, y)
                if x == 0 and y == 0:
                    sumpow = csum[br]
                elif x == 0:
                    sumpow = csum[br] - csum[tr]
                elif y == 0:
                    sumpow = csum[br] - csum[bl]
                else:
                    sumpow = csum[br] - csum[bl] - csum[tr] + csum[(x, y)]
                if sumpow > maxpow:
                    bestpos = cornpos
                    maxpow = sumpow
        if n == 3:
            *xy, _ = bestpos
            print("Part One:", xy)
    print("Part Two:", bestpos)

serialN = 4842

set_up_grid()
slice_nxn()
