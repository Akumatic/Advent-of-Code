""" https://adventofcode.com/2019/day/14 """

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line[:-1] for line in f.readlines()]
    
class Factory:
    def __init__(self):
        self.recipes = dict()
        self.storage = {"ORE": 0}
        self.ores = 0

    def addRecipe(self, recipe):
        left, right = recipe.split(" => ")
        left, right = left.split(", "), right.split()
        self.storage[right[1]] = 0
        self.recipes[right[1]] = {"amount": int(right[0]), "req": {}}
        for l in left:
            l = l.split()
            self.recipes[right[1]]["req"][l[1]] = int(l[0])

    def produce(self, chem="FUEL"):
        if "ORE" in self.recipes[chem]["req"]:
            cur = self.storage["ORE"]
            while self.storage["ORE"] < self.recipes[chem]["req"]["ORE"]:
                self.storage["ORE"] += self.recipes[chem]["req"]["ORE"]
                self.ores += self.recipes[chem]["req"]["ORE"]
            self.storage[chem] += self.recipes[chem]["amount"]
            self.storage["ORE"] -= self.recipes[chem]["req"]["ORE"]

        else:
            for r in self.recipes[chem]["req"]:
                while self.storage[r] < self.recipes[chem]["req"][r]:
                    self.produce(r)
            self.storage[chem] += self.recipes[chem]["amount"]
            for r in self.recipes[chem]["req"]:
                self.storage[r] -= self.recipes[chem]["req"][r]
                while self.storage[r] < 0:
                    self.produce(r)
            return

def part1(vals):
    factory = Factory()
    for val in vals:
        factory.addRecipe(val)
    factory.produce()
    return factory.ores

def part2(vals):
    pass

def test():
    assert part1(["10 ORE => 10 A","1 ORE => 1 B","7 A, 1 B => 1 C","7 A, 1 C => 1 D",
        "7 A, 1 D => 1 E","7 A, 1 E => 1 FUEL"]) ==  31
    assert part1(["9 ORE => 2 A","8 ORE => 3 B","7 ORE => 5 C","3 A, 4 B => 1 AB",
        "5 B, 7 C => 1 BC","4 C, 1 A => 1 CA","2 AB, 3 BC, 4 CA => 1 FUEL"]) == 165
    assert part1(["157 ORE => 5 NZVS","165 ORE => 6 DCFZ","44 XJWVT, 5 KHKGT, 1 QDVJ, 29"
        " NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL","12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ",
        "179 ORE => 7 PSHF","177 ORE => 5 HKGWZ","7 DCFZ, 7 PSHF => 2 XJWVT",
        "165 ORE => 2 GPVTF","3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"]) == 13312

if __name__ == "__main__":
    test()
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")