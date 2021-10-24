try:
    from PIL import Image
except ImportError:
    import Image
Image.MAX_IMAGE_PIXELS = None
import pytesseract
import os

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

with open("output.txt", "a") as ff:

	for image in os.listdir("."):
		if image.endswith('.png') and image != '_Original.png':
			img=Image.open(image)
	# Simple image to string
			ff.write(pytesseract.image_to_string(img, lang='ita'))
