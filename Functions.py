import tkinter as tk
from tkinter import ttk
from matplotlib import style
style.use("ggplot")
XL_FONT  = ("Verdana", 30)  # Base font that we want to use and will call
LARGE_FONT = ("Verdana", 18)  # Base font that we want to use and will call
NORM_FONT = ("Verdana", 12)  # Base font that we want to use and will call
SMALL_FONT = ("Verdana", 10)  # Base font that we want to use and will call

# ==================================================
# ==================================================
#   Old version was PIL
#   Developers kept it as PIL instead of changing it to Pillow
#   Pycharm/Preference/(select the Project)/ProjectInterpreter
#   Click +
#   Search Pillow (if you have it installed on your computer)
#   Import Pillow to project
#   Now we can incorporate it into our project with:
from PIL import Image


# Imported PIL Library from PIL import Image

# Open an Image - getPixel.py
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image - getPixel.py
def save_image(image, path):
  image.save(path, 'png')


# Create a new image with the given size - getPixel.py
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image


# Get the pixel from the given image - getPixel.py
def get_pixel(image, i, j):
  # Inside image bounds?
  width, height = image.size
  if i > width or j > height:
    return None
  # Get Pixel - getPixel.py
  pixel = image.getpixel((i, j))
  return pixel

# Create a Grayscale version of the image - getPixel.py
def convert_grayscale(image):
  # Get size
  width, height = image.size
# ==================================================
# ==================================================
# ==================================================