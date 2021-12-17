# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/17

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines = [s[2:].split("..") for s in f.read().strip().replace("target area: ", "").split(", ")]
    return [(int(lines[0][0]), int(lines[0][1])), (int(lines[1][0]), int(lines[1][1]))]

def fire_probe(vel_x, vel_y, goal_x, goal_y) -> tuple:
    vx, vy = vel_x, vel_y
    x, y = 0, 0
    max_y = 0
    while x + vx < goal_x.stop:
        x += vx
        y += vy
        max_y = max(y, max_y)
        vx += 0 if vx == 0 else -1 if vx > 0 else 1
        vy -= 1
        if vx == 0 and (x < goal_x.start or y < goal_y.start):
            break
        if x in goal_x and y in goal_y:
            return vel_x, vel_y, max_y
    return vel_x, vel_y, None

def brute_force(vals: list):
    r_x = range(vals[0][0], vals[0][1] + 1)
    r_y = range(vals[1][0], vals[1][1] + 1)
    tmp = [fire_probe(x, y, r_x, r_y) for x in range(vals[0][1] + 1) for y in range(-100, 100)]
    return [velocity for velocity in tmp if velocity[2] is not None]

def part1(velocities: list) -> int:
    return max(velocities, key=lambda x: x[2])[2]

def part2(velocities: list) -> int:
    return len(velocities)
        
if __name__ == "__main__":
    vals = read_file()
    vals = brute_force(vals)
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
