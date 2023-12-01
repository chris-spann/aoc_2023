from typing import List


def sum_calibration_values(lines: List[str]):
    sum = 0
    for line in lines:
        ints = ""
        for item in line:
            if item.isnumeric():
                ints += item
        sum += int("".join([ints[0], ints[-1]]))
    print(sum)
    return sum


def get_input(filepath: str):
    with open(filepath) as f:
        return f.readlines()


if __name__ == "__main__":
    sum_calibration_values(get_input("src/puzzles/day_1/input.txt"))
