import pytesseract
from PIL import Image
from config import TESSERACT_CMD,UPLOAD_FOLDER,LOG_FOLDER
import os
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

def writeToFile():
    if not os.path.exists(LOG_FOLDER):
        os.mkdir(LOG_FOLDER)
    for file in os.listdir(UPLOAD_FOLDER):
        with open(LOG_FOLDER+'/output.txt',"a+") as f:
            f.write(pytesseract.image_to_string(Image.open(os.path.join(UPLOAD_FOLDER,file))))
        f.close()
