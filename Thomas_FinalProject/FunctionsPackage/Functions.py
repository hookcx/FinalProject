from PIL import Image, ImageFilter, ImageDraw, ImageFont   #Image manipulation
import os, sys
import requests
from io import BytesIO

def load_image(filename) :
    '''
    Load an image file from disk
    @param filename The file to load
    @return the image object
    '''  
    try:   
        myimage = Image.open(filename)
        myimage.load()       
    except:    #Catching ALL exceptions; might not be a good idea
        #pass  #Placeholder that allows program to be syntactically correct; just skips over it
        myimage = None   #None is a placeholder for a null value
    return myimage
        

def save_image(imageObject, outfilename) :
    '''
    Save an image to disk
    @param imageObject The Image to save
    @param outfilename The target file
    @return None on failure, -1 on success (This is just an arbitrary success return value)
    '''
    try:
        imageObject.save(outfilename)
    except:
        #pass  #Eating the exception; scary because no one knows there's a problem 
        return None  #None could mean we failed 
    return -1


#Now, code will only run print statement below if this is the entry point; main.py is the REAL entry point not functions.py
if __name__ == "__main__":
    print("I am in functions.py and I am NOT in a function")