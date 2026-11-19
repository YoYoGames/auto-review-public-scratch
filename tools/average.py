import sys


def average(values):
    if not values:
        return None
    return sum(values) / len(values)


def read_numbers(path):
    f = open(path)
    return [int(line) for line in f.readlines()]


if __name__ == "__main__":
    print(average(read_numbers(sys.argv[1])))
