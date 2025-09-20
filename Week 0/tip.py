def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f'Leave ${tip:.2f}')

def dollars_to_float(xc):
    xc = xc.strip('$')
    xc = float(xc)
    return xc

def percent_to_float(rdf):
    rdf = rdf.strip('%')
    rdf = float(rdf)/100
    return rdf

main()