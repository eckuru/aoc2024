#!/usr/bin/env python3
import numpy as np

def parse_input():
    with open("input.txt") as f:
        rulesstr, updatestr = open("input.txt").read().split('\n\n')
    rules = [list(map(int, rulestr.split('|'))) for rulestr in rulesstr.split('\n')]
    updates = [list(map(int, i.split(','))) for i in updatestr.split('\n')[:-1]]
    return rules, updates


class MyNumber():
    def __init__(self, n):
        self.n = n

    def __lt__(self, other):
        gt = [other.n, self.n] in rules
        return not gt

    def __eq__(self, other):
        return self.n == other.n


def day5(updates):
    part1 = 0
    part2 = 0
    for update in updates:
        numbers = [MyNumber(i) for i in update]
        sortednumbers = sorted(numbers)
        middle = int((len(numbers) - 1)/2)
        if sortednumbers == numbers:
            part1 += numbers[middle].n
        else:
            part2 += sortednumbers[middle].n
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    rules, updates = parse_input()
    day5(updates)
