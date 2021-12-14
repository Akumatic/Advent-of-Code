# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2, read_file, count

def count_chars(s: str) -> dict:
    cnt = dict()
    for c in s:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    return cnt

def test():
    vals = read_file("test_input.txt")
    assert count(vals[0], vals[1], 1) == count_chars("NCNBCHB")
    assert count(vals[0], vals[1], 2) == count_chars("NBCCNBBBCBHCB")
    assert count(vals[0], vals[1], 3) == count_chars("NBBBCNCCNBBNBNBBCHBHHBCHB")
    assert count(vals[0], vals[1], 4) == count_chars("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")
    print("Passed Counting")

    elements = count(vals[0], vals[1], 10)
    assert elements == {"B": 1749, "C": 298, "H": 161, "N": 865}
    assert part1(*vals) == 1588
    print("Passed Part 1")
    
    elements = count(vals[0], vals[1], 40)
    assert elements["B"] == 2192039569602
    assert elements["H"] == 3849876073
    assert part2(*vals) == 2188189693529
    print("Passed Part 2")

if __name__ == "__main__":
    test()
