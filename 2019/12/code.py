""" https://adventofcode.com/2019/day/12 """

from itertools import combinations

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        lines = [line[1:-2].replace(" ", "").split(",") for line in f.readlines()]
    return [(int(line[0][2:]), int(line[1][2:]), int(line[2][2:])) for line in lines]

def cmp(a,b):
    return 0 if a == b else -1 if a < b else 1

class Moon:
    def __init__(self, pos):
        self.pos = list(pos)
        self.vel = [0] * 3

    def changeGravity(self, other):
        for i in range(3):
            d = cmp(self.pos[i], other.pos[i])
            self.vel[i] -= d
            other.vel[i] += d

    def move(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

    def energy(self):
        pot = sum([abs(p) for p in self.pos])
        kin = sum([abs(v) for v in self.vel])
        return pot, kin, pot * kin

def simulate(moons : list, steps = 1):
    for i in range(steps):
        for m, n in list(combinations(moons, 2)):
            m.changeGravity(n)
        
        for moon in moons:
            moon.move()

def lcm(x, y):
    tmp = x * y
    while y:
        x, y = y, x % y
    return tmp // x
        
def part1(vals: list):
    moons = [Moon(val) for val in vals]
    simulate(moons, 1000)
    return sum([moon.energy()[2] for moon in moons])

def part2(vals: list):
    dims = [0, 0, 0]
    for i in range(3):
        moons = [Moon(val) for val in vals]
        oPos = [moon.pos[i] for moon in moons]

        while 1:
            simulate(moons)
            dims[i] += 1
            if [moon.pos[i] for moon in moons] == oPos and \
                [moon.vel[i] for moon in moons] == [0, 0, 0, 0]:
                break

    return lcm(dims[0], lcm(dims[1], dims[2]))

def test():
    moons = [Moon(p) for p in ((-1,0,2), (2,-10,-7), (4,-8,8), (3,5,-1))]
    simulate(moons, 10)
    assert sum([moon.energy()[2] for moon in moons]) == 179
    vpos, vvel = ([2,1,-3],[1,-8,0],[3,-6,1],[2,0,4]), ([-3,-2,1],[-1,1,3],[3,2,-3],[1,-1,-1])
    for i in range(4):
        assert vpos[i] == moons[i].pos and vvel[i] == moons[i].vel
    moons = [Moon(p) for p in ((-8,-10,0), (5,5,10), (2,-7,3), (9,-8,-3))]    
    simulate(moons,100)
    assert sum([moon.energy()[2] for moon in moons]) == 1940
    assert part2(((-1,0,2),(2,-10,-7),(4,-8,8),(3,5,-1))) == 2772
    assert part2(((-8,-10,0),(5,5,10),(2,-7,3),(9,-8,-3))) == 4686774924

if __name__ == "__main__":
    test()
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")