def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    global inputs
    inputs = [line.strip() for line in file.readlines()]
    file.close()

def format_data():
    global layers, severity
    layers = {}
    severity = 0
    for line in inputs:
        layer, length = line.split(": ")
        layer, length = [int(layer), int(length)]
        layers[layer] = length
        timing = (length - 1) * 2 #how often it returns to the top row
        if not layer % timing:
            severity += layer * length
    print("Part One:", severity)

def iterate_delays():
    delay = 0
    caught = 1
    while caught:
        delay += 1
        caught = 0
        for layer in layers:
            length = layers[layer]
            timing = (length - 1) * 2 
            if not (layer + delay) % timing:
                #adding a delay effectively shifts each layer deeper
                caught = 1
                break
    print("Part Two:", delay)

day = 13
open_file()

format_data()

iterate_delays() #not so slow that another method is needed