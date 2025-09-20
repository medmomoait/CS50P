stuff = []

while True:
    try:
        x = input().upper()
    except EOFError:
        print('')
        break
    else:
        stuff.append(x)

stuff.sort()

y = 0

for _ in stuff:
    z = 0
    if y == 0 or stuff[y] != stuff[y - 1]:
        if stuff[y] != stuff[-1]:
            d = y
            while stuff[1] == stuff[y+1]:
                z += 1
                d += 1
        elif len(stuff) == 2 and stuff[y] == stuff[y - 1]:
            z += 1
        print(z + 1, _)

    y += 1
        
