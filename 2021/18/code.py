# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/18

import math

class Node:
    def __init__(self, left: "Node" = None, right: "Node" = None,
            value: int = None, parent: "Node" = None, depth: int = 1):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent
        self.depth = depth

    def __str__(self) -> str:
        return str(self.value) if self.value is not None else f"[{self.left},{self.right}]"

    def explode(self) -> bool:
        if self.depth < 5:
            tmp = False
            if self.left.value is None:
                tmp = self.left.explode()
                if tmp:
                    return True
            if self.right.value is None:
                tmp = self.right.explode()
            return tmp

        elif self.depth == 5:
            assert self.left.value is not None and self.right.value is not None
            left = self._find_next_node_with_value(left = True)
            right = self._find_next_node_with_value(left = False)
            if left:
                left.value += self.left.value
            if right:
                right.value += self.right.value
            self.left, self.right, self.value = None, None, 0
            return True

    def split(self) -> bool:
        if self.value is None:        
            tmp = False
            tmp = self.left.split()
            if tmp:
                return True
            tmp = self.right.split()
            return tmp
        
        if self.value < 10:
            return False

        val = self.value / 2
        self.value = None
        self.left = Node(value=math.floor(val), parent=self, depth=self.depth + 1)
        self.right = Node(value=math.ceil(val), parent=self, depth=self.depth + 1)
        return True

    def set_parent(self, parent: "Node") -> None:
        self.parent = parent
        self.depth = parent.depth + 1
        if self.value is None:
            self.left.set_parent(self)
            self.right.set_parent(self)

    def _find_next_node_with_value(self, left: bool) -> "Node":
        no_parent = True
        node = self
        while node.parent is not None:
            if left and node.parent.right == node or not left and node.parent.left == node:
                node = node.parent.left if left else node.parent.right
                no_parent = False
                break
            else:
                node = node.parent

        if no_parent:
            return None
        else:
            while left and node.right is not None or not left and node.left is not None:
                node = node.right if left else node.left
            return node

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [eval(line) for line in f.read().strip().split("\n")]

def parse_node(node: list, depth: int = 1) -> Node:
    a = Node(value=node[0], depth=depth) if isinstance(node[0], int) else parse_node(node[0], depth = depth + 1)
    b = Node(value=node[1], depth=depth) if isinstance(node[1], int) else parse_node(node[1], depth = depth + 1)
    node = Node(left=a, right=b, depth=depth)
    a.set_parent(node)
    b.set_parent(node)
    return node

def reduce(node: Node) -> None:
    repeat = True
    while repeat:
        repeat = False
        explosion_result = node.explode()
        if explosion_result:
            repeat = True
            continue
        repeat = node.split()

def add(a: Node, b: Node) -> Node:
    node = Node(left=a, right=b)
    a.set_parent(node)
    b.set_parent(node)
    reduce(node)
    return node

def sum_nodes(nodes: list) -> list:
    node = parse_node(nodes[0])
    for i in range(1, len(nodes)):
        node = add(node, parse_node(nodes[i]))
    return node

def get_magnitude(node: Node) -> int:
    if node.value is not None:
        return node.value
    return 3 * get_magnitude(node.left) + 2 * get_magnitude(node.right)

def part1(vals: list) -> int:
    tree = sum_nodes(vals)
    return get_magnitude(tree)

def part2(vals: list) -> int:
    max_mag = 0
    nodes = [parse_node(node) for node in vals]
    for i in range(len(vals)):
        for j in range(len(vals)):
            if i == j:
                continue
            a, b = parse_node(vals[i]), parse_node(vals[j])
            c, d = parse_node(vals[i]), parse_node(vals[j])
            max_mag = max(max_mag, get_magnitude(add(a, b)), get_magnitude(add(c, d)))
    return max_mag
        
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
