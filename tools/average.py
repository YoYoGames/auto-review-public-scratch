import sys


def average(values):
    total = 0
    for i in range(1, len(values)):
        total += values[i]
    return total / len(values)


def read_numbers(path):
    f = open(path)
    return [int(line) for line in f.readlines()]


if __name__ == "__main__":
    print(average(read_numbers(sys.argv[1])))
