""" https://adventofcode.com/2018/day/10 """

def readFile():
    import os.path as p
    dName = p.dirname(__file__)
    fName = p.basename(__file__).split(".")[0]

    with open(p.join(dName, "input", f"{fName}.txt"), "r") as f:
        lines = f.readlines()
        points = []
        for line in lines:
            points.append(Point(
                int(line[10:16]), int(line[18:24]), # position
                int(line[36:38]), int(line[40:42])  # velocity
            ))
        return points

class Point:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def move(self, reverse = False):
        if reverse:
            self.px -= self.vx
            self.py -= self.vy
        else:
            self.px += self.vx
            self.py += self.vy

def getBorderSizeX(vals, getMin = False):
    minimum, maximum = None, None
    for point in vals:
        if minimum is None or point.px < minimum:
            minimum = point.px
        if maximum is None or point.px > maximum:
            maximum = point.px
    if not getMin:
        return maximum - minimum
    else:
        return maximum - minimum, minimum

def getBorderSizeY(vals, getMin = False):
    minimum, maximum = None, None
    for point in vals:
        if minimum is None or point.py < minimum:
            minimum = point.py
        if maximum is None or point.py > maximum:
            maximum = point.py
    if not getMin:
        return maximum - minimum
    else:
        return maximum - minimum, minimum

def solve(vals):
    oldSizeX, oldSizeY = getBorderSizeX(vals), getBorderSizeY(vals)
    cont = True
    time = 0
    while cont:
        time += 1
        for point in vals:
            point.move()
        sizeX, sizeY = getBorderSizeX(vals), getBorderSizeY(vals)
        if sizeX < oldSizeX or sizeY < oldSizeY:
            oldSizeX = sizeX
            oldSizeY = sizeY
        else:
            cont = False
            time -= 1
            for point in vals:
                point.move(reverse=True)
            sizeX, minX = getBorderSizeX(vals, getMin=True)
            sizeY, minY = getBorderSizeY(vals, getMin=True)


    area = [["." for i in range(sizeX + 1)] for j in range(sizeY + 1)]
    for point in vals:
        area[point.py - minY][point.px - minX] = "#"

    a = []
    for j in range(sizeY + 1):
        b = ["\n"]
        for i in range(sizeX + 1):
            b.append(area[j][i])
        a.append(" ".join(b))
        
    return "".join(a), time

if __name__ == "__main__":
    vals = readFile()
    part1, part2 = solve(vals)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")