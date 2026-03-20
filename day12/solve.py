#! /usr/bin/python3
import re
import sys

def parse_input(path):
    pat = re.compile(r'(\d+)x(\d+): (.+)')
    shapes = []
    grids = []
    for section in open(path).read().strip().split('\n\n'):
        if '#' in section:
            shapes.append(section.strip().split('\n')[1:])
        else:
            for line in section.strip().split('\n'):
                w, h, counts = pat.match(line).groups()
                grid = ((int(w), int(h)), tuple(map(int, counts.split())))
                grids.append(grid)
    return shapes, grids

def can_fit(shapes, grid):
    (w, h), counts = grid
    region_area = w * h
    trivially_fits = (w // 3) * (h // 3)
    n_shapes = sum(counts)
    shape_area = sum(''.join(shapes[i]).count('#') * n for i, n in enumerate(counts))
    if trivially_fits >= n_shapes:
        return True
    if region_area < shape_area:
        return False
    assert 0, "fit not trivially resolvable"

def main(input_file):
    shapes, grids = parse_input(input_file)
    print("Part 1:", sum(can_fit(shapes, grid) for grid in grids))

if __name__ == '__main__':
    main(sys.argv[1])
