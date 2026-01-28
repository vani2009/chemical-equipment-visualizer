import io
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch


def generate_pdf_report(dataset):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("<b>Equipment Analysis Report</b>", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))

    summary = dataset.summary

    table_data = [
        ["Metric", "Value"],
        ["Total Equipment", summary["total_equipment"]],
        ["Avg Flowrate", f'{summary["avg_flowrate"]:.2f}'],
        ["Avg Pressure", f'{summary["avg_pressure"]:.2f}'],
        ["Avg Temperature", f'{summary["avg_temperature"]:.2f}'],
    ]

    table = Table(table_data, colWidths=[3 * inch, 2 * inch])
    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.5 * inch))

    # chart
    dist = summary["type_distribution"]
    fig, ax = plt.subplots()
    ax.bar(dist.keys(), dist.values())
    plt.tight_layout()

    img_buf = io.BytesIO()
    plt.savefig(img_buf, format="png")
    plt.close()
    img_buf.seek(0)

    elements.append(Image(img_buf, width=5 * inch, height=3 * inch))
    doc.build(elements)

    buffer.seek(0)
    return buffer
