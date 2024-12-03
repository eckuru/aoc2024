#!/usr/bin/env python3

import re

def mul(x,y):
    return x * y

def part1():
    regex = re.compile(r"mul\([0-9]+,[0-9]+\)")
    result = 0
    with open("input.txt") as f:
        for line in f.readlines():
            matches = regex.findall(line)
            for match in matches:
                print(match)
                print(eval(match))
                result += eval(match)
    print(f"Part 1: {result}")


if __name__ == '__main__':
    part1()
