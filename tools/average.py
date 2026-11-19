"""Print the average of the numbers in a file, one per line."""

import sys


def average(values: list[float]) -> float | None:
    if not values:  # nothing to average
        return None
    return sum(values) / len(values)


def read_numbers(path: str) -> list[float]:
    with open(path, encoding="utf-8") as f:
        return [float(line) for line in f if line.strip()]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(f"usage: {sys.argv[0]} FILE")
    print(average(read_numbers(sys.argv[1])))
