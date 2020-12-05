#!/usr/bin/env python3

import sys
import re

FIELD_RE = r'([a-z]+):(\#?\w+)'
eyeColors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def validate(dir):
    count = 0
    for entry in dir:
        if len(entry.keys()) == 7 and 'cid' not in entry:
            if validateXtra(entry):
                count += 1
        elif len(entry.keys()) == 8:
            if validateXtra(entry):
                count += 1

    return count

def validateXtra(entry):
    if 1920 > int(entry["byr"]) or int(entry["byr"]) > 2002:
        return False
    if 2010 > int(entry["iyr"]) or int(entry["iyr"]) > 2020:
        return False
    if 2020 > int(entry["eyr"]) or int(entry["eyr"]) > 2030:
        return False
    if not re.match(r"[0-9]+(cm|in)", entry["hgt"]):
        return False
    elif(entry["hgt"][-2:] == "cm"):
        if(int(entry["hgt"][0:-2]) < 150 or int(entry["hgt"][0:-2]) > 193):
            return False
    else:
        if(int(entry["hgt"][0:-2]) < 59 or int(entry["hgt"][0:-2]) > 76):
            return False
    if not re.match(r"#[0-9a-f]{6}", entry["hcl"]):
        return False
    if entry["ecl"] not in eyeColors:
        return False
    if len(entry["pid"]) != 9 or not entry["pid"].isdigit():
        return False
    return True

def main():
    dir = []
    pp = {}

    for i in sys.stdin:
        if i == "\n":
            dir.append(pp)
            pp = {}

        for j in i.split():
            field, value = re.findall(FIELD_RE, j)[0]
            pp[field] = value

    # for last input
    dir.append(pp)
    print(validate(dir))

if __name__ == '__main__':
    main()
