from twttr import shorten

def test_remove_vowels():
    assert shorten("Twitter") == "Twttr"
    assert shorten("AEIOU") == ""
    assert shorten("Hello, World!") == "Hll, Wrld!"
