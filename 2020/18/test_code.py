# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

from code import part1, part2, parse

def test():
    assert parse("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert parse("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert parse("2 * 3 + (4 * 5)") == 26
    assert parse("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert parse("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert parse("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
    print(f"Passed part 1")

    assert parse("1 + 2 * 3 + 4 * 5 + 6", precedence=True) == 231
    assert parse("1 + (2 * 3) + (4 * (5 + 6))", precedence=True) == 51
    assert parse("2 * 3 + (4 * 5)", precedence=True) == 46
    assert parse("5 + (8 * 3 + 9 + 3 * 4 * 3)", precedence=True) == 1445
    assert parse("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", precedence=True) == 669060
    assert parse("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", precedence=True) == 23340
    print(f"Passed part 2")

if __name__ == "__main__":
    test()