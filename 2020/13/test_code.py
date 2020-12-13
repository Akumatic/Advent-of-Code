# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

from code import part1, part2

def getDict(input):
    input = input.strip().split(",")
    return [{"value": int(input[i]), "index": i} 
        for i in range(len(input))
        if input[i] != "x"]

def test():
    input = (939, "7,13,x,x,59,x,31,19")
    timestamp = input[0]
    bus_ids = getDict(input[1])
    assert part1(timestamp, bus_ids) == 295
    assert part2(bus_ids) == 1068781
    print(f"Passed test for ({input[0]}, [{input[1]}])")

    input = "17,x,13,19"
    bus_ids = getDict(input)
    assert part2(bus_ids) == 3417
    print(f"Passed test for [{input}]")

    input = "67,7,59,61"
    bus_ids = getDict(input)
    assert part2(bus_ids) == 754018
    print(f"Passed test for [{input}]")

    input = "67,x,7,59,61"
    bus_ids = getDict(input)
    assert part2(bus_ids) == 779210
    print(f"Passed test for [{input}]")

    input = "67,7,x,59,61"
    bus_ids = getDict(input)
    assert part2(bus_ids) == 1261476
    print(f"Passed test for [{input}]")

    input = "1789,37,47,1889"
    bus_ids = getDict(input)
    assert part2(bus_ids) == 1202161486
    print(f"Passed test for [{input}]")

if __name__ == "__main__":
    test()