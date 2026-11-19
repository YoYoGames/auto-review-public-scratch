"""Print the average of the numbers in a file, one per line."""

import sys


def average(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)


def read_numbers(path):
    with open(path) as f:
        return [float(line) for line in f if line.strip()]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: average.py FILE")
    print(average(read_numbers(sys.argv[1])))
