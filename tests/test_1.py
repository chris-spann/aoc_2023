from src.puzzles.day_1.solution import sum_calibration_values


def test_sum_calibratino_values():
    assert sum_calibration_values(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 142
