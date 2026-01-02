import tempfile
from fpdf import FPDF

def export_to_pdf(name, email, school, degree, skills, bullets):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, name.upper(), ln=True)

    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, f"{email} | {school}", ln=True)
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 8, degree.upper(), ln=True)
    pdf.ln(6)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 8, "SKILLS", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 6, skills)
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 8, "EXPERIENCE", ln=True)
    pdf.set_font("Helvetica", "", 10)

    for bullet in bullets:
        pdf.multi_cell(0, 6, f"- {bullet}")

    fd, path = tempfile.mkstemp(suffix=".pdf")
    pdf.output(path)
    return path
