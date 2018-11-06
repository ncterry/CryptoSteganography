#   Old version was PIL
#   Developers kept it as PIL instead of changing it to Pillow
#   Pycharm/Preference/(select the Project)/ProjectInterpreter
#   Click +
#   Search Pillow (if you have it installed on your computer)
#   Import Pillow to project
#   Now we can incorporate it into our project with:
from PIL import *
#   We are using python3.7
#   Making a basic image
#   Make sure to bring the actual image into the project folder.
#       Though you could open via a directory.
#   Note 'img' is our simple made-up title. Not mandatory for an image

# =====================================
from tkinter import *
import tkinter as tk
from tkinter import ttk
from initialWorkingReduction import *
from Functions import *
from embeddSimpleMessage import *

XL_FONT     = ("Verdana", 30)  # Base font that we want to use and will call
LARGE_FONT  = ("Verdana", 18)  # Base font that we want to use and will call
NORM_FONT   = ("Verdana", 12)  # Base font that we want to use and will call
SMALL_FONT  = ("Verdana", 10)  # Base font that we want to use and will call




# Main
if __name__ == "__main__":


    '''The file initialWorkingReduction takes the fox.jpg file,
    and reduces every working pixel by 25%
    
    This return value here is what the change does, and returns.
    That is also saved.'''
    #img = initialWorking_pixelReduction()
    #img.show()




    img2 = embeddSimpleMessage()
    print("make it here???")
    img2.show()



            # ===============if RGB - end=================================
        # =============for x - end============================================
    # =================for y - end============================================
                # ============================================================
                # NOTE - this is what is being printed to our file
                # Based on our if/or, it is only printed if the pixel is not White
                # We are moving from top to bottom, then from left to right in each row,
                #     ===========================
                #          x, y = (313, 200)
                #          R = 254	G = 254	B = 254
                #          ===========================
                #          x, y = (314, 200)
                #          R = 253	G = 253	B = 253
                #          ===========================
                #          x, y = (315, 200)
                #          R = 254	G = 254	B = 254
                #          ===========================
                #          x, y = (318, 200)
                #          R = 254	G = 254	B = 254
                #          ===========================
                #break # note - break is just here to have a result in our if statement
                # Since we are writing to file in the if statement, we don't need a break
    '''
    # =============================================================
    # =============================================================
    # =============================================================
    # =============================================================
    # =============================================================
    # =============================================================
    # DETAILS FOR WORKING WITH TXT FILES.==========================
    #       file = open("copy.txt", "w")
    #       file.write("Your text goes here")
    #       file.close()
    #       The default value is r and will fail if the file does not exist

    #       'r' open for reading (default)
    #       'w' open for writing, truncating the file first
    #       Other interesting options are

    #       'x' open for exclusive creation, failing if the file already exists
    #       'a' open for writing, appending to the end of the file if it exists
    # =============================================================
    # =============================================================
    # =============================================================


    # ============================================
    # ============================================
    # ============================================
    '''
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


