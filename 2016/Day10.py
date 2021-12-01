def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global bots, steps
    bots = {}
    steps = []
    for line in inputs:
        if "value" in line:
            _, val, *_, bot = line.split(" ")
            val, bot = [int(val), int(bot)]
            if bot not in bots:
                bots[bot] = [val]
            else:
                bots[bot].append(val)
        else:
            bot, rest = line.split(" gives low to ")
            low, high = rest.split(" and high to ")
            _, bot = bot.split(" ")
            low = low.split(" ")
            high = high.split(" ")
            bot, low[1], high[1] = [int(bot), int(low[1]), int(high[1])]
            steps.append([bot, low, high])

def run_steps():
    global outputs
    outputs = {}
    point = 0
    while steps:
        if point >= len(steps):
            point = 0
        step = steps[point]
        point += 1
        bot, low, high = step
        if bot not in bots:
            continue
        micros = tuple(bots[bot])
        if len(bots[bot]) == 2:
            lowval = min(micros)
            highval = max(micros)
            if 61 in micros and 17 in micros:
                print(f"Part One: {bot}")
            if low[0] == "bot":
                if low[1] not in bots:
                    bots[low[1]] = [lowval]
                else:
                    bots[low[1]].append(lowval)
            else:
                outputs[low[1]] = lowval
            if high[0] == "bot":
                if high[1] not in bots:
                    bots[high[1]] = [highval]
                else:
                    bots[high[1]].append(highval)
            else:
                outputs[high[1]] = highval
            bots[bot] = []
            steps.remove(step)
    mult = 1
    for chip in outputs:
        if chip in (0, 1, 2):
            mult *= outputs[chip]
    print(f"Part Two: {mult}")

day = 10
open_file()

format_data()

run_steps()