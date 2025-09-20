from working import convert
import pytest

def test_full_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'

def test_partial_times():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5:00 PM') == '09:00 to 17:00'

    with pytest.raises(ValueError):
        convert('9 AM to % PM')

def test_invalid_formats():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:00 PM')

    with pytest.raises(ValueError):
        convert('13:00 AM to 5:00 PM')

def test_reversed_periods():
    assert convert('5:00 PM to 9:00 AM') == "17:00 to 09:00"

def test_missing_to_separator():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
