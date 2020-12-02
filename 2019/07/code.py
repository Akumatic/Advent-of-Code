# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic
# 
# https://adventofcode.com/2019/day/7

from itertools import permutations
from amp import Amp

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

def amplify(vals: list, phaseSettings: tuple) -> int:
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

def part1(vals: list) -> int:
    return max([amplify(vals, (a, b, c, d, e)) for a,b,c,d,e in permutations([x for x in range(5)])])

def part2(vals: list) -> int:
    return max([amplify(vals, (a, b, c, d, e)) for a,b,c,d,e in permutations([x for x in range(5,10)])])

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