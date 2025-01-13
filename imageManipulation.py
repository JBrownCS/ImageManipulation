'''
An employee sent new images to use on a website, but there are a few issues:

1. The images are 90 degrees counter-clockwise
2. The images are too large, and should be resized to 128x128
3. The images are in the wrong format and should be .jpeg files

This program corrects those issues, and places the updated images in a new folder
'''


import os
import sys
from PIL import Image



#Find current image directory and create new directory for updated images
#If this directory already exists, skip creation process
current_img_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '/images'
new_img_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '/new_images'

if not os.path.exists(new_img_dir):
    os.makedirs(new_img_dir)


#Loop through directory and update images
for imgfile in os.listdir(current_img_dir):

    #Find image path and image name
    curr_img_path = os.path.join(current_img_dir, imgfile)
    curr_img_name = os.path.basename(imgfile)[:-5]
    
    #It is an image if the image name starts with a letter, otherwise skip that file
    if curr_img_name[0] == ".":
        continue
    else:
        #Open the image and format it correctly
        with Image.open(curr_img_path) as image:
            #Convert image to RGB so it can be formatted to JPG, then rotate and resize
            new_img = image.convert('RGB')
            new_img = new_img.rotate(270).resize((128,128))
            new_img_path = new_img_dir + "/new_" + curr_img_name
            

            new_img.save(new_img_path, 'JPEG')
            print(new_img.format, new_img.size)
        
