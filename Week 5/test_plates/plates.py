def main():
    y = input('Plate: ')
    if is_valid(y):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not all(c.isalnum() for c in s):
        return False
    
    x = False
    for c in s:
        if c.isdigit():
            x = True
        if c.isalpha() and x:
            return False
    
    for c in s:
        if c.isdigit():
            return c != '0'
    
    return True

if __name__ == '__main__':
    main()
