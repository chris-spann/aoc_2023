from typing import List
from utils import get_input


def is_symbol(s: str | None) -> bool:
    # if value is not numeric and also not a "."
    if s and not s.isnumeric() and s != ".":
        return True
    return False


def has_neighboring_symbol(matrix: List[List], i: int, j: int) -> bool:
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for direction in directions:
        new_i = i + direction[0]
        new_j = j + direction[1]
        if new_i >= 0 and new_i < len(matrix) and new_j >= 0 and new_j < len(matrix[0]):
            if is_symbol(matrix[new_i][new_j]):
                return True
    return False


def sum_part_numbers(lines: List[str]) -> int:
    sum = 0
    vals_to_sum = []
    # build matrix
    matrix = []
    for line in lines:
        new_line = []
        for char in line:
            if char != "\n":
                new_line.append(char)
        matrix.append(new_line)
    integer_coords = []
    # loop through matrix to create a list of coords where there are integers
    for i in range(len(matrix)):
        in_sequence = False
        row, start = 0, 0
        for j in range(len(matrix[i])):
            if matrix[i][j].isnumeric():
                if not in_sequence:
                    row = i
                    start = j
                    in_sequence = True
            else:
                if in_sequence:
                    stop = j - 1
                    integer_coords.append((row, start, stop))
                    in_sequence = False

        if in_sequence:
            stop = len(matrix[i]) - 1
            integer_coords.append((row, start, stop))

    # loop through coords, use value to loop through each range....
    for coord in integer_coords:
        # if any value has an neighboring symbol...
        if any(
            [has_neighboring_symbol(matrix, coord[0], i) for i in range(coord[1], coord[2] + 1)]
        ):
            # join the range in to one string and add to list
            vals_to_sum.append(int("".join(matrix[coord[0]][coord[1] : coord[2] + 1])))
            sum += int("".join(matrix[coord[0]][coord[1] : coord[2] + 1]))
    print(f"sum: {sum}")

    return sum


if __name__ == "__main__":  # pragma: no cover
    lines = get_input(__file__)
    sum_part_numbers(lines)
