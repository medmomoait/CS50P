def main():
    x = input('Fraction: ')
    y = convert(x)
    print(gauge(y))

def convert(fraction):
    try:
        a, b = map(int, fraction.split("/"))
        if b == 0:
            raise ZeroDivisionError
        if a > b:
            raise ValueError
        return round(a / b * 100)
    except ValueError:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'

if __name__ == "__main__":
    main()