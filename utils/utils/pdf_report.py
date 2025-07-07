from fpdf import FPDF
import os
from datetime import datetime

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "📄 تقرير بلاغ ابتزاز", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_report(phone, message):
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{report_dir}/report_{phone}_{timestamp}.pdf"

    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"رقم المبتز: {phone}", ln=True)
    pdf.multi_cell(0, 10, f"محتوى الرسالة:\n{message}")
    pdf.output(filename)

    return filename
