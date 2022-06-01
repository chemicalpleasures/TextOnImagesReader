# import the modules
import os
from os import listdir

# get the path/directory
folder_dir = "SKY2339"
for images in os.listdir(folder_dir):
    if (images.endswith(".jpg")):
        print(images)