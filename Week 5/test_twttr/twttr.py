def main():
    txt = input("Input: ")
    print(f"Output: {shorten(txt)}")


def shorten(word):
    outp = ''
    for t in word:
        if t.lower() not in 'aeiou':
            outp += t
    return outp


if __name__ == "__main__":
    main()
