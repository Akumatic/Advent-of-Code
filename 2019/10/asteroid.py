# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic

from math import atan2, sqrt

class Asteroid:
    def __init__(self, x: int, y: int, ox: int, oy: int):
        self.x = x
        self.y = y
        self.dist = sqrt((x - ox)**2 + (y - oy)**2)
        self.angle = atan2(y - oy, x - ox)
    
    def __str__(self):
        return str((self.x, self.y))