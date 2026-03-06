#! /usr/bin/python3
import sys

def max_joltage(bank, n):
    digits = []
    for i in range(n):
        if i == n - 1:
            digits.append(max(bank))
        else:
            digit = max(bank[:-(n - i - 1)])
            bank = bank[bank.index(digit) + 1:]
            digits.append(digit)
    return int(''.join(digits))

def main(input_file):
    banks = open(input_file).read().strip().split('\n')
    print("Part 1:", sum(max_joltage(bank, 2) for bank in banks))
    print("Part 2:", sum(max_joltage(bank, 12) for bank in banks))

if __name__ == '__main__':
    main(sys.argv[1])
