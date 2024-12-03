#!/usr/bin/env python3

import re

def mul(x,y):
    return x * y

def part1(regex):
    result = 0
    with open("input.txt") as f:
        for line in f.readlines():
            matches = regex.findall(line)
            for match in matches:
                result += eval(match)
    print(f"Part 1: {result}")

def part2(regex):
    result = 0
    with open("input.txt") as f:
        fullinput = f.read()
        sublines = fullinput.split("do()")
        for subline in sublines:
            partial = subline.split("don't()")[0]
            matches = regex.findall(partial)
            for match in matches:
                result += eval(match)
    print(f"Part 2: {result}")


if __name__ == '__main__':
    regex = re.compile(r"mul\([0-9]+,[0-9]+\)")
    part1(regex)
    part2(regex)
