# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic

class InvalidOpcode(Exception):
    pass

class IndexError(Exception):
    pass

class Data:
    def __init__(self, vals: list):
        self._data = {i:vals[i] for i in range(len(vals))}

    def __getitem__(self, idx):
        if idx < 0:
            raise IndexError("Negative Index")
        if idx in self._data:
            return self._data[idx]
        self._data[idx] = 0
        return 0

    def __setitem__(self, idx, val):
        if idx < 0:
            raise IndexError("Negative Index")
        self._data[idx] = val

    def toList(self):
        return list(self._data.values())

def parseCode(i: int) -> tuple:
    return (i % 100, i // 100 % 10, i // 1000 % 10, i // 10000 % 10)

def getOutput(vals: list, input=0, base=0, full_out: bool = False, 
        getVals: bool = False, output: bool=False) -> int:
    vals = Data(vals)
    i = 0
    out = []
    while True:
        opcode = parseCode(vals[i])

        # 0 Parameter
        if opcode[0] == 99: # Termination
            if output:
                return out
            if getVals:
                return vals.toList()
            if full_out:
                return vals, out
            return vals[0]
        
        # 1 Parameter
        elif opcode[0] in (3,4,9):
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
        elif opcode[0] in (5,6):
            a = vals[i+1] if not opcode[1] else i+1 if opcode[1] == 1 else base+vals[i+1]
            b = vals[i+2] if not opcode[2] else i+2 if opcode[2] == 1 else base+vals[i+2]
            if opcode[0] == 5 and vals[a] != 0: # Jump-if-true
                i = vals[b]
            elif opcode[0] == 6 and vals[a] == 0: # Jump-if-false
                i = vals[b]
            else:
                i += 3
        
        # 3 Parameter
        elif opcode[0] in (1,2,7,8):
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