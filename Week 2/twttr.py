def main():
    txt = input('Input: ')
    outp = ''
    
    for t in txt:

        if matchivowel(t):
            outp += t
    
    print(f"Output: {outp}")

def matchivowel(x):

    if x not in 'a,e,i,o,u, A, E, I, O, U':
        return True



main()