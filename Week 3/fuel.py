def main():
    fraction = hold_fraction('Fraction: ')
    print(fraction)

def hold_fraction(x):
    while True:
        try:
            fraction, y = input(x).split('/')
            if 0 <= int(fraction)/int(y) <= 0.1:
                return("E")
            elif 0.9 <= int(fraction)/int(y) <= 1:
                return('F')
            elif 0.1 < int(fraction)/int(y) < 0.9:
                return str(round(int(fraction)/int(y)*100)) + '%'
        except(ValueError, ZeroDivisionError):
            pass

main()