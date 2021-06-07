from fpdf import FPDF

pdf = FPDF = FPDF()

# Add new page. Without this you cannot create the document.
pdf.add_page()

# Remember to always put one of these at least once for text.
pdf.set_font('Arial', 'U', 30)
pdf.set_margins(10,10,10)

# Create cell gap
pdf.cell(60)

# Title of the Report
pdf.cell(50, 35, 'Specified Project')

# Format for text in description
pdf.set_font('Times', 'B', 16)
pdf.set_text_color(35,56,89)
pdf.cell(-190, 105, 'Report :', 0, 1, 'C')

pdf.set_font('Arial', 'U', 16)
pdf.set_text_color(200,60,0)
pdf.cell(85, -105, 'Datafile', 0, 1, 'C')

pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(40,0,100)
pdf.cell(35, 125, '#Value :', 0, 1, 'C')

pdf.set_font('Arial', 'U', 16)
pdf.set_text_color(0,100,0)
pdf.cell(90, -125, '00001', 0, 1, 'C')

pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(0,0,40)
pdf.cell(35, 145, 'Version :', 0, 1, 'C')

pdf.set_font('Arial', 'U', 16)
pdf.set_text_color(40,0,0)
pdf.cell(88, -145, '2.17', 0, 1, 'C')

pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(0,40,0)
pdf.cell(30, 165, 'Year :', 0, 1, 'C')

pdf.set_font('Arial', 'U', 16)
pdf.set_text_color(3,0,0)
pdf.cell(88, -165, '2021', 0, 1, 'C')

pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(0,3,0)
pdf.cell(20, 185, 'Release :', 0, 1, 'C')

pdf.set_font('Arial', 'U', 16)
pdf.set_text_color(0,0,3)
pdf.cell(105, -185, 'January 2,2021', 0, 1, 'C')

# Adding image in the report.
pdf.image('charts.jpg', x=85, y=40, w=100, h=100, type='', link='')

# Effective page width, or just epw
epw = pdf.w - 2 * pdf.l_margin

# Set column width to 1/4 of effective page width to distribute content
# evenly across table and page
col_width = epw / 4

# Data to be displayed in table
data = [['Author', 'Book', 'Serial', 'Sales'],
        ['A', 'G', 34, '20000'],
        ['B', 'H', 45, '43539'], [
            'C', 'I', 19, '18273'],
        ['D', 'J', 87, '12321'],
        ['E', 'K', 12, '245675'],
        ['F', 'L', 34, '765456'],
        ]

pdf.set_font('Times', '', 10.0)
pdf.ln(0.5)

# Text height is the same as current font size
th = pdf.font_size

# Line break
pdf.ln(45 * th)

# Set fonts for table
pdf.set_font('Times', 'B', 20.0)
pdf.set_text_color(0,200,0)
pdf.cell(epw, 0.0, 'Tabular Data', align='C')
pdf.set_font('Times', '', 15.0)
# Adding line breaks
pdf.ln(5)

# Here we add more padding by passing 2*th as height
for row in data:
    for datum in row:
        # Enter data in columns
        pdf.cell(col_width, 2 * th, str(datum), border=1)

    pdf.ln(2 * th)  # gap in tabs

# Output file in pdf format
pdf.output('PythonPdfSampleReport.pdf')





