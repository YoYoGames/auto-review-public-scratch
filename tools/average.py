import sys


def average(values):
    if not values:
        return None
    return sum(values) / len(values)


def read_numbers(path):
    with open(path) as f:
        return [float(line) for line in f if line.strip()]


if __name__ == "__main__":
    print(average(read_numbers(sys.argv[1])))
