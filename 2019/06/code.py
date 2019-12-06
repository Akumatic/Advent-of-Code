""" https://adventofcode.com/2019/day/6 """

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        lines = [data[:-1].split(")") for data in f.readlines()]
    return {line[1] : line[0] for line in lines}

def countOrbits(data, cache, node):
    if node in cache: return cache[node]
    cache[node] = 0 if node not in data else 1 + countOrbits(data,cache,data[node])
    return cache[node]

def getIntersection(data, cache, node1, node2):
    if cache[node1] > cache[node2]: node1, node2 = node2, node1
    parents = set()
    # get elements of shorter path
    while data[node1] in data:
        parents.add(data[node1])
        node1 = data[node1]
    parents.add(data[node1])
    # look for first node present in both paths
    while node2 not in parents: 
        node2 = data[node2]
    return node2

def part1(vals : dict, cache):
    return sum([countOrbits(vals,cache,val) for val in vals])

def part2(vals : dict, cache):
    intersection = getIntersection(vals,cache,"YOU","SAN")
    return cache["YOU"] + cache["SAN"] - 2*cache[intersection] - 2

def test():
    vals, cache = {"B":"COM","C":"B","D":"C","E":"D","F":"E","G":"B",
        "H":"G","I":"D","J":"E","K":"J","L":"K"}, {}
    assert countOrbits(vals,cache,"D") == 3
    assert countOrbits(vals,cache,"L") == 7
    assert not countOrbits(vals,cache,"COM")
    assert sum([countOrbits(vals,cache,val) for val in vals]) == 42
    vals["YOU"] = "K"
    vals["SAN"] = "I"
    countOrbits(vals,cache,"YOU"), countOrbits(vals,cache,"SAN")
    assert getIntersection(vals,cache,"YOU","SAN") == "D"
    assert countOrbits(vals,cache,"YOU") + countOrbits(vals,cache,"SAN") - \
        2*cache["D"] == 6

if __name__ == "__main__":
    test()
    vals, cache = readFile(), {}
    print(f"Part 1: {part1(vals, cache)}")
    print(f"Part 2: {part2(vals, cache)}")