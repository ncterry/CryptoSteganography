import tkinter as tk
from tkinter import ttk
from matplotlib import style
from main import *
from PIL import Image
# Imported PIL Library from PIL import Image
# ==================================================
# ==================================================
# ==================================================
# Open an Image - getPixel.py
def open_image(path, name):

    newImage = Image.open(path + name)
    return newImage



# ==================================================
# ==================================================
# ==================================================
# Save Image - getPixel.py
def save_image(image, path):
    image.save(path, 'png')


# ==================================================
# ==================================================
# ==================================================
# Create a new image with the given size - getPixel.py
def create_image(i, j):
    image = Image.new("RGB", (i, j), "white")
    return image

# ==================================================
# ==================================================
# ==================================================
def image_RGBconvert(img):
    img = img.convert('RGB')
    # We want to count how many pixels are not white, black, or almost white
    workingPXLs = 0
    # =============================================================
    # =============================================================
    # =============================================================

    # Print out simple properties of the image
    # There are many
    print("img.size = \t", img.size)  # Current Photo = (480, 640)
    print("img.format = \t", img.format)  # Current Photo = JPEG
    return img

# ==================================================
# ==================================================
# ==================================================
def print_pixel(x, y, img):

    #   The most common pixel format is the byte image, where this number is stored as an 8-bit integer
    #       giving a range of possible values from 0 to 255. Typically zero is taken to be black, and 255
    #       is taken to be white. Values in between make up the different shades of gray.
    #   A white pixel  = (255, 255, 255)
    import os, sys
    pix = img.load()
    print("Function print_pixel(x, y, img) = "
          "\n\tpixel[" + str(x) + ", " + str(y) + "] = \t", pix[x,y])
# ==================================================
# ==================================================
# ==================================================

# Get the pixel from the given image - getPixel.py
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
        return None
    # Get Pixel - getPixel.py
    pixel = image.getpixel((i, j))
    return pixel


# ==================================================
# ==================================================
# ==================================================
# Create a Grayscale version of the image - getPixel.py
def convert_grayscale(image):
    # Get size
    width, height = image.size
# ==================================================
# ==================================================


# ==================================================
# ==================================================
# ==================================================
