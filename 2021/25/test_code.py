# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import *

def test():
    vals = read_file("test_input.txt")
    assert part1(vals) == 58
    print("Passed Part 1")
        
if __name__ == "__main__":
    test()
