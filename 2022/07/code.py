# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/7

class Node:
    def __init__(self, name, parent = None, size = None) -> None:
        self.name = name
        self.parent = parent
        if parent:
            parent.children[name] = self
        self.size = size
        self.children = dict()

    def get_size(self) -> int:
        if self.size:
            return self.size
        return sum(self.children[child].get_size() for child in self.children)

def build_dir_tree(terminal_output: list) -> Node:
    root = Node("/")
    cur_dir = root
    for line in terminal_output:
        if line.startswith("$ ls"):
            continue # 'else' will deal with output
        elif line.startswith("$ cd"):
            dir = line[5:]
            match dir:
                case "/":
                    cur_dir = root
                case "..":
                    cur_dir = cur_dir.parent
                case _:
                    cur_dir = cur_dir.children[dir]
        else: # line not starting with "$" => output of ls
            type, name = line.split(" ")
            match type:
                case "dir":
                    new_node = Node(name=name, parent=cur_dir)
                case _:
                    new_node = Node(name=name, parent=cur_dir, size=int(type))
    return root

def read_file(filename: str = "input.txt") -> Node:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return build_dir_tree(lines)

def get_possible_folder_sizes(node: Node, target_size: int, size_up_to: bool, sizes: list) -> None:
    if len(node.children) == 0:
        return
    size = node.get_size()
    if not size_up_to and size >= target_size or size_up_to and size <= target_size:
        sizes.append(size)
    for child in node.children:
        get_possible_folder_sizes(node.children[child], target_size, size_up_to, sizes)

def part1(node: Node) -> int:
    sizes = []
    get_possible_folder_sizes(node, 100000, True, sizes)
    return sum(sizes)

def part2(node: Node) -> int:
    sizes = []
    get_possible_folder_sizes(node, node.get_size() - 40000000, False, sizes)
    return min(sizes)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
