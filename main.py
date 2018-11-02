


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