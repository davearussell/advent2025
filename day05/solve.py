#! /usr/bin/python3
import sys

def merge_ranges(ranges):
    ranges.sort()
    new_ranges = []
    last_lo = last_hi = ranges[0][0] - 2
    for lo, hi in ranges:
        if lo <= last_hi + 1:
            if hi > last_hi:
                last_hi = hi
                new_ranges[-1] = (last_lo, last_hi)
        else:
            last_lo, last_hi = lo, hi
            new_ranges.append((lo, hi))
    return new_ranges

def parse_input(path):
    fresh = []
    ingredients = []
    for word in open(path).read().split():
        if '-' in word:
            a, b = map(int, word.split('-'))
            fresh.append((a, b))
        else:
            ingredients.append(int(word))
    return merge_ranges(fresh), ingredients

def is_fresh(ingredient, ranges):
    for lo, hi in ranges:
        if lo <= ingredient <= hi:
            return True
    return False

def main(input_file):
    fresh, ingredients = parse_input(input_file)
    print("Part 1:", sum(is_fresh(ingredient, fresh) for ingredient in ingredients))
    print("Part 2:", sum(hi - lo + 1 for lo, hi in fresh))

if __name__ == '__main__':
    main(sys.argv[1])
