""" https://adventofcode.com/2019/day/13 """

class InvalidOpcode(Exception):
    pass

class mylist(list):
    def __getitem__(self, item):
        try:
            return super(mylist,self).__getitem__(item)
        except IndexError as e:
            if item < 0: raise IndexError()
            super(mylist,self).extend([0]*(item + 1 - super(mylist,self).__len__()))
            return super(mylist,self).__getitem__(item)

    def __setitem__(self, idx, val):
        try:
            return super(mylist,self).__setitem__(idx,val)
        except IndexError as e:
            if idx < 0: raise IndexError()
            super(mylist,self).extend([0]*(idx + 1 - super(mylist,self).__len__()))
            return super(mylist,self).__setitem__(idx,val)

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

def getOutput(vals : list, input=0, base=0):
    vals = mylist(vals)
    i = 0
    out = []
    while 1:
        opcode = (vals[i] % 100,
            vals[i] // 100 % 10,
            vals[i] // 1000 % 10,
            vals[i] // 10000 % 10)

        # 0 Parameter
        if opcode[0] in [99]: # Termination
            return vals, out
        
        # 1 Parameter
        elif opcode[0] in [3,4,9]:
            a = vals[i+1] if not opcode[1] else i+1 if opcode[1] == 1 else base+vals[i+1]
            if opcode[0] == 3: # Input
                vals[a] = input
            elif opcode[0] == 4: # Output
                vals[0] = vals[a]
                out.append(vals[0])
            elif opcode[0] == 9: # Adjust Base
                base += vals[a]
            i += 2

        # 2 Parameter
        elif opcode[0] in [5,6]:
            a = vals[i+1] if not opcode[1] else i+1 if opcode[1] == 1 else base+vals[i+1]
            b = vals[i+2] if not opcode[2] else i+2 if opcode[2] == 1 else base+vals[i+2]
            if opcode[0] == 5 and vals[a] != 0: # Jump-if-true
                i = vals[b]
            elif opcode[0] == 6 and vals[a] == 0: # Jump-if-false
                i = vals[b]
            else:
                i += 3
        
        # 3 Parameter
        elif opcode[0] in [1,2,7,8]:
            a = vals[i+1] if not opcode[1] else i+1 if opcode[1] == 1 else base+vals[i+1]
            b = vals[i+2] if not opcode[2] else i+2 if opcode[2] == 1 else base+vals[i+2]
            c = vals[i+3] if not opcode[3] else i+3 if opcode[3] == 1 else base+vals[i+3]
            if opcode[0] == 1: # Addition
                vals[c] = vals[a] + vals[b]
            elif opcode[0] == 2: # Multiplication
                vals[c] = vals[a] * vals[b]
            elif opcode[0] == 7: # Less Than
                vals[c] = int(vals[a] < vals[b])
            elif opcode[0] == 8: # Equals
                vals[c] = int(vals[a] == vals[b])
            i += 4

        else:
            raise InvalidOpcode()

def getEntities():
    output = getOutput(vals.copy())[1]
    output.reverse()
    assert len(output) % 3 == 0
    entities = [set() for _ in range(5)]
    while output:
        pos = (output.pop(), output.pop())
        tile = output.pop()
        entities[tile].add(pos)
    return entities

def part1(entities):
    print([len(x) for x in entities])
    print(entities[3], entities[4])
    return len(entities[2])

class Ball:
    def __init__(self, x, y):
        self.x, self.y = 0,0
        self.dx, self.dy = 0,0

def part2(entities):
    pass

if __name__ == "__main__":
    vals = readFile()
    entities = getEntities()
    print(f"Part 1: {part1(entities)}")
    #print(f"Part 2: {part2(entities)}")