#! /usr/bin/env python3
import sys
import itertools
from functools import reduce

def parse_input(path):
    machines = []
    for line in open(path).read().strip().split('\n'):
        words = line.split()
        target = {i - 1 for i, c in enumerate(words[0]) if c == '#'}
        buttons = [{int(x) for x in word[1:-1].split(',')} for word in words[1:-1]]
        joltage = [int(x) for x in words[-1][1:-1].split(',')]
        machines.append( (target, buttons, joltage) )
    return machines

def part1_solutions(target, buttons):
    if not target:
        yield set()
    for n_presses in range(1, len(buttons) + 1):
        for try_buttons in itertools.combinations(buttons, n_presses):
            if reduce(set.__xor__, try_buttons) == target:
                yield try_buttons

def solve_part1(machine):
    target, buttons, _ = machine
    for try_buttons in part1_solutions(target, buttons):
        return len(try_buttons)

def reach_joltage(joltages, buttons, cache):
    if not any(joltages):
        return 0
    if joltages in cache:
        return cache[joltages]
    parity_target = {ji for ji, j in enumerate(joltages) if j & 1}
    score = None
    for parity_buttons in part1_solutions(parity_target, buttons):
        rem_joltages = list(joltages)
        for pb in parity_buttons:
            for i in pb:
                rem_joltages[i] -= 1
        if any(j < 0 for j in rem_joltages):
            continue
        assert all(j & 1 == 0 for j in rem_joltages)
        rem_score = reach_joltage(tuple(j // 2 for j in rem_joltages), buttons, cache)
        if rem_score is not None:
            this_score = len(parity_buttons) + 2 * rem_score
            if score is None or score > this_score:
                score = this_score
    cache[joltages] = score
    return score

def solve_part2(machine):
    _, buttons, joltages = machine
    return reach_joltage(tuple(joltages), buttons, {})

def main(input_file):
    machines = parse_input(input_file)
    print("Part 1:", sum(map(solve_part1, machines)))
    print("Part 2:", sum(map(solve_part2, machines)))

if __name__ == '__main__':
    main(sys.argv[1])
