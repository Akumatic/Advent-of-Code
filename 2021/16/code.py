# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/16

def read_file(filename: str = "input.txt") -> str:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return f.read().strip()

def hex2bin(hex_str: str) -> str:
    return "".join(bin(int(h, 16))[2:].zfill(4) for h in hex_str)

def decode_packet(packet: str) -> tuple:
    # packet header
    version = int(packet[:3], 2)
    type_id = int(packet[3: 6], 2)
    size = 6
    payload = list()

    if type_id == 4: # literal value
        for i in range(6, len(packet), 5):
            payload.append(packet[i+1: i+5])
            size += 5
            if packet[i] == "0":
                break
        payload = int("".join(payload), 2)

    else: # operator
        size += 1
        if packet[6] == "0": # length in bits of the subpacket
            sub_size = int(packet[7: 22], 2)
            size += 15 + sub_size
            data = packet[22:]
            i = 0
            while i < sub_size:
                decoded_sub = decode_packet(data[i:])
                payload.append(decoded_sub)
                i += decoded_sub[2]
        else: # packet[6] == 1, number of sub-packets
            sub_amount = int(packet[7: 18], 2)
            size += 11
            data = packet[size:]
            for i in range(sub_amount):
                decoded_sub = decode_packet(data)
                payload.append(decoded_sub)
                size += decoded_sub[2]
                data = packet[size:]
    
    return version, type_id, size, payload
        
def sum_versions(payload: tuple) -> int:
    if payload[1] == 4:
        return payload[0]
    return payload[0] + sum(sum_versions(sub) for sub in payload[3])

def payload_value(payload: tuple) -> int:
    # literal values
    if payload[1] == 4:
        return payload[3]

    values = [payload_value(sub) for sub in payload[3]]

    if payload[1] == 0: # sum
        return sum(values)
    elif payload[1] == 1: # product
        prod = 1
        for value in values:
            prod *= value
        return prod
    elif payload[1] == 2: # minimum
        return min(values)
    elif payload[1] == 3: # maximum
        return max(values) 
    elif payload[1] == 5: # greater than
        return 1 if values[0] > values[1] else 0
    elif payload[1] == 6: # less than
        return 1 if values[0] < values[1] else 0
    else: # payload[1] == 7, equal to
        return 1 if values[0] == values[1] else 0

def part1(hex_value: str) -> int:
    data = decode_packet(hex2bin(hex_value))
    return sum_versions(data)

def part2(hex_value: str) -> int:
    data = decode_packet(hex2bin(hex_value))
    return payload_value(data)
        
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
