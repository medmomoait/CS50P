x, y, z = input('Expression: ').split()
z = int(z)
x = int(x)

match y:
    case '-':
        print(f'{x - z:.1f}')
    
    case '/':
        print(f'{x / z:.1f}')

    case '+':
        print(f'{x + z:.1f}')
    
    case '*':
        print(f'{x * z:.1f}')