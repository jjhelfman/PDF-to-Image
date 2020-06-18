# PDF to Image batch script
 
###### Python code was adapted from https://gist.github.com/jimmyromanticdevil/691e97ce22f7cd43d6a9d54305344587

## Instructions

1. To use this script, you need to replicate the following folder structure (by cloning this):

    - PDF to Image//
        - Scripts// > pdfToImage_pdf2image.bat, pdfToImage_pdf2image.py, pdfToImage_wand.bat, pdfToImage_wand.py
        - Input//
            - subfolder1//, subfolder 2//... each containing pdfs
        - Output//
        - Logs//
            - pypdf_to_image.log

2. Install the required dependencies/modules via pip install -r requirements.txt

3. After organizing the pdfs in different named folders in the Input folder, run the batch script or python script by double clicking the respective .bat or .py file in the Scripts folder.

## Notes
Adjust the variables per your specific environment and requirements. 

1. pdfToImage_pdf2image.py: 
    - If you observe a decompression bomb warning, it's a Pillow feature and can be disabled if you ever need to. This warning feature indicates the image is too large and may crash the program. 
    - API/docs: https://pdf2image.readthedocs.io/en/latest/ 
2. pdfToImage_wand.py:
    - If the output is not as expected: adjust the Image() object's paramaters in the python script as needed
    - API/docs: http://docs.wand-py.org/en/0.6.1/wand/image.html)