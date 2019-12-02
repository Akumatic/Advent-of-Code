""" https://adventofcode.com/2018/day/1 """

def readFile():
    l = []
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        line = f.readline()
        while line:
            l.append(int(line))
            line = f.readline()
    return l

def part1(vals : list):
    sum = 0
    for val in vals:
        sum += val
    return sum

def part2(vals : list):
    sum = 0
    s = {sum}
    while True:
        for val in vals:
            sum += val
            if sum in s:
                return sum
            s.add(sum)
    return sum

if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")