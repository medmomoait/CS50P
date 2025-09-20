import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2}(?::\d{2})?) (AM|PM) to (\d{1,2}(?::\d{2})?) (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    start_time, start_period, end_time, end_period = match.groups()
    start_24 = to_24_hour(start_time, start_period)
    end_24 = to_24_hour(end_time, end_period)
    return f"{start_24} to {end_24}"

def to_24_hour(time_str, period):
    parts = time_str.split(':')
    hour = int(parts[0])
    minute = int(parts[1]) if len(parts) == 2 else 0

    if hour > 12 or minute >= 60:
        raise ValueError("Invalid time")

    if period == 'AM':
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()