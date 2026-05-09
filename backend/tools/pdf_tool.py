from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_pdf(filename: str, content: str):

    file_path = f"{filename}.pdf"

    c = canvas.Canvas(file_path, pagesize=letter)

    width, height = letter

    y = height - 50

    for line in content.split("\n"):
        c.drawString(50, y, line[:100])
        y -= 15

        if y < 50:
            c.showPage()
            y = height - 50

    c.save()

    return file_path