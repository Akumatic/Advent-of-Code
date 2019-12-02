""" https://adventofcode.com/2018/day/11 """

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return int(f.read())

def getPowerlevel(x, y, serial):
    rackId = x + 10
    powerLevel = (rackId * y + serial) * rackId
    return (int(powerLevel / 100) % 10) - 5

def createGrid(serial):
    grid = []
    for j in range(1, 301):
        row = []
        for i in range(1, 301):
            row.append(getPowerlevel(i, j, serial))
        grid.append(row)
    return grid

def getBiggestField(grid, size):
    maxSum = 0
    maxCoords = (-1, -1)
    for j in range(300 - size + 1):
        for i in range(300 - size + 1):
            curSum = 0
            for n in range(size):
                for m in range(size):
                    curSum += grid[j + m][i + n]
            if curSum > maxSum:
                maxSum = curSum
                maxCoords = (i + 1, j + 1)
    return maxCoords, maxSum

def getSat(grid):
    # generates and returns summed-area table
    sat = {}
    size = len(grid)
    for j in range(size):
        for i in range(size):
            value = grid[j][i] + sat.get(str((i - 1, j)), 0) 
            value += sat.get(str((i, j - 1)), 0) - sat.get(str((i - 1, j - 1)), 0)
            sat[str((i, j))] = value
    return sat

def getBiggestFieldSAT(sat, size):
    maxSum = 0
    maxCoords = (-1, -1)
    for j in range(300 - size):
        for i in range(300 - size):
            ip, jp = i + size, j + size
            curSum = sat[str((i, j))] + sat[str((ip, jp))] - sat[str((ip, j))] - sat[str((i, jp))]
            if curSum > maxSum:
                maxSum = curSum
                maxCoords = (i + 2, j + 2)
    return maxCoords, maxSum

def part1(value):
    grid = createGrid(value)
    return getBiggestField(grid, 3)[0]

def part2(value):
    grid = createGrid(value)
    sat = getSat(grid)
    maxSum = 0
    size = -1
    maxCoords = (-1, -1)
    for i in range(300):
        curCoords, curSum = getBiggestFieldSAT(sat, i)
        if curSum > maxSum:
            maxSum = curSum
            size = i
            maxCoords = curCoords
    return (maxCoords[0], maxCoords[1], size)

if __name__ == "__main__":
    value = readFile()
    print(f"Part 1: {part1(value)}")
    print(f"Part 2: {part2(value)}")