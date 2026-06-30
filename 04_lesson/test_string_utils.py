import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# capitalize()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("test", "Test"),
    ("my name", "My name"),
    ("привет", "Привет"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("456test", "456test"),
    ("", ""),
    ("!!!hello", "!!!hello"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# trim()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("    hello", "hello"),
    (" python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),
    ("", ""),
    (" ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# contains()


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("12345", "3", True),
    ("Hello World", " ", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "S", False),
    ("SkyPro", " ", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# delete_symbol()


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("12345", "3", "1245"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", "SkyPro"),
    ("", "S", ""),
    ("SkyPro", "", "SkyPro"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
