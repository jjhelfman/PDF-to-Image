# PDF to Image 

## Change Log

- **12/24/2021**: Successfully tested using Python 3.7.4 and C:/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe.

## Scripts

1. pdfToImage_wand.py uses the wand module, is currently set to convert to JPGs, and has the following resolution specs (the resolution parameter is passed to the Image object)
    - 1000 res : ~ 10 sec per pg
    - 750 res: ~ 5 sec per pg
    - 300 res : ~ 2 sec per pg (much lower quality)

2. pdfToImage_pdf2image.py uses the pdf2image and Pillow modules, as well as the Poppler library. This script converts to PNG format.
    > This script may be more difficult to use due to the separate installation of the Poppler library (C:\\Program Files\\poppler-0.68.0\\bin). 
    > This script should only be ran if PNG outputs are needed - the script may perform a couple seconds faster per page than the wand script. 

## Instructions

1. Install the required dependencies via `pip install -r requirements.txt`
    - This requirements file was generated using pipreqs (https://pypi.org/project/pipreqs/)

2. Place the PDFs in appropriately named folder(s) in the directory, "\PDF to Image\Input". 

3. Run "pdfToImage_wand.py" by double clicking it or running from an IDE. 

    - If a PNG file is required or if desired results cannot be achieved with the wand script, try running "pdfToImage_pdf2image.py". Before running it, make sure the **popplerPath variable** is correctly specified (see Debugging section below for more info). 

4. If only parts of an image are needed, the image can be cropped using a program like Paint 3D. 

## Cloning and Set-Up 

1. Folder structure of PDF to Image:

    ├── Scripts/
    <br>
    &nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── pdfToImage_wand.py and pdfToImage_pdf2image.py (for PNG)
    <br>
    ├── Input/
    <br>
    &nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── subfolder1 with pdfs
    <br>
    &nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── subfolder2 with pdfs
    <br>
    &nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── ...
    <br>
    ├── Output/
    <br>
    &nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── subfolder1 with images
    <br>
    &nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── subfolder2 with images
    <br>
    &nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── ...
    <br>
    ├── Logs/
    <br>
    &nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── pypdf_to_image.log 

## Debugging

Adjust the variables per your specific environment and requirements.
And follow conventions/best practices according to the development team. For instance, raw strings and single backslashes may be preferred rather than the f strings used here. Another example is the if statement for making the output subfolders. This can be replaced by passing exist_ok=True to os.makedirs() in order to prevent exceptions when subfolders don't exist. 

1. pdfToImage_wand.py:
    - If the output is not as expected: adjust the Image() object's parameters in the Python script as needed
    - API/docs: http://docs.wand-py.org/en/0.6.1/wand/image.html)

2. pdfToImage_pdf2image.py: 
    - If the pdf2image script is not working or not reading any PDF pages, try downloading the latest Poppler version here: https://github.com/oschwartz10612/poppler-windows/releases/. Remember to set the bin directory to the popplerPath variable in the pdfToImage_pdf2image.py script.
    - If you get a decompression bomb warning, it's a Pillow feature and can be disabled if you ever need to. This warning feature indicates the image is too large and may crash the program. To disable the limit, add the line: `Image.MAX_IMAGE_PIXELS = None`. The warning can be disabled by importing the warnings module and adding the line: `warnings.simplefilter('ignore', Image.DecompressionBombWarning)`. Source: https://stackoverflow.com/a/25705844/11178099 
    - API/docs: https://pdf2image.readthedocs.io/en/latest/
