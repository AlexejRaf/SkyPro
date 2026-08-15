import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("HELLO", "Hello"),
    ("123sky", "123sky"),
    ("", ""),
    (" ", " "),
    (" skypro ", "Skypro"),
])
def test_capitalize(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("   skypro", "skypro"),
    ("\tskypro", "skypro"),
    ("\nskypro", "skypro"),
    ("skypro ", "skypro "),
    (" sky pro ", "sky pro "),
    ("", ""),
    ("   ", ""),
])
def test_trim(utils, input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "r", True),
    ("SkyPro", "o", True),
    ("SkyPro", "U", False),
    ("SkyPro", "s", False),
    ("", "A", False),
])
def test_contains(utils, input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("skyprosky", "sky", "pro"),
    ("SkyPro", "x", "SkyPro"),
    ("SkyPro", "sky", "SkyPro"),
    ("", "a", ""),
    (" SkyPro ", "k", "SyPro"),
])
def test_delete_symbol(utils, input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected
