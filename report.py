import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Step 1: Read data
data = pd.read_csv("students.csv")

# Step 2: Analyze data
average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()

# Step 3: Create PDF
file_name = "student_report.pdf"
pdf = canvas.Canvas(file_name, pagesize=A4)
width, height = A4

# Title
pdf.setFont("Helvetica-Bold", 16)
pdf.drawCentredString(width / 2, height - 50, "Student Performance Report")

# Summary Section
pdf.setFont("Helvetica", 12)
pdf.drawString(50, height - 100, f"Average Marks: {average_marks:.2f}")
pdf.drawString(50, height - 130, f"Highest Marks: {highest_marks}")
pdf.drawString(50, height - 160, f"Lowest Marks: {lowest_marks}")

# Table Header
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(50, height - 220, "Name")
pdf.drawString(300, height - 220, "Marks")

# Table Data
y = height - 250
pdf.setFont("Helvetica", 12)
for index, row in data.iterrows():
    pdf.drawString(50, y, row["Name"])
    pdf.drawString(300, y, str(row["Marks"]))
    y -= 30

# Save PDF
pdf.save()

print("PDF report generated successfully: student_report.pdf")
