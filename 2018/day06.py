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

class Location:
    maxDist = 0
    def __init__(self, x, y):
        self.distance = 0
        self.x = x
        self.y = y
        self.inRegion = True

    def addDistance(self, point):
        self.distance += point.getDistance(self.x, self.y)
        if self.distance >= Location.maxDist:
            self.inRegion = False

def part2(vals, maxDist):
    x, y = [val.x for val in vals], [val.y for val in vals]
    minx, maxx, miny, maxy = min(x), max(x), min(y), max(y)
    Location.maxDist = maxDist

    locations = []
    for j in range(miny, maxy + 1):
        for i in range(minx, maxx + 1):
            loc = Location(i, j)
            for point in vals:
                loc.addDistance(point)
            locations.append(loc)

    count = 0
    for loc in locations:
        if loc.inRegion:
            count += 1
    return count

if __name__ == "__main__":
    vals, maxDist = readFile(), 10000
    #vals, maxDist = [Point(1, 1), Point(1, 6), Point(8, 3), Point(3, 4), 
    #   Point(5, 5), Point(8, 9)], 32
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals, maxDist)}")