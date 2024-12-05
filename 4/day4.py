#!/usr/bin/env python3
import numpy as np
import re

def parse_input():
    n = len(open("input.txt", "r").readlines())
    m = len(open("input.txt", "r").readlines()[0].replace("\n", ""))
    inputmat = np.zeros((n, m), str)
    with open("input.txt") as f:
        for i, line in enumerate(f.readlines()):
            inputmat[i, :] = list(line.replace('\n', ''))
    return inputmat


def reshape_ids(idxlist):
    #This probably exists in numpy...
    return [(i,j) for i, j in zip(idxlist[0], idxlist[1])]


def part1(xids, mids, aids, sids):
    count = 0
    for i, j in xids:
        if (i, j+1) in mids and (i, j+2) in aids and (i, j+3) in sids:
            count += 1
        if (i, j-1) in mids and (i, j-2) in aids and (i, j-3) in sids:
            count += 1
        if (i+1, j) in mids and (i+2, j) in aids and (i+3, j) in sids:
            count += 1
        if (i-1, j) in mids and (i-2, j) in aids and (i-3, j) in sids:
            count += 1
        if (i+1, j+1) in mids and (i+2, j+2) in aids and (i+3, j+3) in sids:
            count += 1
        if (i-1, j-1) in mids and (i-2, j-2) in aids and (i-3, j-3) in sids:
            count += 1
        if (i+1, j-1) in mids and (i+2, j-2) in aids and (i+3, j-3) in sids:
            count += 1
        if (i-1, j+1) in mids and (i-2, j+2) in aids and (i-3, j+3) in sids:
            count += 1
    print(count)


def part2(mids, aids, sids):
    count = 0
    for i, j in aids:
        if ((i+1, j+1) in mids and (i-1, j-1) in sids) or ((i+1, j+1) in sids and (i-1, j-1) in mids):
            if ((i-1, j+1) in mids and (i+1, j-1) in sids) or ((i-1, j+1) in sids and (i+1, j-1) in mids):
                count += 1
    print(count)


if __name__ == "__main__":
    inputmat = parse_input()
    xidxlist = np.where(inputmat == "X")
    midxlist = np.where(inputmat == "M")
    aidxlist = np.where(inputmat == "A")
    sidxlist = np.where(inputmat == "S")

    xids = reshape_ids(xidxlist)
    mids = reshape_ids(midxlist)
    aids = reshape_ids(aidxlist)
    sids = reshape_ids(sidxlist)
    part1(xids, mids, aids, sids)
    part2(mids, aids, sids)
