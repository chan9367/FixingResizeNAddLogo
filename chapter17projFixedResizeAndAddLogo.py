#! python3
# chapter17projFixedResizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'D:\pythonSTUFF\catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
#logo image needed to be resized first
logoIm = logoIm.resize((50,50))
logoWidth, logoHeight = logoIm.size

os.makedirs('D:\pythonSTUFF\withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('D:\pythonSTUFF'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp')) \
       or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself

    im = Image.open('D:\pythonSTUFF\\'+filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))
        
    # Add logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    
    # Save changes.
    im.save(os.path.join('D:\pythonSTUFF\withLogo', filename))
