#! /usr/bin/python3
import sys

def main(input_file):
    dial = 50
    part1 = part2 = 0
    for word in open(input_file).read().split():
        direction, value = word[0], int(word[1:])
        rotations, value = divmod(value, 100)
        if direction == 'L':
            value = -value
        new_dial = (dial + value) % 100
        part1 += new_dial == 0
        part2 += rotations + (new_dial == 0)
        if dial != 0 and new_dial != 0 and not (0 <= (dial + value) < 100):
            part2 += 1
        dial = new_dial
    print("Part 1:", part1)
    print("Part 2:", part2)

if __name__ == '__main__':
    main(sys.argv[1])
