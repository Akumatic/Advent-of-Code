""" https://adventofcode.com/2019/day/7 """

import queue, itertools

class InvalidOpcode(Exception):
    pass

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

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
                            self.vals[self.vals[self.i+1]] =  self.prev.output
                        else:
                            self.vals[self.vals[self.i+1]] =  self.queue.get(block=False)
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

def amplify(vals : list, phaseSettings : tuple):
    amps = [Amp(vals, phaseSettings[i]) for i in range(5)]
    amps[0].queue.put(0)
    
    for i in range(1, 4):
        amps[i].next = amps[i+1]
        amps[i].prev = amps[i-1]

    amps[0].next = amps[1]
    amps[4].prev = amps[3]

    if phaseSettings[0] > 4:
        amps[4].next = amps[0]
        amps[0].prev = amps[4]

    while not (amps[0].term and amps[1].term and amps[2].term and amps[3].term and amps[4].term):
        for i in range(5):
            if not amps[i].term:
                amps[i].run()

    return amps[4].output

def part1(vals : list):
    return max([amplify(vals, (a, b, c, d, e)) for a,b,c,d,e in itertools.permutations([x for x in range(5)])])

def part2(vals : list):
    return max([amplify(vals, (a, b, c, d, e)) for a,b,c,d,e in itertools.permutations([x for x in range(5,10)])])

def test():
    vals = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    assert amplify(vals, (4,3,2,1,0)) == 43210
    vals = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
        101,5,23,23,1,24,23,23,4,23,99,0,0]
    assert amplify(vals, (0,1,2,3,4)) == 54321
    vals = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
        1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    assert amplify(vals, (1,0,4,3,2)) == 65210
    vals = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
        27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    assert amplify(vals, (9,8,7,6,5)) == 139629729
    vals = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
        -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
        53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    assert amplify(vals, (9,7,8,5,6)) == 18216
     
if __name__ == "__main__":
    test()
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")