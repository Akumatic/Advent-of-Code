""" https://adventofcode.com/2018/day/6 """

def readFile():
    import os.path as p
    dName = p.dirname(__file__)
    fName = p.basename(__file__).split(".")[0]

    with open(p.join(dName, "input", f"{fName}.txt"), "r") as f:
        lines = [line[:-1].split(", ") for line in f.readlines()]
        return [Point(int(line[0]), int(line[1])) for line in lines]

class Point:
    n = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = str(Point.n).zfill(3)
        Point.n += 1
        self.coords = (x, y)
        self.isInfinite = False


    def getDistance(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

def getMinimumOfDict(data : dict):
    minVal = None
    minID = None
    for d in data:
        if minVal is None or data[d] < minVal:
            minVal = data[d]
            minID = d
    return minVal, minID

def part1(vals):
    x, y = [val.x for val in vals], [val.y for val in vals]
    minx, maxx, miny, maxy = min(x), max(x), min(y), max(y)

    field = []
    for y in range(miny, maxy + 1):
        field.append([-1 for x in range(minx, maxx + 1)])

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            dist = {}
            for val in vals:
                dist[val.name] = val.getDistance(x, y)
            minDist, point = getMinimumOfDict(dist)
            
            if sum(value == minDist for value in dist.values()) == 1:
                field[y-miny][x-minx] = point

    points = {}
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            id = field[y-miny][x-minx]
            if id == -1:
                continue
            if id in points:
                points[id]["value"] += 1
                if not points[id]["border"]:
                    points[id]["border"] = x == minx or x == maxx or y == miny or y == maxy
            else:
                points[id] = {
                    "value": 1,
                    "border": x == minx or x == maxx or y == miny or y == maxy
                }

    result = -1
    for point in points:
        if points[point]["border"]:
            continue
        if points[point]["value"] > result:
            result = points[point]["value"]

    return result

def part2(vals):
    pass

if __name__ == "__main__":
    vals = readFile()
    #vals = [Point(1, 1), Point(1, 6), Point(8, 3), Point(3, 4), Point(5, 5), Point(8, 9)]
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")