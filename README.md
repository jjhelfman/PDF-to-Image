PDF to Image batch script
 
Python code was adapted from https://gist.github.com/jimmyromanticdevil/691e97ce22f7cd43d6a9d54305344587

Instructions:

1. To use this script, you need to replicate the following folder structure (by cloning this):

    PDF to Image
    ├── Scripts/
    |   └── pdfToImage_wand.py
    |
    ├── Input/
    |   ├── subfolder1 with pdfs
    |   ├── subfolder2 with pdfs
    |   └── ...
    |
    ├── Output/

2. Install the required dependencies/modules via pip install -r requirements.txt

3. After setting up your pdfs different named folders in the Input folder, run the batch script by double clicking the .bat file in Scripts folder

4. Adjust the Image() object's paramaters as needed to achieve desired effect (http://docs.wand-py.org/en/0.6.1/wand/image.html)