from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table
)
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_report(
    output_path,
    waveform_image,
    metrics
):
    doc = SimpleDocTemplate(output_path)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Audio Quality Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    table_data = [
        ["Metric", "Value"],
        ["Duration (sec)", f"{metrics['duration']:.2f}"],
        ["LUFS", f"{metrics['lufs']:.2f}"],
        ["Clipping samples", metrics['clipping_count']],
        ["Long pauses", metrics['pause_count']],
    ]

    table = Table(table_data)
    elements.append(table)
    elements.append(Spacer(1, 12))

    elements.append(Image(waveform_image, width=500, height=150))

    doc.build(elements)
