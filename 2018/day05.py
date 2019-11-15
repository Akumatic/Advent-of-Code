""" https://adventofcode.com/2018/day/5 """

def readFile():
    import os.path as p
    dName = p.dirname(__file__)
    fName = p.basename(__file__).split(".")[0]

    with open(p.join(dName, "input", f"{fName}.txt"), "r") as f:
        return list(f.read())

def part1(vals):
    i = 0
    while i < len(vals) - 1:
        if vals[i].lower() == vals[i+1].lower() and vals[i] != vals[i+1]:
            vals.pop(i)
            vals.pop(i)
            i = max(i - 1, 0)
        else:
            i += 1
    return len(vals)

def part2(vals):
    l = []
    for i in range(65, 91):
        temp = list("".join(vals).replace(chr(i), "").replace(chr(i+32), ""))
        l.append(part1(temp))
    return min(l)

if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")