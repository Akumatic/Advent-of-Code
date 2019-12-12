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
        self.pos = [pos[0], pos[1], pos[2]]
        self.vel = [0] * 3

    def changeGravity(self, other):
        x,y,z = cmp(self.pos[0], other.pos[0]), cmp(self.pos[1], other.pos[1]), cmp(self.pos[2], other.pos[2])
        self.vel[0], other.vel[0] = self.vel[0] - x, other.vel[0] + x
        self.vel[1], other.vel[1] = self.vel[1] - y, other.vel[1] + y
        self.vel[2], other.vel[2] = self.vel[2] - z, other.vel[2] + z

    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[2] += self.vel[2]

    def energy(self):
        pot = abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
        kin = abs(self.vel[0]) + abs(self.vel[1]) + abs(self.vel[2])
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
    moons = [Moon((val[0], val[1], val[2])) for val in vals]
    simulate(moons, 1000)
    return sum([moon.energy()[2] for moon in moons])

def part2(vals: list):
    dims = [0, 0, 0]
    for i in range(3):
        moons = [Moon((val[0], val[1], val[2])) for val in vals]
        oPos = [moons[0].pos[i], moons[1].pos[i], moons[2].pos[i], moons[3].pos[i]]

        while 1:
            simulate(moons)
            dims[i] += 1
            if [moons[0].pos[i], moons[1].pos[i], moons[2].pos[i], moons[3].pos[i]] == oPos and \
                [moons[0].vel[i], moons[1].vel[i], moons[2].vel[i], moons[3].vel[i]] == [0, 0, 0, 0]:
                break

    return lcm(dims[0], lcm(dims[1], dims[2]))

def test():
    moons = [Moon(p) for p in ((-1,0,2), (2,-10,-7), (4,-8,8), (3,5,-1))]
    simulate(moons, 10)
    assert sum([moon.energy()[2] for moon in moons]) == 179
    vpos, vvel = ((2,1,-3),(1,-8,0),(3,-6,1),(2,0,4)), ((-3,-2,1),(-1,1,3),(3,2,-3),(1,-1,-1))
    for i in range(4):
        assert vpos[i] == (moons[i].pos[0], moons[i].pos[1] ,moons[i].pos[2]) and \
            vvel[i] == (moons[i].vel[0], moons[i].vel[1], moons[i].vel[2])
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