""" https://adventofcode.com/2019/day/10 """

from math import atan2, sqrt, pi

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line[:-1] for line in f.readlines()]

class Asteroid:
    def __init__(self, x: int, y: int, ox: int, oy: int):
        self.x = x
        self.y = y
        self.dist = sqrt((x - ox)**2 + (y - oy)**2)
        self.angle = atan2(y - oy, x - ox)
    
    def __str__(self):
        return str((self.x, self.y))

def getAsteroids(field: list, x: int, y: int):
    return [Asteroid(i,j,x,y) for j in range(len(field)) 
        for i in range(len(field[j])) if field[j][i] != "." and (i,j) != (x,y)]

def getVisibleAsteroids(field: list, x: int, y: int):
    asteroids = getAsteroids(field, x, y)
    angles = set([asteroid.angle for asteroid in asteroids])
    return len(angles)

def part1(vals: list):
    mx, my, max = 0, 0, 0
    for y in range(len(vals)):
        for x in range(len(vals[0])):
            if vals[y][x] == ".": 
                continue
            tmp = getVisibleAsteroids(vals, x, y)
            if tmp > max:
                mx, my, max = x, y, tmp
    return mx, my, max

def part2(vals: list, x: int, y: int, count):
    pass

def test():
    assert part1([".#..#",".....","#####","....#","...##"]) == (3, 4, 8)
    assert part1(["......#.#.","#..#.#....","..#######.",".#.#.###..",".#..#.....","..#....#.#",
        "#..#....#.",".##.#..###","##...#..#.",".#....####"]) == (5,8,33)
    assert part1(["#.#...#.#.",".###....#.",".#....#...","##.#.#.#.#","....#.#.#.",".##..###.#",
        "..#...##..","..##....##","......#...",".####.###."]) == (1,2,35)
    assert part1([".#..#..###","####.###.#","....###.#.","..###.##.#","##.##.#.#.","....###..#",
        "..#.#..#.#","#..#.#.###",".##...##.#",".....#.#.."]) == (6,3,41)
    assert part1([".#..##.###...#######","##.############..##.",".#.######.########.#",".###.#######.####.#.",
        "#####.##.#.##.###.##","..#####..#.#########","####################","#.####....###.#.#.##",
        "##.#################","#####.##.###..####..","..######..##.#######","####.##.####...##..#",
        ".#####..#.######.###","##...#.##########...","#.##########.#######",".####.#.###.###.#.##",
        "....##.##.###..#####",".#.#.###########.###","#.#.#.#####.####.###","###.##.####.##.#..##"]) == (11,13,210)
    
if __name__ == "__main__":
    test()
    vals = readFile()
    p1 = part1(vals)
    print(f"Part 1: {p1[2]}")
    print(f"Part 2: {part2(vals, p1[0], p1[1], 200)}")