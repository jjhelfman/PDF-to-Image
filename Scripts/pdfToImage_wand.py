# Import modules
from wand.image import Image
import os
import re
import logging

# Change CWD to Project's "PDF to Image" folder
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

logging.info(f"The current working directory is {os.getcwd()}")


def convert(subfolder, filepdf):
    """
    Converts pdf files to jpg files
    Args:
            subfolder: The subfolder string from the findToConvert() function
            filepdf: The pdf file string from the findToConvert() function
    Returns:
            N/A
    """
    # Try to convert pdf to image,
    # other wise handle the error
    try:
        # Create Image object
        with Image(filename=f"Input\\{subfolder}\\{filepdf}", resolution=750) as img:
            # Define the output path
            out_path = f"Output\\{subfolder}\\"
            # Define the file name, without extension
            file_name = re.sub(".pdf$", "", filepdf)
            # Define compression quality
            img.compression_quality = 100

            # Log the number of pages in the pdf
            logging.info(f"'{filepdf}' contains {len(img.sequence)} page(s)")
            # If the directory isn't there, create it
            logging.info(f"Checking for 'Output\\{subfolder}\\'")
            if not os.path.exists(out_path):
                logging.info(
                    f"'Output\\{subfolder}\\' does not exist, it's being created"
                )
                os.makedirs(out_path)

            # Save the image
            logging.info(f"Saving 'Output\\{subfolder}\\{file_name}.jpg'")
            img.save(filename=f"{out_path}{file_name}.jpg")

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
                        convert(subfolder, file)
    except Exception as err:
        # Log errors
        logging.error(err)


# Main block
# Use conditional to preventing running from module
# and to run in CLI
if __name__ == "__main__":
    logging.info("Wand program is STARTING...")

    inputFolder = "Input\\"
    findToConvert(inputFolder)

    logging.info("Wand program has RAN")
