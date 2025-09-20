import sys
import csv

def main():
    
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith(".csv") or not output_file.endswith(".csv"):
        sys.exit("Input and output files must be CSV")
    
    try:
        with open(input_file, mode='r') as f:
            reader = csv.DictReader(f)
            students = []

            for row in reader:
                try:
                    last, first = row['name'].split(', ')
                    students.append({
                        "first": first, "last": last, "house": row["house"]
                    })
                except ValueError:
                    sys.exit("Invalid CSV format")
     
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")
    
    with open (output_file, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for student in students:
            writer.writerow(student)

if __name__ == "__main__":
    main()
