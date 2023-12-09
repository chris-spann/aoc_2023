from day_3.solution import sum_part_numbers


def test_day_3_part_1():
    lines = [
        "467..114..\n",
        "...*......\n",
        "..35..633.\n",
        "......#...\n",
        "617*......\n",
        ".....+.58.\n",
        "..592.....\n",
        "......755.\n",
        "...$.*....\n",
        ".664.598..\n",
    ]
    expected = 467 + 35 + 633 + 617 + 592 + 755 + 664 + 598
    assert sum_part_numbers(lines) == expected


def test_day_3_part_1_sequence():
    lines = [
        "123*456",
        "789.012",
        "*345.678",
    ]
    expected_result = 123 + 456 + 12 + 789 + 345
    assert sum_part_numbers(lines) == expected_result


# def test_day_3_part_2():
#     assert part_2([]) is None
