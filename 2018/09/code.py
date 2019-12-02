""" https://adventofcode.com/2018/day/9 """

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        data = f.read().split(" ")
        return (int(data[0]), int(data[6]))

class Player:
    num = 1
    def __init__(self):
        self.score = 0
        self.number = Player.num
        Player.num += 1

def getMaxScore(players):
    maxScore = 0
    for player in players:
        if player.score > maxScore:
            maxScore = player.score
    return maxScore

def part1(vals):
    players = [Player() for i in range(vals[0])]
    curPlayer = 0
    curMarble = 0
    marbles = [0]

    for i in range(1, vals[1] + 1):
        size = len(marbles)
        if i % 23 != 0:
            idx = (curMarble + 2) % size
            if idx == 0:
                marbles.append(i)
                curMarble = size
            else:
                marbles.insert(idx, i)
                curMarble = idx
        else:
            idx = (curMarble - 7) % size
            temp = marbles.pop(idx)
            players[curPlayer].score += i + temp
            curMarble = idx % (size - 1)

        curPlayer = (curPlayer + 1) % vals[0]

    return getMaxScore(players)

def part2(vals): # optimized part 1 because that took too long
    from collections import deque

    players = [Player() for i in range(vals[0])]
    curPlayer = 0
    marbles = deque([0])

    for i in range(1, vals[1] + 1):
        if i % 23 == 0:
            marbles.rotate(7)
            players[curPlayer].score += i + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(i)

        curPlayer = (curPlayer + 1) % vals[0]

    return getMaxScore(players)

def testPart1():
    examples = [
        (9, 23, 32), (10, 1618, 8317),
        (13, 7999, 146373), (17, 1104, 2764),
        (21, 6111, 54718), (30, 5807, 37305)
    ]
    for e in examples:
        r = part1(e[:2])
        print(f"{e[0]} Players, {e[1]} Marbles, Goal: {e[2]}," \
            f"Result: {r}, Correct: {e[2] == r}")

if __name__ == "__main__":
    #testPart1()
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2((vals[0], vals[1]*100))}")