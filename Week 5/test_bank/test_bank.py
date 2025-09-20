from bank import value

def test_value_h():
    assert value("How are you") == 20
    assert value("How much") == 20

def test_value_hello():
    assert value("Hello") == 0

def test_value_other():
    assert value('Where are you going') == 100