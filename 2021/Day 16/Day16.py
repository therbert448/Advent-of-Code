"""
Advent of Code
2021 Day 16

@author: Tom Herbert
"""

class Packet:
    def __init__(self, string):
        self.string = string
    
    def get_version(self):
        v = self.string[:3]
        self.version = int(v, 2)
    
    def get_type(self):
        t = self.string[3:6]
        self.type = int(t, 2)
        if self.type == 4:
            self.isLiteral = 1
        else:
            self.isLiteral = 0
    
    def get_literal(self):
        self.endIdx = 0
        idx = 6
        litString = ""
        while not self.endIdx:
            char = self.string[idx]
            litString += self.string[idx+1:idx+5]
            if char == "0":
                self.endIdx = idx + 5
            idx += 5
        self.literal = int(litString, 2)

    def get_operator(self):
        lengthType = self.string[6]
        if lengthType == "0":
            length = int(self.string[7:22], 2)
            self.endIdx = 22
        else:
            length = int(self.string[7:18], 2)
            self.endIdx = 18
        self.operator = (lengthType, length)

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().strip()
    file.close()
    return inputs

def format_data():
    global binString
    binString = ""
    for char in inputs:
        num = int(char, base=16)
        string = str(bin(num))[2:].zfill(4)
        binString += string

def operate(values, opType):
    result = 0
    if opType == 0:
        result = sum(values)
    elif opType == 1:
        result = 1
        for val in values:
            result *= val
    elif opType == 2:
        result = min(values)
    elif opType == 3:
        result = max(values)
    elif opType == 5:
        if values[0] > values[1]:
            result = 1
    elif opType == 6:
        if values[0] < values[1]:
            result = 1
    elif opType == 7:
        if values[0] == values[1]:
            result = 1
    return result

def breakdown_packet(packet):
    packet.get_version()
    versions.append(packet.version)
    packet.get_type()
    if packet.isLiteral:
        packet.get_literal()
        if all([char=="0" for char in packet.string[packet.endIdx:]]):
            return "", packet.literal
        else:
            return packet.string[packet.endIdx:], packet.literal
    else:
        packet.get_operator()
        values = []
        if packet.operator[0] == "0":
            substring = packet.string[22:22+packet.operator[1]]
            while substring:
                newPacket = Packet(substring)
                substring, val = breakdown_packet(newPacket)
                values.append(val)
            substring = packet.string[22+packet.operator[1]:]
        else:
            count = 0
            substring = packet.string[18:]
            while count < packet.operator[1]:
                newPacket = Packet(substring)
                substring, val = breakdown_packet(newPacket)
                values.append(val)
                count += 1
        result = operate(values, packet.type)
        return substring, result

def part_one_and_two():
    global packet, point, versions, literals
    packet = Packet(binString)
    versions = []
    _, result = breakdown_packet(packet)
    print(f"Part One = {sum(versions)}")
    print(f"Part Two = {result}")

day = 16
inputs = open_file()

format_data()

part_one_and_two()