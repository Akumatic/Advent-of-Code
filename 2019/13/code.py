# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic
# 
# https://adventofcode.com/2019/day/13

import sys, os
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import intcode

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

def getEntities(vals: list):
    assert len(vals) % 3 == 0
    entities = {"empty": [], "wall": [], "block": [],
        "paddle": tuple(), "ball": tuple(), "score": 0}
    keys = tuple(entities.keys())

    for i in range(0, len(vals), 3):
        # updated score
        if (vals[i] == -1 and vals[i+1] == 0):
            entities["score"] = vals[i+2]
            continue
        # updated ball, paddle and other positions
        pos = (vals[i], vals[i+1])
        if vals[i+2] < 3:
            entities[keys[vals[i+2]]].append(pos)
        else:
            entities[keys[vals[i+2]]] = pos

    return entities

def part1(pc: intcode.Computer) -> int:
    pc.run()
    entities = getEntities(pc.output)
    return len(entities["block"])

def part2(pc: intcode.Computer) -> int:
    pc.reset(wait_for_input=True)
    pc.data[0] = 2

    # initial setup
    pc.run()
    idx = pc.output.index(-1)
    while pc.output[idx + 1] != 0:
        idx = pc.output.index(-1, idx + 1)
    entities = getEntities(pc.output[:idx])
    pc.output = pc.output[idx:]

    # loop
    while not pc.stop:
        pc.run()
        changes = getEntities(pc.output)
        if changes["score"]:
            entities["score"] = changes["score"]

        if changes["ball"]:
            changes["empty"].remove(entities["ball"])
            entities["ball"] = changes["ball"]

        if changes["paddle"]:
            changes["empty"].remove(entities["paddle"])
            entities["paddle"] = changes["paddle"]

        for e in changes["empty"]:
            entities["block"].remove(e)

        pc.output.clear()
        pc.input = entities["ball"][0] - entities["paddle"][0]

    return entities["score"]

def test():
    test_input = [1, 2, 3, 6, 5, 4]
    test_output = getEntities(test_input)
    assert test_output["empty"] == test_output["wall"] == test_output["block"] == []
    assert test_output["paddle"] == (1, 2) and test_output["ball"] == (6, 5)

if __name__ == "__main__":
    test()
    pc = intcode.Computer(readFile())
    print(f"Part 1: {part1(pc)}")
    print(f"Part 2: {part2(pc)}")