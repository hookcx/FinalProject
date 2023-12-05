# main.py
# Name: Kelly Roden, Cassidy Hook, Max Smith, Dylan Moore
# Email: rodenky@mail.uc.edu, hookcx@mail.uc.edu, smith6mx@mail.uc.edu, moore4dl@mail.uc.edu
# Assignment Title: Final
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: The culmination of this semester and its teachings
# Thomas Final Project

from PIL import Image, ImageFilter, ImageDraw, ImageFont 
import os, sys
import requests
from io import BytesIO
from FunctionsPackage.Functions import *
from DecryptLocationPackage.DecryptLocation import *
from MovieDecrypterPackage.MovieDecrypter import *
from cryptography.fernet import Fernet
import json

if __name__ == "__main__":
    
# Print the location  
    decrypt_location_data(index_list)
# Print the movie
    decrypter()
 
#RELATIVE Path - can exchange code and it will still work on different machines
    im = Image.open(r"..\ImageArchivePackage\ImageArchive\Avengers.jpg")   #File has to be relative to the entry point
    print(im.width, im.height, im.mode, im.format)  # Display some info about the image

# if it starts with '..' its relative, if its absolute is starts with 'C:'

    # Indenting to show code is part of above if statement
    my_image = load_image(r"..\ImageArchivePackage\ImageArchive\Avengers.jpg")
    my_image.show(my_image)
# Python is intuitive enough to open the Windows Photo Viewer
# We created a temporary image file by running thousands of lines of code using the .show
    

