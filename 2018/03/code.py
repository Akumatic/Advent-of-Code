""" https://adventofcode.com/2018/day/3 """

def readFile():
    l = []
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        line = f.readline()
        while line:
            s = line.split(" ")
            dist = s[2].split(",")
            size = s[3].split("x")
            fields = []
            for i in range(int(dist[0]), int(dist[0]) + int(size[0])):
                for j in range(int(dist[1][:-1]), int(dist[1][:-1]) + int(size[1])):
                    fields.append((i, j))

            l.append({
                "id" : int(s[0][1:]),
                "fields" : fields
            })
            line = f.readline()
    return l

def part1(vals : list):
    data = {}
    # get count for every field
    for val in vals:
        for field in val["fields"]:
            f = str(field)
            if f in data:
                data[f] += 1
            else:
                data[f] = 1
                
    # count fields with count higher than one
    overlap = 0
    for d in data:
        if data[d] > 1:
            overlap += 1
    
    return overlap
    
def part2(vals : list):
    data = {}
    # get count for every field
    for val in vals:
        for field in val["fields"]:
            f = str(field)
            if f in data:
                data[f] += 1
            else:
                data[f] = 1
    
    # look for area covered by only one id
    for val in vals:
        check = True
        for field in val["fields"]:
            if data[str(field)] > 1:
                check = False
                break
        if check:
            return val["id"]

if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")