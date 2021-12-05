# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/04

class Draws:
    def __init__(self, numbers: list):
        self.draws = numbers[:]
        self.last_idx = -1
        self.draws_left = self.last_idx < len(numbers)

    def draw(self) -> int:
        if not self.draws_left:
            return None
        self.last_idx += 1
        self.draws_left = self.last_idx < len(self.draws)
        return self.draws[self.last_idx]

class Bingo:
    def __init__(self, numbers: list):
        self.field = numbers[:]
        self.drawn = [False] * 25
        self.last_number = None
        self.winner = False

    def draw(self, number: int):
        if number in self.field:
            self.last_number = number
            idx = self.field.index(number)
            self.drawn[idx] = True
            self.check_for_win()

    def check_for_win(self) -> bool:
        for i in range(0, 5):
            if all(self.drawn[i*5 + j] for j in range(5)) or all(self.drawn[j*5 + i] for j in range(5)):
                self.winner = True
                return True
        return False

    def calculate_score(self):
        return sum(self.field[i] for i in range(25) if not self.drawn[i]) * self.last_number

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines = [line for line in f.read().split("\n")]

    draws = Draws([int(x) for x in lines[0].split(",")])

    fields = list()
    cur_nums = list()
    for i in range(2, len(lines), 6):
        for j in range(5):
            cur_nums += [int(x) for x in lines[i + j].lstrip().strip().split()]
        fields.append(Bingo(cur_nums))
        cur_nums.clear()

    return draws, fields

def part1(draws: Draws, fields: list) -> int:
    winner = None
    while draws.draws_left:
        num = draws.draw()
        for f in fields:
            f.draw(num)
            if f.winner and winner is None:
                winner = f

        if winner:
            return winner.calculate_score()
    return -1
            
def part2(draws: Draws, fields: list) -> int:
    while draws.draws_left:
        playing_fields = [field for field in fields if not field.winner]
        if len(playing_fields) == 1:
            break

        num = draws.draw()
        for field in playing_fields:
            field.draw(num)

    last = playing_fields[0]
    while not last.winner:
        last.draw(draws.draw())
    return last.calculate_score()
                
if __name__ == "__main__":
    draws, fields = read_file()
    print(f"Part 1: {part1(draws, fields)}")
    print(f"Part 2: {part2(draws, fields)}")