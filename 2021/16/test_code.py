# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2, read_file, hex2bin, decode_packet

def test():
    assert decode_packet(hex2bin("D2FE28")) == (6, 4, 21, 2021)
    assert decode_packet(hex2bin("38006F45291200")) == (1, 6, 49, [(6, 4, 11, 10), (2, 4, 16, 20)])
    assert decode_packet(hex2bin("EE00D40C823060")) == (7, 3, 51, [(2, 4, 11, 1), (4, 4, 11, 2), (1, 4, 11, 3)])
    print("Passed decoding tests")
    assert part1("8A004A801A8002F478") == 16
    assert part1("620080001611562C8802118E34") == 12
    assert part1("C0015000016115A2E0802F182340") == 23
    assert part1("A0016C880162017C3686B18A3D4780") == 31
    print("Passed Part 1")
    assert part2("C200B40A82") == 3
    assert part2("04005AC33890") == 54
    assert part2("880086C3E88112") == 7
    assert part2("CE00C43D881120") == 9
    assert part2("D8005AC2A8F0") == 1
    assert part2("F600BC2D8F") == 0
    assert part2("9C005AC2F8F0") == 0
    assert part2("9C0141080250320F1802104A08") == 1
    print("Passed Part 2")

if __name__ == "__main__":
    test()
