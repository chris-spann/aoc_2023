import os
from typing import List
import inspect


def read_file(filepath: str) -> List[str]:
    with open(filepath) as f:
        return f.readlines()


def get_input_file_path(filename: str = "input.txt") -> str:
    dir_path = os.path.dirname(os.path.abspath(inspect.stack()[1][1]))
    file_path = os.path.join(dir_path, filename)
    return file_path


def get_input(file="input.txt"):
    return read_file(get_input_file_path(file))
