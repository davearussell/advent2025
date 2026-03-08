#! /usr/bin/python3
import sys

def main(input_file):
    boxes = [tuple(map(int, line.split(','))) for line in open(input_file).read().strip().split('\n')]

    distances = []
    for i0, (x0, y0, z0) in enumerate(boxes):
        for i1, (x1, y1, z1) in enumerate(boxes[i0 + 1:]):
            dist = (abs(x1 - x0) ** 2) + (abs(y1 - y0) ** 2) + (abs(z1 - z0) ** 2)
            distances.append((dist, i0, i0 + i1 + 1))
    distances.sort()

    circuits = []
    for i, (d, i0, i1) in enumerate(distances):
        if i == (1000 if len(boxes) == 1000 else 10):
            circuits.sort(key=lambda x: -len(x))
            print("Part 1:", len(circuits[0]) * len(circuits[1]) * len(circuits[2]))
        new_circuit = {i0, i1}
        matches = [c for c in circuits if c & new_circuit]
        if not matches:
            circuits.append(new_circuit)
        else:
            if len(matches) == 1:
                circuit = matches[0]
                circuit |= new_circuit
            else:
                circuit, c2 = matches
                circuits.remove(c2)
                circuit |= c2
            if len(circuit) == len(boxes):
                print("Part 2:", boxes[i0][0] * boxes[i1][0])
                break

if __name__ == '__main__':
    main(sys.argv[1])
