""" https://adventofcode.com/2018/day/2 """

def readFile():
    l = []
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        line = f.readline()
        while line:
            l.append(line)
            line = f.readline()
    return l

def count(data : dict, n : int):
    sum = 0
    for val in data:
        for char in val:
            if data[val][char] == n:
                sum += 1
                break
    return sum

def part1(vals : list):
    data = {}
    # Count for each letter per word
    for val in vals:
        data[val] = {}
        for char in val:
            if char in data[val]:
                data[val][char] = data[val][char] + 1
            else:
                data[val][char] = 1
    
    return count(data, 2) * count(data, 3)

def getCommonLetters(a : str, b : str):
    lenMin = min(len(a), len(b))
    commons = [a[i] for i in range(lenMin) if a[i] == b[i]]
    return "".join(commons)

def part2(vals : list):
    maxLen = 0
    maxStr = ""
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            cur = getCommonLetters(vals[i], vals[j])
            if len(cur) > maxLen:
                maxLen = len(cur)
                maxStr = cur

    return maxStr

if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")