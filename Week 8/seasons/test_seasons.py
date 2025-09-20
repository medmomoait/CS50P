import pytest
from datetime import date
from seasons import parse_date, calculate_minutes, convert_to_words

def test_parse_date_valid():
    assert parse_date("2000-01-01") == date(2000, 1, 1)

def test_parse_date_invalid_format():
    with pytest.raises(ValueError):
        parse_date("01-01-2000")

def test_parse_date_non_numeric():
    with pytest.raises(ValueError):
        parse_date("January 1, 2000")

def test_calculate_minutes_exact_year():
    birth = date(2024, 9, 11)
    today = date(2025, 9, 11)
    assert calculate_minutes(birth, today) == 525600

def test_calculate_minutes_leap_year():
    birth = date(2020, 2, 29)
    today = date(2021, 3, 1)
    assert calculate_minutes(birth, today) == 527040

def test_calculate_minutes_one_day():
    birth = date(2024, 9, 10)
    today = date(2024, 9, 11)
    assert calculate_minutes(birth, today) == 1440

def test_convert_to_words_basic():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand six hundred minutes"

def test_convert_to_words_leap():
    assert convert_to_words(527040) == "Five hundred twenty-seven thousand forty minutes"