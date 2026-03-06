#! /usr/bin/python3
import sys

def find_accessible(rolls):
    accessible = set()
    n = 0
    for x, y in rolls:
        neighbours = rolls & {(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                              (x - 1, y), (x + 1, y),
                              (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)}
        if len(neighbours) < 4:
            accessible.add((x, y))
    return accessible

def main(input_file):
    rolls = set()
    for y, line in enumerate(open(input_file).read().strip().split('\n')):
        for x, c in enumerate(line):
            if c == '@':
                rolls.add((x, y))
    print("Part 1:", len(find_accessible(rolls)))
    n_rolls = len(rolls)
    while (accessible := find_accessible(rolls)):
        rolls -= accessible
    print("Part 2:", n_rolls - len(rolls))

if __name__ == '__main__':
    main(sys.argv[1])
