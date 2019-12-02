""" https://adventofcode.com/2018/day/5 """

def readFile():
    nodes = {}
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        lines =  [(line[5:6], line[36:37]) for line in f.readlines()]
    for l in lines:
        if l[0] not in nodes:
            nodes[l[0]] = Node(l[0])
        if l[1] not in nodes:
            nodes[l[1]] = Node(l[1])
        nodes[l[0]].children.append(nodes[l[1]])
        nodes[l[1]].parents.append(nodes[l[0]])
    return nodes

class Node:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.timeNeeded = ord(name) - 4

class Worker:
    def __init__(self):
        self.working = False
        self.node = None
        self.time = 0

    def work(self):
        self.time -= 1
        if self.time == 0:
            self.working = False

    def setNode(self, node):
        self.node = node
        self.working = True
        self.time = self.node.timeNeeded

def getStartNodes(vals):
    l = []
    for val in vals:
        if len(vals[val].parents) == 0:
            l.append(vals[val])
    return l

def selectNextNode(vals):
    minVal, minIdx = None, -1
    for i in range(len(vals)):
        if minVal is None or ord(vals[i].name) < minVal:
            minVal, minIdx = ord(vals[i].name), i
    return vals[minIdx]
        
def part1(vals):
    order = []
    nodes = getStartNodes(vals)
    while nodes:
        n = selectNextNode(nodes)
        nodes.remove(n)
        order.append(n.name)
        for child in n.children:
            child.parents.remove(n)
            if len(child.parents) == 0:
                nodes.append(child)
    return "".join(order)

def stillWorking(worker):
    for w in worker:
        if w.working:
            return True
    return False

def part2(vals, numOfWorker):
    order = []
    time = 0
    nodes = getStartNodes(vals)
    worker = [Worker() for i in range(numOfWorker)]
    while nodes or stillWorking(worker):
        temp = []
        for w in worker:
            if not w.working:
                if len(nodes) == 0:
                    continue
                else:
                    n = selectNextNode(nodes)
                    w.setNode(n)
                    nodes.remove(n)
            if w.working:
                w.work()
                if not w.working:
                    # finished working
                    order.append(w.node.name)
                    for child in w.node.children:
                        child.parents.remove(w.node)
                        if len(child.parents) == 0:
                            temp.append(child)
        nodes += temp
        time += 1
    return time

if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    vals = readFile()
    print(f"Part 2: {part2(vals, 5)}")