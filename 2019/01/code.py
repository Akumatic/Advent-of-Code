""" https://adventofcode.com/2019/day/1 """

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(line[:-1]) for line in f.readlines()]

def part1(vals : list):
    return sum([val // 3 - 2 for val in vals])

def part2(vals : list):
    fuel = [val // 3 - 2 for val in vals]
    for f in fuel:
        temp = f // 3 - 2
        if temp > 0:
            fuel.append(temp)
    return sum(fuel)

if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")