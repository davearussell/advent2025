#! /usr/bin/env python3
import sys

def make_perimeter(tiles):
    facings = []
    for i in range(len(tiles)):
        x, y = tiles[i]
        nx, ny = tiles[(i + 1) % len(tiles)]
        facings.append(0 if y > ny else 1 if x < nx else 2 if y < ny else 3)

    turns = 0
    for i in range(len(tiles)):
        next_facing = facings[i]
        prev_facing = facings[(i - 1) % len(tiles)]
        turns += 1 if next_facing == (prev_facing + 1) % 4 else -1
    assert turns == -4 or turns == 4
    is_clockwise = (turns == 4)
    offset = 0.25 if is_clockwise else -0.25

    perimeter_points = []
    for i, (x, y) in enumerate(tiles):
        prev_facing = facings[(i - 1) % len(tiles)]
        next_facing = facings[i]
        if next_facing & 1:
            x += offset * (1 if prev_facing & 2 else -1)
            y += offset * (1 if next_facing & 2 else -1)
        else:
            x += offset * (1 if next_facing & 2 else -1)
            y += offset * (1 if prev_facing & 2 else -1)
        perimeter_points.append((x, y))

    perimeter_lines = list(zip(perimeter_points, perimeter_points[1:] + [perimeter_points[0]]))
    return perimeter_lines

def intersect(point, lines):
    px, py = point
    for (x, y0, y1) in lines:
        if y0 < py < y1:
            if x < px:
                first = px - x
            else:
                return (first, x - px)
    assert 0, "unreachable"

def main(input_file):
    tiles = [tuple(map(int, x.split(','))) for x in open(input_file).read().strip().split()]
    def size(t0, t1):
        return abs(t1[0] - t0[0] + 1) * abs(t1[1] - t0[1] + 1)
    print("Part 1:", max(size(a, b) for a in tiles for b in tiles))

    perimeter_lines = make_perimeter(tiles)
    xlines = []
    ylines = []
    for ((x0, y0), (x1, y1)) in perimeter_lines:
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
        if y0 == y1:
            xlines.append((y0, x0, x1))
        else:
            ylines.append((x0, y0, y1))
    xlines.sort()
    ylines.sort()

    safe_distances = []
    for x, y in tiles:
        l, r = intersect((x, y), ylines)
        u, d = intersect((y, x), xlines)
        safe_distances.append((u, r, d, l))

    def p2_size(i0, i1):
        x0, y0 = tiles[i0]
        x1, y1 = tiles[i1]

        u0, r0, d0, l0 = safe_distances[i0]
        u1, r1, d1, l1 = safe_distances[i1]

        dx = x1 - x0
        dy = y1 - y0
        okay = ( dx < r0 and -dx < l0 and
                -dx < r1 and  dx < l1 and
                 dy < d0 and -dy < u0 and
                -dy < d1 and  dy < u1)
        return (abs(dx) + 1) * (abs(dy) + 1) if okay else 0
    print("Part 2:", max(p2_size(a, b) for a in range(len(tiles)) for b in range(len(tiles))))

if __name__ == '__main__':
    main(sys.argv[1])
