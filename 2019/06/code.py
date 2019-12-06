""" https://adventofcode.com/2019/day/6 """

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [data[:-1].split(")") for data in f.readlines()]

def parse(lines):
    data = {}
    for line in lines:
        data[line[1]] = line[0]
    return data

def countOrbits(data, node):
    if node not in data:
        return 0
    return 1 + countOrbits(data, data[node])

def getIntersection(data, node1, node2):
    node = node1
    parents = []

    while data[node] in data:
        parents.append(data[node])
        node = data[node]
    parents.append(data[node])

    node = node2
    while node not in parents:
        node = data[node]
    
    return node

def getJumps(data, start, goal, intersection):
    iDist = countOrbits(data, intersection)
    return countOrbits(data, start) + countOrbits(data, goal) - 2*iDist - 2

def part1(vals : list):
    return sum([countOrbits(vals, val) for val in vals])

def part2(vals : list):
    intersection = getIntersection(vals, "YOU", "SAN")
    return getJumps(vals, "YOU", "SAN", intersection)

def test():
    lines = [["COM","B"],["B","C"],["C","D"],["D","E"],["E","F"],
        ["B","G"],["G","H"],["D","I"],["E","J"],["J","K"],["K","L"]]
    vals = parse(lines)
    assert countOrbits(vals, "D") == 3
    assert countOrbits(vals, "L") == 7
    assert countOrbits(vals, "COM") == 0
    assert sum([countOrbits(vals, val) for val in vals]) == 42
    vals["YOU"] = "K"
    vals["SAN"] = "I"
    assert getIntersection(vals, "YOU", "SAN") == "D"
    assert getJumps(vals, "YOU", "SAN", "D") == 4

if __name__ == "__main__":
    test()
    vals = parse(readFile())
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")