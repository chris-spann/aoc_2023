from typing import List

from utils import get_input


def sum_valid_game_ids(lines: List[str]):
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    for line in lines:
        game_id, data = line.split(":")
        rounds = [round.strip() for round in data.split(";")]
        game_id = game_id.split(" ")[1]
        is_allowed = True
        for round in rounds:
            vals = round.split(",")
            for v in vals:
                cubes, color = v.strip().split(" ")
                if int(cubes) > max_cubes[color]:
                    is_allowed = False
        if is_allowed:
            sum += int(game_id)

    print(f"sum: {sum}")
    return sum


def sum_minimum_cubes_power(lines: List[str]):
    sum = 0
    for line in lines:
        cubes_needed = {"blue": 0, "red": 0, "green": 0}
        game_id, data = line.split(":")
        rounds = [round.strip() for round in data.split(";")]
        game_id = game_id.split(" ")[1]
        for round in rounds:
            vals = round.split(",")
            for v in vals:
                cubes, color = v.strip().split(" ")
                if int(cubes) > cubes_needed[color]:
                    cubes_needed[color] = int(cubes)
        sum += cubes_needed["blue"] * cubes_needed["green"] * cubes_needed["red"]
    print(f"sum: {sum}")
    return sum


if __name__ == "__main__":
    sum_valid_game_ids(get_input(__file__))
    sum_minimum_cubes_power(get_input(__file__))
