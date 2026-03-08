#! /usr/bin/python3
import sys

def parse_input(path):
    start_x = None
    splitters = []
    for y, row in enumerate(open(path).read().strip().split('\n')):
        splitters.append(set())
        for x, c in enumerate(row):
            if c == 'S':
                start_x = x
            elif c == '^':
                splitters[-1].add(x)
    return start_x, [row for row in splitters if row]

def count_splits(start_x, splitters):
    beams = {start_x}
    n_splits = 0
    for row in splitters:
        hits = beams & row
        misses = beams - row
        beams = misses | {x + i for x in hits for i in [-1, 1]}
        n_splits += len(hits)
    return n_splits

def count_timelines(start_x, splitters):
    beams = {start_x: 1}
    for row in splitters:
        new_beams = {}
        for beam, n in beams.items():
            if beam in row:
                new_beams[beam - 1] = new_beams.get(beam - 1, 0) + n
                new_beams[beam + 1] = new_beams.get(beam + 1, 0) + n
            else:
                new_beams[beam] = new_beams.get(beam, 0) + n
        beams = new_beams
    return sum(new_beams.values())

def main(input_file):
    start_x, splitters = parse_input(input_file)
    print("Part 1:", count_splits(start_x, splitters))
    print("Part 1:", count_timelines(start_x, splitters))

if __name__ == '__main__':
    main(sys.argv[1])
