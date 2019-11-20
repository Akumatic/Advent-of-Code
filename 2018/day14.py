""" https://adventofcode.com/2018/day/14 """

def readFile():
    import os.path as p
    dName = p.dirname(__file__)
    fName = p.basename(__file__).split(".")[0]

    with open(p.join(dName, "input", f"{fName}.txt"), "r") as f:
        return f.read()

def part1(vals):
    border = int(vals)
    scores = [3, 7]
    elf1 = 0
    elf2 = 1
    i = 2

    while i < border + 10:
        new = scores[elf1] + scores[elf2]
        if new > 9:
            scores.append(new // 10)
            scores.append(new % 10)
            i += 2
        else:
            scores.append(new)
            i += 1
        elf1 = (elf1 + 1 + scores[elf1]) % i
        elf2 = (elf2 + 1 + scores[elf2]) % i

    return "".join([str(i) for i in scores[border:border + 10]])

def part2(vals):
    size = len(vals)
    comp = [int(c) for c in vals]
    scores = [3, 7]
    elf1 = 0
    elf2 = 1
    i = 2

    while True:
        new = scores[elf1] + scores[elf2]
        if new > 9:
            scores.append(new // 10)
            scores.append(new % 10)
            i += 2
            if scores[-(size + 1):-1] == comp:
                return i - (size + 1)
        else:
            scores.append(new)
            i += 1

        if scores[-size:] == comp:
            return i - size
        elf1 = (elf1 + 1 + scores[elf1]) % i
        elf2 = (elf2 + 1 + scores[elf2]) % i

if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")