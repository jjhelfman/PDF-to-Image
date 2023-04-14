# Import modules
from pdf2image import convert_from_path
import os
import re
import logging
from PIL import (
    Image,
)  # Python Imaging Library

# Define vars/params
Image.MAX_IMAGE_PIXELS = None
# popplerPath = "C:\\Program Files\\poppler-0.68.0\\bin"
popplerPath = "C:\\Program Files\\poppler-21.11.0\\Library\\bin"
inputFolder = "Input"
imageFormat = "png"

# Change current working directory (CWD) to Project's "PDF to Image" folder
# Start from Scripts folder
parentFolder = os.path.dirname(os.path.abspath(__file__))
# Move up one folder from current Scripts folder
os.chdir(os.path.dirname(parentFolder))
# Configure log messages
logging.basicConfig(
    filename="Logs\\pypdf_to_image.log",
    level=logging.DEBUG,
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# Log the CWD
logging.info(f"The current working directory is {os.getcwd()}")


def convert(inputFolder, subfolder, filepdf):
    """
    Converts pdf files to jpg files
    Args:
            subfolder: The subfolder string from the findToConvert() function
            filepdf: The pdf file string from the findToConvert() function
    Returns:
            N/A
    """
    # Try to convert pdf to image,
    # otherwise, handle the error
    try:
        # Convert the pdf to a PNG image, at a resolution of 750
        # 750 res : ~ 6 sec per pg
        # Define the list of images from the path
        images = convert_from_path(
            pdf_path=f"{inputFolder}\\{subfolder}\\{filepdf}",
            dpi=750,
            fmt=imageFormat,
            poppler_path=popplerPath,
        )
        # Define the output path
        out_path = f"Output\\{subfolder}\\"
        # Define the file name, without extension
        file_name = re.sub(".pdf$", "", filepdf)

        # Log the number of pages in the pdf
        logging.info(f"'{file_name}' contains {len(images)} page(s)")
        # If the directory isn't there, create it
        logging.info(f"Checking for 'Output\\{subfolder}\\'")
        if not os.path.exists(out_path):
            logging.info(
                f"'Output\\{subfolder}\\' does not exist, it's being created"
            )
            os.makedirs(out_path)

        # Save the images by looping over the list
        for image in enumerate(images):
            fname = f"{file_name}" + f".{imageFormat}"
            # print(image)
            image[1].save(f"{out_path}\\{fname}", f"{imageFormat}")

    except Exception as err:
        # Log errors
        logging.error(err)


def findToConvert(in_folder):
    """
    Searches through each subfolder in the "Input" folder
    and passes each pdf file to convert()
    Args:
            in_folder: The Input folder, containing PDFs
    Returns:
            N/A
    """
    try:
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
                    if file.endswith(".pdf"):
                        logging.info(f"Converting the file '{file}'")
                        convert(inputFolder, subfolder, file)
    except Exception as err:
        # Log errors
        logging.error(err)


# Main block
# Use conditional to preventing running from module
# and to run in CLI
if __name__ == "__main__":
    logging.info("Pdf2image program is STARTING...")

    findToConvert(inputFolder)

    logging.info("Pdf2image program has RAN")
