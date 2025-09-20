from um import count

def test_single_um():
    assert count("hello, um, world") == 1

def test_multiple_ums():
    assert count("um um um") == 3

def test_embedded_um():
    assert count("yummy umbrella momentum") == 0

def test_case_insensitive():
    assert count("Um UM uM") == 3

def test_with_punctuation():
    assert count("Um? Well, um... yes.") == 2
