#!/usr/bin/env python3

import numpy as np


def parseinput():
    n = len(open("input.txt").readlines())
    with open("input.txt", "r") as f:
        inputmat = np.zeros((n, 2), int)
        for i, line in enumerate(f.readlines()):
            data = line.replace("\n", "").split("   ")
            inputmat[i, :] = data[0], data[-1]
    return inputmat


def part1():
    inputmat = parseinput()
    inputmat.sort(0)
    totaldist = np.sum(abs(inputmat[:, 0] - inputmat[:, 1]))
    print(f"Part 1: {totaldist}")


def part2():
    inputmat = parseinput()
    similarity = [
        i * sum(inputmat[:, 1] == i)
        for i in inputmat[:, 0]
        if i in inputmat[:, 1]
    ]
    print(f"Part 2: {sum(similarity)}")


if __name__ == "__main__":
    part1()
    part2()
