x = 50
y = [25, 10, 5]
wer = 0

while x > 0:
    print(f'Amount Due: {x}')
    i = int(input('Insert coin: '))
    if i in y:
        x -= i
        wer += i

if wer >= x:
    print(f'Change Owed: {wer - 50}')