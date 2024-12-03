#!/usr/bin/env python3

import numpy as np


def issafe(line):
    diffs = np.ediff1d(line)
    n_mon_inc = sum(diffs > 0)
    n_mon_dec = sum(diffs < 0)
    n_right_diff_range = sum((abs(diffs) <= 3) & (abs(diffs) >= 1))
    if n_right_diff_range == len(diffs) and (n_mon_dec == 0 or n_mon_inc == 0):
        return True


def day2():
    safecount = 0
    almostsafecount = 0
    with open("input.txt") as f:
        for line in f.readlines():
            line = np.array(list(map(int, line.replace("\n", "").split(" "))))
            if issafe(line):
                safecount += 1
            else:
                for i in range(0, len(line)):
                    newline = np.hstack([line[:i], line[i+1:]])
                    print(newline)
                    if issafe(newline):
                        print("almost safe")
                        almostsafecount += 1
                        break

    print(f"Part 1 {safecount}")
    print(f"Part 2 {safecount + almostsafecount}")


if __name__ == "__main__":
    day2()
