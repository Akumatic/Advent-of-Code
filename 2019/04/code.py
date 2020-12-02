# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic
#
# https://adventofcode.com/2019/day/4

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(vals) for vals in f.readline().split("-")]

def getNumbers(min: int, max: int) -> set:
    result = set()
    for i in range(min, max+1):
        nums = [i // 100000, (i // 10000) % 10, (i // 1000) % 10, 
            (i // 100) % 10, (i // 10) % 10, i % 10]
        if isNotDecreasing(nums) and hasDoubleAdjacentValue(nums):
            result.add(i)
    return result

def isNotDecreasing(nums: list) -> bool:
    for x in range(1, 6):
        if nums[x] < nums[x - 1]: 
            return False
    return True

def hasDoubleAdjacentValue(nums: list) -> bool:
    for x in range(1, 5):
        if nums[x] == nums[x - 1] or nums[x] == nums[x + 1]:
            return True
    return False

def isNotPartOfBiggerGroup(nums: list) -> bool:
    for x in range(1, 6):
        if nums[x] == nums[x - 1] and nums.count(nums[x]) == 2:
            return True
    return False

def part1(vals : list) -> int:
    return len(getNumbers(vals[0], vals[1]))

def part2(vals : list) -> int:
    result = set()
    numbers = getNumbers(vals[0], vals[1] + 1)
    for i in numbers:
        nums = [i // 100000, (i // 10000) % 10, (i // 1000) % 10, 
            (i // 100) % 10, (i // 10) % 10, i % 10]
        if isNotPartOfBiggerGroup(nums):
            result.add(i)
    return len(result)

def test():
    assert(isNotDecreasing([1, 1, 1, 1, 1, 1]) == True)
    assert(isNotDecreasing([2, 2, 3, 4, 5, 0]) == False)
    assert(isNotDecreasing([1, 2, 3, 7, 8, 9]) == True)
    assert(hasDoubleAdjacentValue([1, 1, 1, 1, 1, 1]) == True)
    assert(hasDoubleAdjacentValue([2, 2, 3, 4, 5, 0]) == True)
    assert(hasDoubleAdjacentValue([1, 2, 3, 7, 8, 9]) == False)
    assert(isNotPartOfBiggerGroup([1,1,2,2,3,3]) == True)
    assert(isNotPartOfBiggerGroup([1,2,3,4,4,4]) == False)
    assert(isNotPartOfBiggerGroup([1,1,1,1,2,2]) == True)

if __name__ == "__main__":
    test()
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")