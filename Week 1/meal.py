def main():

    x = input('What time is it: ')
    x = convert(x)
    if 7 <= x <= 8:
        print('breakfast time')
    elif 12 <= x <= 13:
        print('lunch time')
    elif 18 <= x <= 19:
        print('dinner time')

def convert(x):

    if x.endswith(' a.m. '):
        x = x.split(' a.m. ')
        x = x[0].split(':')
        return round(int(x[0]) + int(x[1])/60, 2)
    elif x.endswith(' p.m. '):
        x = x.split(' p.m. ')
        x = x[0].split(':')
        return round(12 + int(x[0]) + int(x[1])/60, 2)

    else:
        x = x.split(':')
        return round(int(x[0]) + int(x[1])/60, 2)


if __name__ == "__main__":
    main()