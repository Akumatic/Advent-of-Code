# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

class Pass:
    def __init__(self, input):
        tmp = dict()
        for data in input:
            d = data.split(":")
            tmp[d[0]] = d[1]
        self.byr = int(tmp["byr"]) if "byr" in tmp else None
        self.iyr = int(tmp["iyr"]) if "iyr" in tmp else None
        self.eyr = int(tmp["eyr"]) if "eyr" in tmp else None
        self.hgt = tmp["hgt"] if "hgt" in tmp else None
        self.hcl = tmp["hcl"] if "hcl" in tmp else None
        self.ecl = tmp["ecl"] if "ecl" in tmp else None
        self.pid = tmp["pid"] if "pid" in tmp else None
        self.cid = tmp["cid"] if "cid" in tmp else None

    def valid_fields(self) -> bool:
        return all((self.byr, self.iyr, self.eyr, \
            self.hgt, self.hcl, self.ecl, self.pid))

    def valid_data(self):
        if not self.valid_fields():
            return False
        return all((
            validate_byr(self.byr),
            validate_iyr(self.iyr),
            validate_eyr(self.eyr),
            validate_hgt(self.hgt),
            validate_hcl(self.hcl),
            validate_ecl(self.ecl),
            validate_pid(self.pid)
        ))

def validate_byr(byr: int) -> bool:
    return 1920 <= byr <= 2002

def validate_iyr(iyr: int) -> bool:
    return 2010 <= iyr <= 2020

def validate_eyr(eyr: int) -> bool:
    return 2020 <= eyr <= 2030

def validate_hgt(hgt: str) -> bool:
    if not(hgt[-2:] in ("cm","in") and hgt[:-2].isnumeric()):
        return False
    i = int(hgt[:-2])
    return 150 <= i <= 193 if hgt[-2:] == "cm" else 59 <= i <= 76

def validate_hcl(hcl: str) -> bool:
    if not(len(hcl) == 7 and hcl[0] == "#"):
        return False
    return all(47 < ord(c) < 58 or 96 < ord(c) < 103 for c in hcl[1:])

def validate_ecl(ecl: str) -> bool:
    return ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def validate_pid(pid: str) -> bool:
    return len(pid) == 9 and pid.isnumeric()