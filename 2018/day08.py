""" https://adventofcode.com/2018/day/8 """

def readFile():
    import os.path as p
    dName = p.dirname(__file__)
    fName = p.basename(__file__).split(".")[0]

    with open(p.join(dName, "input", f"{fName}.txt"), "r") as f:
        data = f.read()
        return [int(val) for val in data.split(" ")]

class Node:
    def __init__(self, numChildren, numMeta):
        self.numChildren = numChildren
        self.children = []
        self.numMeta = numMeta
        self.meta = []

def parse(vals, i):
    nodes = []
    size = len(vals)
    while i < len(vals):
        node = Node(vals[i], vals[i+1])
        i += 2
        if not node.numChildren:
            for m in range(node.numMeta):
                node.meta.append(vals[i + m])
            nodes.append(node)
            i += node.numMeta
            return nodes, i
        else:
            for c in range(node.numChildren):
                temp, i = parse(vals, i)
                node.children += temp
            for m in range(node.numMeta):
                node.meta.append(vals[i + m])
            nodes.append(node)
            i += node.numMeta
            if i >= size:
                return nodes[0]
            else:
                return nodes, i

def part1(node):
    metadata = 0
    for child in node.children:
        metadata += part1(child)
    for meta in node.meta:
        metadata += meta
    return metadata

def part2(node):
    value = 0
    if not node.numChildren:
        for meta in node.meta:
            value += meta
    else:
        for meta in node.meta:
            try:
                value += part2(node.children[meta - 1])
            except IndexError:
                pass
    return value

if __name__ == "__main__":
    vals = readFile()
    #vals = [int(val) for val in "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(" ")]
    node = parse(vals, 0)
    print(f"Part 1: {part1(node)}")
    print(f"Part 2: {part2(node)}")