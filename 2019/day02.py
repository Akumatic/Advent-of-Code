""" https://adventofcode.com/2019/day/2 """

def readFile():
    import os.path as p
    dName = p.dirname(__file__)
    fName = p.basename(__file__).split(".")[0]

    with open(p.join(dName, "input", f"{fName}.txt"), "r") as f:
        return [int(num) for num in f.readline().split(",")]

def getOutput(vals : list):
    for i in range(0, len(vals), 4):
        if vals[i] == 99:
            break
        elif vals[i] == 1:
            vals[vals[i+3]] = vals[vals[i+1]] + vals[vals[i+2]]
        else: # vals[i] == 2
            vals[vals[i+3]] = vals[vals[i+1]] * vals[vals[i+2]]
    return vals[0]

def part1(vals : list):
    memory = vals.copy()
    memory[1], memory[2] = 12, 2
    return getOutput(memory)

def part2(vals : list):
    for noun in range(100):
        for verb in range(100):
            memory = vals.copy()
            memory[1], memory[2] = noun, verb
            if getOutput(memory) == 19690720:
                return 100 * noun + verb

if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")