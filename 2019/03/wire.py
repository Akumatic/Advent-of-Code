# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic

class Wire:
    def __init__(self, input):
        self.input = input
        self.fields = {(0, 0, 0)}
        self.__initFields()

    def __initFields(self):
        x, y, step = 0, 0, 0
        for i in self.input:
            dir = i[0]
            len = int(i[1:])
            dx = 1 if dir == "R" else -1 if dir == "L" else 0
            dy = 1 if dir == "U" else -1 if dir == "D" else 0
            for r in range(0, len):
                x += dx
                y += dy
                step += 1
                self.fields.add((x, y, step))