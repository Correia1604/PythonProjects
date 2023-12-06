'''import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write('result.pdf')'''

import PyPDF2
import os

# Input and output folder paths
input_folder = r'./pdf'
output_folder = r'./pdf'
output_file = 'result.pdf'

# Initialize PdfMerger
merger = PyPDF2.PdfMerger()

# Loop through PDF files in the input folder
for file in os.listdir(input_folder):
    if file.endswith(".pdf"):
        file_path = os.path.join(input_folder, file)
        merger.append(file_path)

# Save the merged PDF in the output folder
output_path = os.path.join(output_folder, output_file)
merger.write(output_path)

# Close the PdfMerger object
merger.close()
