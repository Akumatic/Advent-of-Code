""" https://adventofcode.com/2018/day/12 """

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        lines = [line[:-1] for line in f.readlines()]
    state = list(lines[0][15:])
    rules = [Rule(line) for line in lines[2:] if line[9] == "#"]
    return (state, rules)

def getTest():
    stateString = "initial state: ...#..#.#..##......###...###..........."
    ruleStrings = ["...## => #", "..#.. => #", ".#... => #", ".#.#. => #", 
        ".#.## => #", ".##.. => #", ".#### => #", "#.#.# => #", "#.### => #", 
        "##.#. => #", "##.## => #", "###.. => #", "###.# => #", "####. => #"]
    state = list(stateString[15:])
    rules = [Rule(rule) for rule in ruleStrings]
    return (state, rules)

class Rule:
    def __init__(self, string):
        self.left = string[:2]
        self.center = string[2]
        self.right = string[3:5]
        self.rule = list(self.left + self.center + self.right)
        self.result = string[9]

    def compare(self, state):
        return self.rule == state

def part1(vals, generations, offset = 0, printGen = False):
    generation = vals[0]
    pad = ["."]

    if generation[-1] == "#":
        generation += [".", "."]
    elif generation[-2] == "#":
        generation.append(".")

    if printGen:
        print(f" 0: {''.join(generation)}")

    for i in range(generations):
        size = len(generation)
        cur = ["." for j in range(size)]
        for j in range(size):
            if j < 2: # pad left side with empty pods
                temp = pad*(2 - j) + generation[:(3 + j)]
            elif j > size - 3: # pad right side with empty pods
                diff = size - j
                temp = generation[(size-2-diff):] + pad*(3-diff)
            else:
                temp = generation[j-2:j+3]
            
            for rule in vals[1]:
                if rule.compare(temp):
                    cur[j] = rule.result
                    break
        
        if cur[-1] == "#":
            cur += [".", "."]
        elif cur[-2] == "#":
            cur.append(".")

        generation = cur

        if printGen:
            print(f"{i + 1 if i + 1 > 9 else f' {i + 1}'}: {''.join(generation)}")
    
    return sum(i - offset for i in range(len(generation)) if generation[i] == "#")

def part2(vals, generations, offset = 0):
    generation = vals[0]
    pad = ["."]

    genSum = sum(i - offset for i in range(len(generation)) if generation[i] == "#")

    if generation[-1] == "#":
        generation += [".", "."]
    elif generation[-2] == "#":
        generation.append(".")

    i = 0
    while True:
        i += 1
        size = len(generation)
        cur = ["." for j in range(size)]
        for j in range(size):
            if j < 2: # pad left side with empty pods
                temp = pad*(2 - j) + generation[:(3 + j)]
            elif j > size - 3: # pad right side with empty pods
                diff = size - j
                temp = generation[(size-2-diff):] + pad*(3-diff)
            else:
                temp = generation[j-2:j+3]
            
            for rule in vals[1]:
                if rule.compare(temp):
                    cur[j] = rule.result
                    break
        
        if cur[-1] == "#":
            cur += [".", "."]
        elif cur[-2] == "#":
            cur.append(".")

        generation = cur

        curSum = sum(i - offset for i in range(len(cur)) if cur[i] == "#")
        if curSum - genSum == 52:
            break
        genSum = curSum

    return curSum + 52*(generations - i)

if __name__ == "__main__":
    print(f"Test:   {part1(getTest(), generations=20, offset=3, printGen=True)}")
    vals = readFile()
    print(f"Part 1: {part1(vals, generations=20)}")
    print(f"Part 2: {part2(vals, generations=5*10**10)}")