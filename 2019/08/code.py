""" https://adventofcode.com/2019/day/8 """

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return f.read()[:-1]

def getLayers(input, width, height):
    layers = []
    for i in range(0, len(input), width*height):
        layers.append([input[i+width*x:i+width*(x+1)] for x in range(height)])
    return layers

def getPicture(layers):
    width, height = len(layers[0][0]), len(layers[0])
    return "\n".join(["".join([getColor(layers, w, h) for w in range(width)]) for h in range(height)])
    
def getColor(layers, w, h):
    for layer in layers:
        if layer[h][w] != "2": return layer[h][w]
    return "2"

def part1(layers):
    min, minLayer = None, None
    for layer in layers:
        cnt = sum([l.count("0") for l in layer])
        if min is None or cnt < min:
            min, minLayer = cnt, layer
    return sum([l.count("1") for l in minLayer]) * sum([l.count("2") for l in minLayer])

def part2(layers):
    picture = getPicture(layers)
    return f"\n{picture.replace('0', ' ').replace('1', 'X')}"

def test():
    assert getLayers("123456789012",3,2) == [["123","456"],["789","012"]]
    assert getPicture(getLayers("0222112222120000",2,2)) == "01\n10"

if __name__ == "__main__":
    test()
    vals = getLayers(readFile(), 25, 6)
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")