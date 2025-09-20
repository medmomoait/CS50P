import inflect

def main():

    x = inflect.engine()
    nms = []

    while True:
        try:
            n = input("Name: ")
        except EOFError:
            print()
            break
        else:
            nms.append(n)

    print(f"Adieu, adieu, to {x.join(nms)}")

main()