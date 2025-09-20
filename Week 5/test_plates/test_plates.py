from plates import is_valid

def test_len():
    assert is_valid("CS") == True
    assert is_valid('HellothisisCS50') == False
    assert is_valid('AABB20') == True

def test_two_letters():
    assert is_valid('1') == False
    assert is_valid('00') == False
    assert is_valid('A2') == False
    assert is_valid('CS') == True

def test_ponctuation():
    assert is_valid('CS50!') == False
    assert is_valid('CS50?') == False
    assert is_valid('CS50.') == False
    assert is_valid('CS50,') == False

def test_numbers():
    assert is_valid('ABC123') == True
    assert is_valid('ABC12D') == False
    assert is_valid('abc012') == False