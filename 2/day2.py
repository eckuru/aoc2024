#!/usr/bin/env python3

import numpy as np


def part1():
    safecount = 0
    with open("input.txt") as f:
        for line in f.readlines():
            line = np.array(list(map(int, line.replace("\n", "").split(" "))))
            print(line)
            diffs = np.ediff1d(line)
            if all(abs(diffs) <= 3) and all(abs(diffs) >= 1):
                if all(diffs > 0) or all(diffs < 0):
                    safecount += 1
    print(f"Part 1 {safecount}")


if __name__ == "__main__":
    part1()
