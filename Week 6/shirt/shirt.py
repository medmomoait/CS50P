import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = [".jpg", ".jpeg", ".png"]

    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid input")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    if not os.path.exists(input_file):
        sys.exit("Input file does not exist")

    try:
        input_image = Image.open(input_file)
        shirt_image = Image.open("shirt.png")
        resized_image = ImageOps.fit(input_image, shirt_image.size)
        resized_image.paste(shirt_image, shirt_image)
        resized_image.save(output_file)

    except Exception as e:
        sys.exit(f"Error processing image: {e}")

if __name__ == "__main__":
    main()
