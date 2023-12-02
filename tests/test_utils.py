import tempfile
from utils import read_file, get_input_file_path, get_input


def test_read_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"Hello\nWorld")
        tmp.close()
        assert read_file(tmp.name) == ["Hello\n", "World"]


def test_get_input_file_path():
    filename = "test.txt"
    assert get_input_file_path(__file__, filename).endswith(filename)


def test_get_input():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"Hello\nWorld")
        tmp.close()
        assert get_input(__file__, tmp.name) == ["Hello\n", "World"]
