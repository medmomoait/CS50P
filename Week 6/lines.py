import sys
import os

def main():
    # Check for exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    # Check if file ends with .py
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Check if file exists
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with open(filename) as file:
            count = 0
            for line in file:
                stripped = line.lstrip()
                if stripped.startswith("#") or stripped == "":
                    continue  # skip comments and blank lines
                count += 1
        print(count)
    except FileNotFoundError:
        sys.exit("Could not open file")

if __name__ == "__main__":
    main()
