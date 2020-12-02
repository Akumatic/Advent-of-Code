# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic
#
# https://adventofcode.com/2019/day/3

from wire import Wire

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [Wire(val for val in line[:-1].split(",")) for line in f.readlines()]

def getIntersections(a, b) -> set:
    intersections = set()
    bFields = {(val[0], val[1]) for val in b.fields}
    for point in a.fields:
        if point[:2] in bFields:
            intersections.add(point)
    return intersections

def getIntersectionDistance(intersections, i) -> int:
    for intersection in intersections:
        if intersection[0] == i[0] and intersection[1] == i[1]:
            return intersection[2]
                
def part1(vals: list) -> int:
    intersections = getIntersections(vals[0], vals[1])
    dists = []
    for i in intersections:
        dists.append(abs(i[0]) + abs(i[1])) # Manhattan Distance
    dists.sort()
    return dists[1]

def part2(vals: list) -> int:
    intersections = getIntersections(vals[0], vals[1])
    intersections2 = getIntersections(vals[1], vals[0])
    steps = []
    for i in intersections:
        steps.append(i[2] + getIntersectionDistance(intersections2, i))
    steps.sort()
    return steps[1]

def test():
    w1 = Wire([val for val in "R8,U5,L5,D3".split(",")])
    w2 = Wire([val for val in "U7,R6,D4,L4".split(",")])
    assert(part1([w1, w2]) == 6), "Failed 1 - 1"
    assert(part2([w1, w2]) == 30), "Failed 1 - 2"

    w3 = Wire([val for val in "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")])
    w4 = Wire([val for val in "U62,R66,U55,R34,D71,R55,D58,R83".split(",")])
    assert(part1([w3, w4]) == 159), "Failed 2 - 1"
    assert(part2([w3, w4]) == 610), "Failed 2 - 2"

    w5 = Wire([val for val in "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")])
    w6 = Wire([val for val in "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")])
    assert(part1([w5, w6]) == 135), "Failed 3 - 1"
    assert(part2([w5, w6]) == 410), "Failed 3 - 2"

if __name__ == "__main__":
    test()
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")