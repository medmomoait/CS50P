x = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input('Date: ').strip()
    try:
        mm, dd, yyyy = date.split('/')
        mm = int(mm)
    except ValueError:
        pass
    else:
        if int(dd) < 32 and mm < 13:
            print(f"{yyyy.zfill(4)}-{mm:02}-{dd.zfill(2)}", end='')
            break
    try:
        ss1, yyyy = date.split(', ')
        mm, dd = ss1.split()
        mm = str((x.index(mm))+1)
    except(ValueError, KeyError):
        pass
    else:
        if int(dd) < 32 and int(mm) < 13:
            print(f"{yyyy.rjust(4, '0')}-{mm.rjust(2, '0')}-{dd.rjust(2, '0')}", end='')
            break
        