from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.line(10, 21, 200, 21)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    pdf.ln(265)

    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
    height = 31

    for _ in range(27):
        pdf.line(10, height, 200, height)
        height += 10

    for _ in range(row["Pages"] - 1):
        pdf.add_page()

        pdf.ln(277)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
        height = 20
        for i in range(28):
            pdf.line(10, height, 200, height)
            height += 10
pdf.output("output.pdf")
