# test_numb3rs.py

from numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.0") is True
    assert validate("1.2.3.4") is True

def test_out_of_range():
    assert validate("256.100.100.100") is False
    assert validate("1000.1.2.3") is False
    assert validate("512.512.512.512") is False

def test_leading_zeros():
    assert validate("192.168.001.1") is False
    assert validate("01.02.03.04") is False
    assert validate("00.0.0.0") is False

def test_invalid_format():
    assert validate("cat") is False
    assert validate("...") is False
    assert validate("1.2.3") is False
    assert validate("1.2.3.4.5") is False
    assert validate("1.2.3.4.") is False
    assert validate(".1.2.3.4") is False
