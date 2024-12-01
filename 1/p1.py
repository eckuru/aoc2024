#!/usr/bin/env python3

import numpy as np


def part1():
    n = len(open("input.txt").readlines())
    with open("input.txt", "r") as f:
        inputmat = np.zeros((n, 2), int)
        for i, line in enumerate(f.readlines()):
            data = line.replace("\n", "").split("   ")
            inputmat[i, :] = data[0], data[-1]
    inputmat.sort(0)
    totaldist = np.sum(abs(inputmat[:, 0] - inputmat[:, 1]))
    print(f"Part 1: {totaldist}")


if __name__ == "__main__":
    part1()
