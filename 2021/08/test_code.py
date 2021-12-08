# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2, read_file, determine_mapping, determine_output

def test():
    vals = read_file("test_input.txt")
    assert part1(vals) == 26
    print("Passed Part 1")
    mapping_in = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split()
    mapping = {"a": "d", "b": "e", "c": "a", "d": "f", "e": "g", "f": "b", "g": "c"}
    assert determine_mapping(mapping_in) == mapping
    print("Passed mapping test")
    decode_test_values = {"cdfeb": 5, "fcadb": 3, "cdfeb": 5, "cdbaf": 3}
    decode_mapping = {mapping[key]:key for key in mapping}
    assert all(determine_output(val, decode_mapping) == decode_test_values[val] for val in decode_test_values)
    print("Passed output test")
    assert part2(vals) == 61229
    print("Passed Part 2")

if __name__ == "__main__":
    test()