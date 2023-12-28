from PIL import Image

Image.MAX_IMAGE_PIXELS = None
import pytesseract
import os
from tqdm import tqdm

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r"tesseract"
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

with open("output.txt", "a") as ff:
    for image in tqdm(os.listdir(".")):
        if image.endswith(".bmp"):
            img = Image.open(image)
            # Simple image to string
            ff.write(pytesseract.image_to_string(img, lang="eng"))
