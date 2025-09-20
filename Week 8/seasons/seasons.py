from datetime import date
import sys
import inflect

def main():
    birth_str = input("Date of Birth: ")
    try:
        birth_date = parse_date(birth_str)
    except ValueError:
        sys.exit("Invalid date")
    minutes = calculate_minutes(birth_date)
    print(convert_to_words(minutes))

def parse_date(birth_str):
    try:
        year, month, day = map(int, birth_str.split("-"))
        return date(year, month, day)
    except Exception:
        raise ValueError

def calculate_minutes(birth_date, today=None):
    if today is None:
        today = date.today()
    delta = today - birth_date
    return round(delta.days * 24 * 60)

def convert_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="").replace(",", "").capitalize()
    return f"{words} minutes"

if __name__ == "__main__":
    main()