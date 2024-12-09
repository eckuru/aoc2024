#!/usr/bin/env python3
#
import numpy as np
from copy import copy


def parseinput():
    inputlist = []
    with open("input.txt") as f:
        for line in f.readlines():
            inputlist.append(list(line.replace('\n', '')))
    inputmat = np.array(inputlist)
    startloc = np.where(inputmat == '^')
    inputmat[startloc] = '.'
    return inputmat, startloc

def propagate(mat, x, y, direction):
    inputmat = copy(mat)
    visited_corners = []
    looped = False
    left = False
    while not looped and not left:
        if (x, y, direction) in visited_corners:
            looped = True
            break
        else:
            visited_corners.append((x, y, direction))
        if direction == 'up':
            try:
                obstacle = np.where(inputmat[:x, y] == '#')[0][-1]
            except IndexError:
                left = True
                break
            inputmat[obstacle+1:x+1, y] = 'X'
            x = obstacle + 1
            direction = 'right'
        elif direction == 'right':
            try:
                obstacle = np.where(inputmat[x, y+1:] == '#')[0][0]
            except IndexError:
                left = True
                break
            inputmat[x, y+1:y+obstacle+1] = 'X'
            y += obstacle
            direction = 'down'
        elif direction == 'down':
            try:
                obstacle = np.where(inputmat[x+1:, y] == '#')[0][0]
            except IndexError:
                left = True
                break
            inputmat[x+1:x+obstacle+1, y] = 'X'
            x += obstacle
            direction = 'left'
        elif direction == 'left':
            try:
                obstacle = np.where(inputmat[x, :y] == '#')[0][-1]
            except IndexError:
                left = True
                break
            inputmat[x, obstacle+1:y+1] = 'X'
            y = obstacle + 1
            direction = 'up'
    if left:
        if direction == 'up':
            inputmat[:x+1, y] =  'X'
        elif direction == 'right':
            inputmat[x, y:] =  'X'
        elif direction == 'down':
            inputmat[x:, y] =  'X'
        elif direction == 'left':
            inputmat[x, :y+1] =  'X'
    return inputmat, looped

def part1(inputmat, x, y):
    direction = 'up'
    res, _ = propagate(inputmat, x, y, direction)
    visited = np.where(res == 'X')
    print(f"Part 1: {len(visited[0])}")
    return visited

def part2(inputmat, candidates, x, y):
    newobstacles = 0
    obstlist = []
    errslist = []
    for i, j in zip(*candidates):
        if (i, j) == (x, y):
            continue
        mati = copy(inputmat)
        mati[i, j] = '#'
        res, loop = propagate(mati, x, y, 'up')
        if loop:
            obstlist.append((i,j))
            newobstacles += 1
    print(f"Part 2: {newobstacles}")


if __name__ == '__main__':
    inputmat, startloc = parseinput()
    x, y = startloc[0][0], startloc[1][0]
    visited = part1(inputmat, x, y)
    part2(inputmat, visited, x, y)
