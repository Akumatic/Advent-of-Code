# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic

import queue

class InvalidOpcode(Exception):
    pass

class Amp:
    def __init__(self, vals, phase):
        self.vals = vals.copy()
        self.phase = phase
        self.queue = queue.Queue()
        self.output, self.prev, self.next = None, None, None
        self.phased, self.term = False, False
        self.i = 0

    def run(self):
        while 1:
            opcode = (self.vals[self.i] % 100, self.vals[self.i] // 100 % 10, 
                self.vals[self.i] // 1000 % 10, self.vals[self.i] // 10000 % 10)

            # 99 : Termination
            # 0 Parameter
            if opcode[0] == 99:
                self.output = self.vals[0]
                self.term = True
                break

            # 1 : Addition
            # 3 parameter
            elif opcode[0] == 1:
                a = self.vals[self.i+1] if opcode[1] == 0 else self.i+1
                b = self.vals[self.i+2] if opcode[2] == 0 else self.i+2
                self.vals[self.vals[self.i+3]] = self.vals[a] + self.vals[b]
                self.i += 4

            # 2 : Multiplication
            # 3 parameter
            elif opcode[0] == 2:
                a = self.vals[self.i+1] if opcode[1] == 0 else self.i+1
                b = self.vals[self.i+2] if opcode[2] == 0 else self.i+2
                self.vals[self.vals[self.i+3]] = self.vals[a] * self.vals[b]
                self.i += 4

            # 3 : Input
            # 1 parameter
            elif opcode[0] == 3: 
                if self.phased:
                    try:
                        if self.prev and self.prev.output:
                            self.vals[self.vals[self.i+1]] = self.prev.output
                        else:
                            self.vals[self.vals[self.i+1]] = self.queue.get(block=False)
                    except queue.Empty:
                        break
                else:
                    self.vals[self.vals[self.i+1]], self.phased = self.phase, True
                self.i += 2

            # 4 : Output
            # 1 parameter
            elif opcode[0] == 4: 
                a = self.vals[self.i+1] if opcode[1] == 0 else self.i+1
                self.vals[0] = self.vals[a]
                if self.next:
                    self.next.queue.put(self.vals[0])
                self.i += 2

            # 5 : Jump-if-true
            # 6 : Jump-if-false
            # 2 parameter
            elif opcode[0] in [5, 6]:
                a = self.vals[self.i+1] if opcode[1] == 0 else self.i+1
                if opcode[0] == 5 and self.vals[a] or \
                opcode[0] == 6 and not self.vals[a]:
                    b = self.vals[self.i+2] if opcode[2] == 0 else self.i+2
                    self.i = self.vals[b]
                else:
                    self.i += 3

            # 7 : less-than
            # 8 : equals
            # 3 parameter
            elif opcode[0] in [7, 8]:
                a = self.vals[self.i+1] if opcode[1] == 0 else self.i+1
                b = self.vals[self.i+2] if opcode[2] == 0 else self.i+2
                self.vals[self.vals[self.i+3]] = 1 if opcode[0] == 7 and self.vals[a] < \
                    self.vals[b] or opcode[0] == 8 and self.vals[a] == self.vals[b] else 0
                self.i += 4
            
            else:
                raise InvalidOpcode