#! /usr/bin/python3
import sys
import operator
from functools import reduce

def parse_input(path):
    lines = open(path).read().strip().split('\n')
    cols = [i for i, c in enumerate(lines[-1]) if c in '+*'] + [max(map(len, lines)) + 1]
    ops = [operator.add if op == '+' else operator.mul for op in lines[-1].split()]
    return [[o] + [l[a: b-1] for l in lines[:-1]] for o, (a, b) in zip(ops, (zip(cols, cols[1:])))]

def solve(problems):
    return sum(reduce(problem[0], map(int, problem[1:])) for problem in problems)

def transpose(problems):
    for problem in problems:
        yield [problem[0]] + [''.join(digits) for digits in zip(*problem[1:])]

def main(input_file):
    problems = parse_input(input_file)
    print("Part 1:", solve(problems))
    print("Part 2:", solve(transpose(problems)))

if __name__ == '__main__':
    main(sys.argv[1])
