from src.puzzles.day_1.solution import sum_calibration_values, sum_calibration_values2


def test_sum_calibration_values():
    assert sum_calibration_values(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 142


def test_sum_calibration_values2():
    assert (
        sum_calibration_values2(
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ]
        )
        == 281
    )
