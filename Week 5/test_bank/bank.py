def main():
    inp = input('Greeting: ')
    print(f'${value(inp)}')

def value(greeting):
    x = greeting.lower().strip()
    if x.startswith('hello'):
        return 0
    elif x.startswith('h'):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()