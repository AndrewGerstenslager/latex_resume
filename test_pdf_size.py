# %%
from PyPDF2 import PdfReader

# Open and read the uploaded PDF file
pdf_path = "resume_main.pdf"  # Assuming this is the latest uploaded file path
pdf_reader = PdfReader(pdf_path)

# Get page size (dimensions are usually in points)
page = pdf_reader.pages[0]  # Assuming a single-page PDF for this analysis
page_width = page.mediabox.width
page_height = page.mediabox.height

# Convert dimensions to inches (1 inch = 72 points)
page_width_inches = page_width / 72
page_height_inches = page_height / 72

(page_width_inches, page_height_inches)  # Display dimensions in inches
