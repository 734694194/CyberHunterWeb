from fpdf import FPDF
import os
from datetime import datetime

def generate_report(phone, message):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"report_{timestamp}.pdf"
    filepath = os.path.join("reports", filename)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="🚨 تقرير ابتزاز إلكتروني 🚨", ln=True, align="C")
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"رقم المبتز: {phone}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"الرسالة:\n{message}")
    pdf.output(filepath)

    return filepath
