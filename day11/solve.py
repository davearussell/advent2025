#! /usr/bin/python3
import sys

def parse_input(path):
    edges = {}
    for line in open(path).read().strip().split('\n'):
        lhs, rhs = line.split(':')
        edges[lhs] = set(rhs.split())
    return edges

def reverse(edges):
    rev = {}
    for src, dsts in edges.items():
        for dst in dsts:
            rev.setdefault(dst, set()).add(src)
    return rev

def order_nodes(edges):
    rev = reverse(edges)
    todo = set(edges) | set(rev)
    while todo:
        nodes = todo - set(rev)
        todo -= nodes
        for node in nodes:
            yield node
        for dst in list(rev):
            rev[dst] -= nodes
            if not rev[dst]:
                del rev[dst]

def count_paths(edges, src, dst):
    rev = reverse(edges)
    counts = {src: 1}
    for node in order_nodes(edges):
        if node != src:
            counts[node] = sum(counts[n] for n in rev.get(node, []))
    return counts[dst]

def main(input_file):
    edges = parse_input(input_file)
    print("Part 1:", count_paths(edges, 'you', 'out'))

    first, second = 'fft', 'dac'
    n = count_paths(edges, first, second)
    if n == 0:
        first, second = second, first
        n = count_paths(edges, first, second)
    n *= count_paths(edges, 'svr', first)
    n *= count_paths(edges, second, 'out')
    print("Part 2:", n)

if __name__ == '__main__':
    main(sys.argv[1])
