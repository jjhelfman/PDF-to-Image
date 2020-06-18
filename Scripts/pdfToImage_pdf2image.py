# Folder structure of PDF to Image:
# ├── Scripts/
# |   └── pdfToImage_pdf2image.py
# |
# ├── Input/
# |   ├── subfolder1 with pdfs
# |   ├── subfolder2 with pdfs
# |   └── ...
# |
# ├── Output/
# |
# ├── Logs/
#     └── pypdf_to_image.log

# Import modules
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
)
import os
import re
import logging

# Define vars
popplerPath = f"C:\\Program Files\\poppler-0.68.0\\bin"
inputFolder = f"Input"
imageFormat = f"png"

# Change current working directory (CWD) to Project's "PDF to Image" folder
# Start from Scripts folder
parentFolder = os.path.dirname(os.path.abspath(__file__))
# Move up one folder from current Scripts folder
os.chdir(os.path.dirname(parentFolder))
# Configure log messages
logging.basicConfig(filename='Logs\\pypdf_to_image.log', 
    level=logging.DEBUG, 
    format='%(asctime)s -  %(levelname)s -  %(message)s')
# Log the CWD
logging.info(f"The current working directory is {os.getcwd()}")

def convert(inputFolder, subfolder, filepdf):
	'''
	Converts pdf files to jpg files
	Args:
		subfolder: The subfolder string from the findToConvert() function
		filepdf: The pdf file string from the findToConvert() function
	Returns:
		N/A
	'''
	# Try to convert pdf to image,
	# other wise handle the error
	try:
		# Convert the pdf to a PNG image, at a resolution of 750
		# 750 res : ~ 6 sec per pg
		# Define the list of images from the path
		images = convert_from_path(pdf_path=f"{inputFolder}\\{subfolder}\\{filepdf}", dpi=750, fmt=imageFormat, poppler_path=popplerPath)
		# Define the output path
		out_path = f"Output\\{subfolder}\\"
		# Define the file name, without extension
		file_name = re.sub(".pdf$", "", filepdf)

		# Log the number of pages in the pdf
		logging.info(f"'{file_name}' contains {len(images)} page(s)")
		# If the directory isn't there, create it
		logging.info(f"Checking for 'Output\\{subfolder}\\'")
		if not os.path.exists(out_path):
			logging.info(f"'Output\\{subfolder}\\' does not exist, so it is being created")
			os.makedirs(out_path)
		
		# Save the images by looping over the list
		for image in enumerate(images):
			fname = f"{file_name}" + f".{imageFormat}"
			image.save(f'{out_path}\\{fname}', f"{imageFormat}")

	except Exception as err:
        # Log errors
		logging.error(err)

def findToConvert(in_folder):
	'''
	Searches through each subfolder in the "Input" folder 
	and passes each pdf file to convert()
	Args:
		in_foler: The Input folder, as defined in the main block below (inputFolder var)
	Returns:
		N/A
	'''
	# Walk through all folders in the Input folder
	for foldername, subfolders, _ in os.walk(in_folder):
		
		# Loop through each input subfolder
		for subfolder in subfolders:
			logging.info(f"Going through the input folder '{subfolder}'")
			# Create a list of files in each subfolder
			files = os.listdir(f"{foldername}\\{subfolder}")
			
			# Loop through each file
			for file in files:
				# and if the file is a pdf, call convert()
				if file.endswith('.pdf'):
					logging.info(f"Converting the file '{file}'")
					convert(inputFolder, subfolder, file)

# Main block
# Use conditional to preventing running from module
# and to run in CLI
if __name__ == '__main__':
	logging.info(f"Pdf2image program is STARTING...")
	findToConvert(inputFolder)
	logging.info(f"Pdf2image program has SUCCESSFULLY RAN")
	




					
          





#   file = "As-Builts 1\\4B 1st Flr Color.pdf"
  # convert("C:\\Users\\User\\Desktop\\GIS\\PDF to Image\\As-Builts 1\\4A 1st Flr B&W.pdf")
  # convert(file)