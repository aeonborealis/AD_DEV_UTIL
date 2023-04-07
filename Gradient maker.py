import random
import math
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Define the size of the canvas
PAGE_WIDTH, PAGE_HEIGHT = letter

# Create a new canvas
pdf_canvas = canvas.Canvas("gradient.pdf", pagesize=letter)

# Define the number of gradient steps
STEPS = 1000

# Define the colors of the gradient
colors = [(random.random(), random.random(), random.random()) for i in range(STEPS)]

# Draw the gradient
for i in range(STEPS):
    r, g, b = colors[i]
    pdf_canvas.setStrokeColorRGB(r, g, b)
    pdf_canvas.setFillColorRGB(r, g, b)
    pdf_canvas.rect(0, i*(PAGE_HEIGHT/STEPS), PAGE_WIDTH, (PAGE_HEIGHT/STEPS), fill=1)

# Save the PDF file
pdf_canvas.save()
