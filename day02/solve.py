#! /usr/bin/python3
import sys

def is_invalid(n):
    s = str(n)
    lhs = s[:len(s) // 2]
    return s == lhs + lhs

def is_invalid2(n):
    s = str(n)
    l = len(s)
    for i in range(1, l // 2 + 1):
        if s == (s[:i] * (l // i)):
            return True
    return False

def main(input_file):
    ranges = [[int(x) for x in r.split('-')] for r in open(input_file).read().split(',')]
    print("Part 1:", sum(v for lo, hi in ranges for v in range(lo, hi + 1) if is_invalid(v)))
    print("Part 2:", sum(v for lo, hi in ranges for v in range(lo, hi + 1) if is_invalid2(v)))

if __name__ == '__main__':
    main(sys.argv[1])
