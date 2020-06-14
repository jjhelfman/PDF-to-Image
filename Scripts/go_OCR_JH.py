# Project Title: Kenneth E. Batcher Historical Work OCR
# Project Description: Project to conduct OCR on the historical work of PP-father Kenneth E. Batcher
# Author:  Matthew E. Miller
# Date: 02/01/2020 10:38:31
# Medium: https://medium.com/@matthew_earl_miller (where this is being published)
# Github: https://github.com/matmill5
# Linkedin: https://www.linkedin.com/in/matthew-miller-engineer/
# StackOverflow: https://stackoverflow.com/users/11937169/matthew-e-miller?tab=profile
# (c) Copyright by Matthew E. Miller

import pytesseract
from PIL import Image
import sys
from pdf2image import convert_from_path
import os
import io

# Note:  Don't run this on my development laptop, will take up too much storage space with all of the image files.
# Note:  Run this on my desktop machine.

# Note:  The command below is good for setting the pytesseract path, if that becomes an issue. 
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Matthew\AppData\Local\Tesseract-OCR\tesseract.exe'

# For each pdf in the pdfs directory, convert the pdf to a jpg, do ocr on the jpg, and print the results to a results_filename[0:20].txt
for pdf in os.listdir('As-Builts 1'):
    pdf_path = str(pdf)
    output_filename = "results_" + pdf_path.split('/')[-1].replace('.pdf','')[0:20] + ".txt"
    pages = convert_from_path(pdf_path)
    pg_cntr = 1

    sub_dir = str("images/" + pdf_path.split('/')[-1].replace('.pdf','')[0:20] + "/")
    if not os.path.exists(sub_dir):
        os.makedirs(sub_dir)

    for page in pages:
        # if pg_cntr <= 20:
        filename = "pg_"+str(pg_cntr)+'_'+pdf_path.split('/')[-1].replace('.pdf','.jpg')
        page.save(sub_dir+filename)
        with io.open(output_filename, 'a+', encoding='utf8') as f:
            f.write(unicode("======================================================== PAGE " + str(pg_cntr) + " ========================================================\n"))
            f.write(unicode(pytesseract.image_to_string(sub_dir+filename)+"\n"))
            f.write(unicode("======================================================== ========================= ========================================================\n"))
        pg_cntr = pg_cntr + 1


