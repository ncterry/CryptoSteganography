

#=====================================
from Functions import *
from tkinter import *
import tkinter as tk
from tkinter import ttk

XL_FONT  = ("Verdana", 30)  # Base font that we want to use and will call
LARGE_FONT = ("Verdana", 18)  # Base font that we want to use and will call
NORM_FONT = ("Verdana", 12)  # Base font that we want to use and will call
SMALL_FONT = ("Verdana", 10)  # Base font that we want to use and will call


# This is our global list.
# While the program is running this will be used with our study data
global global_photoName
global_photoName = ""

global globalMain_Directory
globalMain_Directory = "/Users/nct/Dropbox/ComputerScience/PycharmProjects/CryptoSteganography"

# Set photo directory address in StudyPage, so the PhotoPage knows what to open
# We set it to a stock photo initially, so the PhotoPage can open up front.
global globalOriginalPhoto_Directory
globalOriginalPhoto_Directory = "/Users/nct/Dropbox/ComputerScience/PycharmProjects/CryptoSteganography/OriginalPhotos/"

# Set the photo directory for encrypted photos
global globalEncryptedPhoto_Directory
globalEncryptedPhoto_Directory = "/Users/nct/Dropbox/ComputerScience/PycharmProjects/CryptoSteganography/StegoPhotos/"





#from subFunctions import open_image, save_image, create_image, get_pixel
#rom a_grayScale import convert_grayscale
#from aaaa_primaryColors import convert_primary
from tkinter import *
from Classes import Steganography

# Define the tkinter class that will open a program window.
app = Steganography()

# Main
if __name__ == "__main__":

  # This is looping the tkinter window
  app.mainloop()
  '''
  # Load Image (JPEG/JPG needs libjpeg to load)
  original = open_image('Apple_original.jpg')

  # Example Pixel Color
  print('Color: ' + str(get_pixel(original, 0, 0)))

  # Convert to Grayscale and save
  # Working
  new = convert_grayscale(original)
  save_image(new, 'Prinny_gray.png')


  # Convert to Primary and save
  new = convert_primary(original)
  save_image(new, 'Prinny_primary.png')
'''