# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic

from code import read_file, part1, part2

def test():
    root = read_file("test_input.txt")
    assert root.get_size() == 48381165
    assert root.children["d"].get_size() == 24933642
    assert root.children["a"].get_size() == 94853
    assert root.children["a"].children["e"].get_size() == 584
    print("Passed Tree Bulding")
    assert part1(root) == 95437
    print("Passed Part 1")
    assert part2(root) == 24933642
    print("Passed Part 2")

if __name__ == "__main__":
    test()
