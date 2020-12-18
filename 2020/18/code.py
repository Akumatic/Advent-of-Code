# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
# https://adventofcode.com/2020/day/18

def read_file() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def evaluate(values: list, operators: list, precedence: bool) -> int:
    if not precedence: # "+" and "*" have same precedence levels
        result = int(values[0])
        for i in range(len(operators)):
            if operators[i] == "+":
                result += int(values[i+1])
            else: # operators[i] == "*"
                result *= int(values[i+1])

    else: # "+" and "*" have different precedence levels; "+" evaluated before "*"
        while True:
            try:
                idx = operators.index("+")
                values = values[:idx] + [values[idx] + values[idx+1]] + values[idx+2:]
                operators = operators[:idx] + operators[idx+1:]
            except ValueError:
                break

        result = 1
        for factor in values:
            result *= factor

    return result

def parse(expression: str, precedence: bool = False) -> int:
    expression = expression.replace(" ", "")
    values = list()
    operators = list()
    i = 0
    while i < len(expression):
        if expression[i] == "+":
            operators.append("+")
            i += 1
        elif expression[i] == "*":
            operators.append("*")
            i += 1
        elif expression[i] == "(":
            # find correct closing bracket
            layer = 1
            j = i + 1
            while j < len(expression):
                if expression[j] == "(":
                    layer += 1
                elif expression[j] == ")":
                    if layer == 1:
                        break
                    layer -= 1
                j += 1
            # evaluate expression between brackets
            values.append(parse(expression[i+1:j], precedence))
            i += j - i + 1
        else: # numbers
            j = i
            value =  0
            while j < len(expression) and expression[j].isnumeric():
                value = value * 10 + int(expression[j])
                j += 1
            values.append(value)
            i += j - i
    
    return evaluate(values, operators, precedence)

def part1(input: list) -> int:
    return sum([parse(line) for line in input])

def part2(input: list) -> int:
    return sum([parse(line, precedence=True) for line in input])

if __name__ == "__main__":
    input = read_file()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")