""" https://adventofcode.com/2019/day/5 """

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

def parseCode(code):
    DE = code % 100
    C = code // 100 % 10
    B = code // 1000 % 10
    A = code // 10000 % 10
    return (DE, C, B, A)

def getOutput(vals : list, input=0, getVals=False):
    i = 0
    while 1:
        opcode = parseCode(vals[i])
        # 99 : Termination
        # 0 Parameter
        if opcode[0] == 99:
            if getVals: 
                return vals
            return vals[0]

        # 1 : Addition
        # 3 parameter
        elif opcode[0] == 1:
            load1 = vals[i+1] if opcode[1] == 0 else i+1
            load2 = vals[i+2] if opcode[2] == 0 else i+2
            vals[vals[i+3]] = vals[load1] + vals[load2]
            i += 4

        # 2 : Multiplication
        # 3 parameter
        elif opcode[0] == 2:
            load1 = vals[i+1] if opcode[1] == 0 else i+1
            load2 = vals[i+2] if opcode[2] == 0 else i+2
            vals[vals[i+3]] = vals[load1] * vals[load2]
            i += 4

        # 3 : Input
        # 1 parameter
        elif opcode[0] == 3: 
            vals[vals[i+1]] = input
            i += 2

        # 4 : Output
        # 1 parameter
        elif opcode[0] == 4: 
            load = vals[i+1] if opcode[1] == 0 else i+1
            vals[0] = vals[load]
            i += 2

        # 5 : Jump-if-true
        # 6 : Jump-if-false
        # 2 parameter
        elif opcode[0] in [5, 6]:
            load1 = vals[i+1] if opcode[1] == 0 else i+1
            if opcode[0] == 5 and vals[load1] or \
            opcode[0] == 6 and not vals[load1]:
                load2 = vals[i+2] if opcode[2] == 0 else i+2
                i = vals[load2]
            else:
                i += 3

        # 7 : less-than
        # 8 : equals
        # 3 parameter
        elif opcode[0] in [7, 8]:
            load1 = vals[i+1] if opcode[1] == 0 else i+1
            load2 = vals[i+2] if opcode[2] == 0 else i+2
            vals[vals[i+3]] = 1 if opcode[0] == 7 and vals[load1] < vals[load2] or \
                opcode[0] == 8 and vals[load1] == vals[load2] else 0
            i += 4

def part1(vals : list):
    return getOutput(vals.copy(), input=1)

def part2(vals : list):
    return getOutput(vals.copy(), input=5)

def test():
    assert parseCode(1001) == (1, 0, 1, 0)
    assert getOutput([1,0,0,0,99]) == 2
    assert getOutput([1,1,1,4,99,5,6,0,99]) == 30
    assert getOutput([3,0,4,0,99], input=42) == 42
    assert getOutput([1101,100,-1,4,0], getVals=True) == [1101,100,-1,4,99]
    assert getOutput([3,9,8,9,10,9,4,9,99,-1,8], input=0) == 0
    assert getOutput([3,9,8,9,10,9,4,9,99,-1,8], input=8) == 1
    assert getOutput([3,9,7,9,10,9,4,9,99,-1,8], input=0) == 1
    assert getOutput([3,9,7,9,10,9,4,9,99,-1,8], input=8) == 0
    assert getOutput([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input=0) == 0
    assert getOutput([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input=1) == 1
    assert getOutput([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input=0) == 0 
    assert getOutput([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input=1) == 1
    assert getOutput([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,
        1101,1000,1,20,4,20,1105,1,46,98,99], input=0) == 999
    assert getOutput([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,
        1101,1000,1,20,4,20,1105,1,46,98,99], input=8) == 1000
    assert getOutput([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,
        1101,1000,1,20,4,20,1105,1,46,98,99], input=9) == 1001

if __name__ == "__main__":
    test()
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")