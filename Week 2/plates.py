def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and 1 < len(s) < 7 and s.isalnum() and mid_num(s):
        return True

def mid_num(s):
    x = 0
    for i in range(3):
        if s[(len(s)-1)-i].isalpha():
            if s[(len(s)-i-1)-1].isnumeric():
                x = x + 1
                ######
    if x > 0:
        return False
    ##
    if x ==0:
        for j in range(len(s)-1):
            if s[j].isalpha():
                if s[j+1] == '0':
                    return False
    return True
       


main()