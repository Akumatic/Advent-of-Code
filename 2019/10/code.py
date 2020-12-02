# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic
# 
# https://adventofcode.com/2019/day/10

from asteroid import Asteroid
from math import pi

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line[:-1] for line in f.readlines()]

def getAsteroids(field: list, x: int, y: int) -> list:
    return [Asteroid(i,j,x,y) for j in range(len(field)) 
        for i in range(len(field[j])) if field[j][i] != "." and (i,j) != (x,y)]

def getVisibleAsteroids(field: list, x: int, y: int) -> int:
    asteroids = getAsteroids(field, x, y)
    angles = set([asteroid.angle for asteroid in asteroids])
    return len(angles)

def part1(vals: list) -> tuple:
    mx, my, max = 0, 0, 0
    for y in range(len(vals)):
        for x in range(len(vals[0])):
            if vals[y][x] == ".": 
                continue
            tmp = getVisibleAsteroids(vals, x, y)
            if tmp > max:
                mx, my, max = x, y, tmp
    return mx, my, max

def selectStart(indices: list, current: float) -> int:
    i = 0
    while indices[i] < current:
        i += 1
    return i + 1

def part2(vals: list, x: int, y: int, count: int) -> int:
    asteroids = getAsteroids(vals, x, y)
    d = dict()
    for asteroid in asteroids:
        if str(asteroid.angle) in d:
            d[str(asteroid.angle)].append(asteroid)
        else:
            d[str(asteroid.angle)] = [asteroid]

    for a in d:
        d[a].sort(key=lambda x:x.dist, reverse=True)

    idx = list(set([asteroid.angle for asteroid in asteroids]))
    idx.sort()
    
    laser = (selectStart(idx, -pi/2) - 1) % len(idx)
    destroyed = []
    id = str(idx[laser])
    for i in range(count):
        cur = d[id].pop()
        destroyed.append((cur.x, cur.y))
        if not len(d[id]):
            d.pop(id)
        if i < count - 1:
            while 1:
                laser = (laser + 1) % len(idx)
                id = str(idx[laser])
                if id not in d:
                    continue
                if len(d[str(idx[laser])]):
                    break

    return destroyed

def test():
    assert part1([".#..#",".....","#####","....#","...##"]) == (3, 4, 8)
    assert part1(["......#.#.","#..#.#....","..#######.",".#.#.###..",".#..#.....","..#....#.#",
        "#..#....#.",".##.#..###","##...#..#.",".#....####"]) == (5,8,33)
    assert part1(["#.#...#.#.",".###....#.",".#....#...","##.#.#.#.#","....#.#.#.",".##..###.#",
        "..#...##..","..##....##","......#...",".####.###."]) == (1,2,35)
    assert part1([".#..#..###","####.###.#","....###.#.","..###.##.#","##.##.#.#.","....###..#",
        "..#.#..#.#","#..#.#.###",".##...##.#",".....#.#.."]) == (6,3,41)
    tmp = [".#..##.###...#######","##.############..##.",".#.######.########.#",".###.#######.####.#.",
        "#####.##.#.##.###.##","..#####..#.#########","####################","#.####....###.#.#.##",
        "##.#################","#####.##.###..####..","..######..##.#######","####.##.####...##..#",
        ".#####..#.######.###","##...#.##########...","#.##########.#######",".####.#.###.###.#.##",
        "....##.##.###..#####",".#.#.###########.###","#.#.#.#####.####.###","###.##.####.##.#..##"]
    assert part1(tmp) == (11,13,210)
    assert part2([".#....#####...#..","##...##.#####..##","##...#...#.#####.","..#.....X...###..",
        "..#.#.....#....##"], 8, 3, 4*9)[-1] == (14, 3)
    assert part2(tmp, 11,13, 299)[199] == (8,2)
    
if __name__ == "__main__":
    test()
    vals = readFile()
    p1 = part1(vals)
    print(f"Part 1: {p1[2]}")
    p2 = part2(vals, p1[0], p1[1], 200)
    print(f"Part 2: {p2[-1][0] * 100 + p2[-1][1]}")