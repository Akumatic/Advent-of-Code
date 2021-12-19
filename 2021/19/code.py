# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/19

class Scanner:
    def __init__(self, id: int) -> "Scanner":
        self.id = id
        self.x, self.y, self.z, self.orientation = None, None, None, None
        self._beacons = 0
        self.transformations = {x:list() for x in range(24)}
        self.distances = {x:dict() for x in range(24)}
        self.positions = None

    def get_position(self) -> tuple:
        return (self.x, self.y, self.z)
    
    def add_beacon(self, beacon: list) -> None:
        self._beacons += 1
        # beacons and their transformations
        for i in range(24):
            self.transformations[i].append(self._transform(beacon, i))
        # distances between different beacons for each orientation
        for t in range(24):
            self.distances[t] = list()
            for i in range(self._beacons):
                for j in range(i, self._beacons):
                    if i == j:
                        continue
                    a = self.transformations[t][i]
                    b = self.transformations[t][j]
                    dist =  (b[0] - a[0], b[1] - a[1], b[2] - a[2])
                    self.distances[t].append(dist)

    def set_position_and_orientation(self, pos: tuple, orientation: int) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.orientation = orientation
        self.positions = [[self.x + beacon[0], self.y + beacon[1], self.z + beacon[2]] 
            for beacon in self.transformations[orientation]]
        self.distances = self.distances[orientation]

    def _transform(self, beacon: list, t: int) -> list:
        x, y, z = beacon[0], beacon[1], beacon[2]
        if t == 0: return [x, y, z]
        elif t == 1: return [x, -y, -z]
        elif t == 2: return [x, z, -y]
        elif t == 3: return [x, -z, y]
        elif t == 4: return [y, x, -z]
        elif t == 5: return [y, -x, z]
        elif t == 6: return [y, z, x]
        elif t == 7: return [y, -z, -x]
        elif t == 8: return [z, x, y]
        elif t == 9: return [z, -x, -y]
        elif t == 10: return [z, y, -x]
        elif t == 11: return [z, -y, x]
        elif t == 12: return [-x, y, -z]
        elif t == 13: return [-x, -y, z]
        elif t == 14: return [-x, z, y]
        elif t == 15: return [-x, -z, -y]
        elif t == 16: return [-y, x, z]
        elif t == 17: return [-y, -x, -z]
        elif t == 18: return [-y, z, -x]
        elif t == 19: return [-y, -z, x]
        elif t == 20: return [-z, x, -y]
        elif t == 21: return [-z, -x, y]
        elif t == 22: return [-z, y, x]
        else: return [-z, -y, -x] # t == 23

def shared_points(scn_a: Scanner, scn_b: Scanner) -> tuple:
    result, orientation = 0, 0
    for t in range(24): # transformations
        tmp = [distance for distance in scn_a.distances[t] if distance in scn_b.distances]
        if len(tmp) > result:
            result = len(tmp)
            orientation = t
    return result, orientation

def get_points_to_distance(scanner: Scanner, distance: list, orientation: int) -> list:
    result = list()
    for i in range(scanner._beacons):
        for j in range(scanner._beacons):
            if i == j:
                continue
            a, b = scanner.transformations[orientation][i], scanner.transformations[orientation][j]
            dist = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
            if dist == distance:
                result.append([a, b])
    return result

def calculate_position_orientation(scn_a: Scanner, scn_b: Scanner, orientation: int) -> tuple:
    mapping = {dist: get_points_to_distance(scn_a, dist, orientation) 
        for dist in scn_a.distances[orientation] if dist in scn_b.distances}
    a, b = None, None
    for key in mapping:
        if len(mapping[key]) > 1:
            continue
        tmp = get_points_to_distance(scn_b, key, scn_b.orientation)
        if len(tmp) > 1:
            continue
        a, b = mapping[key][0][0], tmp[0][0]
        return [scn_b.x + b[0] - a[0], scn_b.y + b[1] - a[1], scn_b.z + b[2] - a[2]], orientation

def find_scanner_positions(scanners: list, shared_beacons: int = 12) -> None:
    done = [s for s in scanners if s.get_position() != (None, None, None)]
    queue = [s for s in scanners if s not in done]
    while queue:
        a = queue.pop(0)
        add = True
        for b in done:
            shared = shared_points(a, b)
            if shared[0] < shared_beacons:
                continue
            add = False
            a.set_position_and_orientation(*calculate_position_orientation(a, b, shared[1]))
            done.append(a)
            break

        if add: 
            queue.append(a)

def manhattan_distance(a: tuple, b: tuple) -> int:
    return sum(abs(b[i] - a[i]) for i in range(3))

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines= [line for line in f.read().strip().split("\n")]
    scanners = list()
    cur = None
    for line in lines:
        if line.startswith("--- scanner"):
            scanners.append(Scanner(int(line.split(" ")[2])))
        elif line == "":
            continue
        else:
            tmp = [int(x) for x in line.split(",")]
            scanners[-1].add_beacon(tmp)
    scanners[0].set_position_and_orientation((0, 0, 0), 0)
    return scanners

def part1(scanners: list) -> int:
    unique_positions = list()
    find_scanner_positions(scanners)
    for scanner in scanners:
        for pos in scanner.positions:
            if pos not in unique_positions:
                unique_positions.append(pos)
    return len(unique_positions)

def part2(scanners: list) -> int:
    max_dist = 0
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            if i == j:
                continue
            dist = manhattan_distance(scanners[i].get_position(), scanners[j].get_position())
            if max_dist < dist:
                max_dist = dist
    return max_dist
        
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
    