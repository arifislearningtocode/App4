import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob('Text Files/*.txt')

pdf = FPDF(orientation='P', unit="mm", format='A4')

for filepath in filepaths:
    filename = Path(filepath).stem
    pdf.add_page()
    pdf.set_font(family="Times", style='B', size=24)
    pdf.cell(align='L', w=50, h=8, txt=f"{filename.title()}")

pdf.output(f"PDFS/output.pdf")
