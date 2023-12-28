import os
from PIL import Image
import image_slicer
Image.MAX_IMAGE_PIXELS = None

for number in [14,17]:
	image_slicer.main.slice('_Original.png', col=1, row=number)
	for file in os.listdir():
		if file.endswith('.png') and file.startswith('_') and file!='_Original.png':
			os.rename(file, str(number) + file)
