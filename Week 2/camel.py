x = input('camelCase: ')
y = ''

for c in x:
    if c.isupper():
        y = y + '_' + c.lower()
    else:
        y = y + c

print('snake_case:', x)