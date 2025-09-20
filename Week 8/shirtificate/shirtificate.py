from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C", ln=1)

    # Shirt image (centered)
    pdf.image("shirtificate.png", x=(210-150)//2, y=40, w=150)

    # Name text (centered on shirt, white)
    pdf.set_xy(0, 110)
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(210, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()