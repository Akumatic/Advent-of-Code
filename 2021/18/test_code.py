# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import *

def test_explode(a, b):
    tmp = parse_node(a)
    tmp.explode()
    return str(tmp) == str(parse_node(b))

def test():
    vals = read_file("test_input_2.txt")
    assert str(parse_node([1,2])) == "[1,2]"
    assert str(add(parse_node([1,2]), parse_node([[3,4],5]))) == "[[1,2],[[3,4],5]]"
    assert test_explode([[[[[9,8],1],2],3],4], [[[[0,9],2],3],4])
    assert test_explode([7,[6,[5,[4,[3,2]]]]], [7,[6,[5,[7,0]]]])
    assert test_explode([[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3])
    assert test_explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
    assert test_explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[7,0]]]])
    print("Passed explosion test")
    assert str(add(parse_node([[[[4,3],4],4],[7,[[8,4],9]]]), parse_node([1,1]))) == str(parse_node([[[[0,7],4],[[7,8],[6,0]]],[8,1]]))
    print("Passed reduction test")
    assert str(sum_nodes([[1,1], [2,2], [3,3], [4,4]])) == "[[[[1,1],[2,2]],[3,3]],[4,4]]"
    assert str(sum_nodes([[1,1], [2,2], [3,3], [4,4], [5,5]])) == "[[[[3,0],[5,3]],[4,4]],[5,5]]"
    assert str(sum_nodes([[1,1], [2,2], [3,3], [4,4], [5,5], [6,6]])) == "[[[[5,0],[7,4]],[5,5]],[6,6]]"
    assert str(sum_nodes(read_file("test_input_1.txt"))) == "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
    assert str(sum_nodes(vals)) == "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"
    print("Passed summing nodes test")
    assert get_magnitude(parse_node([[1,2],[[3,4],5]])) == 143.
    assert get_magnitude(parse_node([[[[0,7],4],[[7,8],[6,0]]],[8,1]])) == 1384.
    assert get_magnitude(parse_node([[[[1,1],[2,2]],[3,3]],[4,4]])) == 445.
    assert get_magnitude(parse_node([[[[3,0],[5,3]],[4,4]],[5,5]])) == 791.
    assert get_magnitude(parse_node([[[[5,0],[7,4]],[5,5]],[6,6]])) == 1137.
    assert get_magnitude(parse_node([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])) == 3488.
    assert part1(vals) == 4140
    print("Passed magnitude test")
    assert part2(vals) == 3993
    print("Passed Part 2")

if __name__ == "__main__":
    test()
