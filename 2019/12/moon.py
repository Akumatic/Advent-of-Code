# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic

def cmp(a: int, b: int) -> int:
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