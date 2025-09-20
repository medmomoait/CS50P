from tabulate import tabulate
import csv
import sys

def main():
    if len(sys.argv) < 2:
        exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        exit('Too many command-line arguments')
    else:
        if sys.argv[1][-4:] != '.csv':
            exit('Not a CSV file')
        else:
            print(tab(sys.argv[1]))

def tab(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            return tabulate(data[1:], headers=data[0], tablefmt='grid')
    except FileNotFoundError:
        exit('File does not exist')

if __name__ == "__main__":
    main()
