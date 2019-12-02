""" https://adventofcode.com/2018/day/4 """

def readFile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        l = [line[:-1] for line in f.readlines()]
    l.sort()
    return l

class Guard:
    def __init__(self, id):
        self.id = int(id)
        self.idStr = id
        self.timeAsleep = 0
        self.minutes = [0 for min in range(60)]

    def sleep(self, start, end):
        self.timeAsleep += (end - start)
        for i in range(start, end):
            self.minutes[i] += 1

def evaluateLines(vals : list):
    curID = -1
    start = -1
    guards = {}
    for val in vals:
        timestamp = val[1:17]
        event = val[19:]

        if "#" in event:
            curID = event.split()[1][1:]
            if curID not in guards:
                guards[curID] = Guard(curID)
        elif event == "falls asleep":
            start = int(timestamp[14:16])
        else: # event == "wakes up"
            end = int(timestamp[14:16])
            guards[curID].sleep(start, end)

    return guards

def part1(guards : dict):
    maxID = ""
    maxSleep = 0
    for guard in guards:
        if guards[guard].timeAsleep > maxSleep:
            maxSleep = guards[guard].timeAsleep
            maxID = guard

    guard = guards[maxID]
    return guard.id * guard.minutes.index(max(guard.minutes))

def part2(guards : dict):
    maxID = ""
    maxAmount = 0
    for guard in guards:
        cur = max(guards[guard].minutes)
        if cur > maxAmount:
            maxAmount = cur
            maxID = guard
    
    guard = guards[maxID]
    return guard.id * guard.minutes.index(max(guard.minutes))

if __name__ == "__main__":
    vals = readFile()
    guards = evaluateLines(vals)
    print(f"Part 1: {part1(guards)}")
    print(f"Part 2: {part2(guards)}")