# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/21

def read_file(filename: str = "input.txt") -> tuple:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [int(line[28:]) for line in f.read().strip().split("\n")]

def game_deterministic(positions: list) -> tuple:
    pos = positions[:]
    player, rolls, die = 0, 0, 0
    scores = [0, 0]
    while max(scores) < 1000:
        for _ in range(3):
            die = (die + 1) % 100 or 100
            rolls += 1
            pos[player] = (pos[player] + die) % 10 or 10
        scores[player] += pos[player]
        player = (player + 1) % 2
    return rolls, scores

def game_dirac(move_frequency: dict, wins: list, positions: list, 
        scores: list = [0, 0], player: int = 0, win_mult: int = 1) -> None:
    next_player = (player + 1) % 2
    for moves in move_frequency:
        pos, scr = positions[:], scores[:]
        pos[player] = (pos[player] + moves) % 10 or 10
        scr[player] += pos[player]
        next_mult = move_frequency[moves] * win_mult
        if scr[player] < 21:
            game_dirac(move_frequency, wins, pos, scr, next_player, next_mult)
        else:
            wins[player] += next_mult

def part1(start_positions: list) -> int:
    rolls, scores = game_deterministic(start_positions)
    return rolls * min(scores)

def part2(start_positions: list) -> int:
    move_frequency = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    wins = [0, 0]
    game_dirac(move_frequency, wins, start_positions)
    return max(wins)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
    