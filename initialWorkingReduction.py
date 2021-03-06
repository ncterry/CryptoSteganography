from main import *
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
from Functions import *
import globals
XL_FONT     = ("Verdana", 30)  # Base font that we want to use and will call
LARGE_FONT  = ("Verdana", 18)  # Base font that we want to use and will call
NORM_FONT   = ("Verdana", 12)  # Base font that we want to use and will call
SMALL_FONT  = ("Verdana", 10)  # Base font that we want to use and will call

def initialWorking_pixelReduction():
    # This is looping the tkinter window

    # ============================================
    # photo we want, need input from user later
    # ============================================
    # Send initial photo directoy + name of photo
    # Function returns photo
    img = open_image(globalOriginalPhoto_Directory, global_photoName)

    # ============================================
    # Display photo - not needed in the long term.
    # img.show()

    # ============================================
    # We are sending the image to be converted to RGB format
    convertedRGBimage = image_RGBconvert(img)

    # ============================================
    # Display a specific pixel (not needed, just for show)
    print_pixel(300, 400, convertedRGBimage)

    # ============================================
    #   Define the width and height
    width = img.size[0]
    print("\n\n\twidth = ", width)
    print("So there are ", width, " pixels from left to right.")
    height = img.size[1]
    print("\theight = ", height)
    print("So there are ", height, " pixels from top to bottom.")
    print("\nSo there are ", width * height, " pixels total in this image.")
    print("Color Pixels have the RBG sets, so we have ", width * height * 3), " bytes"
    print("We need 8-bits per char, and each RBG is 8-bits, so we get 1-bit from each RBG")
    print("So we have ", (width * height * 3), " bytes from pixles that are RBG sets. "
                                               "\n 1-bit from each, up to 8-bits for each char."
                                               "\n Divide total bytes by 8 to see how many characters we can fit in this image. "
                                               "\n RBG Pixels divided by 8 = ", (width * height * 3 / 8),
          "\n but remember this is all of the pixels, not just the color ones we will use.")

    # =============================================================
    file = open("originalPixels.txt", "w")  # Creating/opening a txt file, and allow it to be written
    #   We are starting a double for loop
    #   Row 1   --> pixel1, pixel2, pixel3.....
    #   Row 2   --> .......

    # Create new Image and a Pixel Map
    newImage = create_image(width, height)
    pixels = newImage.load()

    # =================for y - start============================================
    for y in range(0, height):  # each pixel has coordinates
        row = ""
        # =============for x - start============================================
        for x in range(0, width):

            # we take pixel x,y from the original image
            # Send that to function, and return the RBG details of that pixel
            pixel = get_pixel(img, x, y)
            R = pixel[0]
            G = pixel[1]
            B = pixel[2]
            # -----------

            # Convert the values to binary
            # Example:
            #       R = 163
            #       bin_R = 10100011
            bin_R = bin(R)
            bin_G = bin(G)
            bin_B = bin(B)

            # Note - binary conversion, then to string will give us 0b10101010
            #       Since we have a byte
            #       We will convert to string so we can remove byte next.
            bin_R2 = str(bin_R)
            bin_G2 = str(bin_G)
            bin_B2 = str(bin_B)

            # Cycle through to remove the b from the string.
            for char in bin_R2:
                bin_R3 = bin_R2.replace("b", "")
            for char in bin_G2:
                bin_G3 = bin_G2.replace("b", "")
            for char in bin_B2:
                bin_B3 = bin_B2.replace("b", "")

            # Note if the length is 9, then these were  given an extra 0 at the front
            # Remove the extra, meaningless 0
            if len(bin_R3) == 9:
                bin_R4 = bin_R3[1:]
            if len(bin_G3) == 9:
                bin_G4 = bin_G3[1:]
            if len(bin_B3) == 9:
                bin_B4 = bin_B3[1:]

            # We are in our for loops to cycle through each line of pixels one-by-one
            # If we hit any pixel that is not solid white, 255x255x255 then we will print the pixel details.

            # ===============if RGB - start=============================================
            # We do not want to change or acknowledge:
            #   White Pixels 255
            #   Black pixels 0
            #   Pixles 1 from White --> add 1 would make White
            if (R != 255 or G != 255 or B != 255) and \
                    (R != 254 or G != 254 or B != 254) and \
                    (R != 0 or G != 0 or B != 0):
                # Change the RBG values
                reduce = (R * 0.25) + (G * 0.25) + (B * 0.25)

                # Set Pixel in new image
                #   We care have taken all pixels (RBG) down to .25 of what they where.
                #   This is basically making the image look black and whte
                pixels[x, y] = (int(reduce), int(reduce), int(reduce))


                # This prints too many pixels for pycharm.
                #       The program works, but we cant see all the results here.
                #       There are just too many pixels to display in pycharm
                #       This is only the non-white pixels, and it is still to many to display in pycharm
                #       Currently I am using a simple fox image, so it will be extreme on large, detailed photos.

                # print("===========================")
                # print("x, y = (",x, ", ", y, ")")
                # print("R = ", R, "\t\tG = ", G, "\t\tB = ", B)
                # print("R = " + str(bin_R4) + "\tG = " + str(bin_G4) + "\tB = " + str(bin_B4))

                # Length is not needed after we removed the extra zero.
                #   Keeping it just for display
                # print("len R = " + str(len(bin_R4)))
                # print("len G = " + str(len(bin_G4)))
                # print("len B = " + str(len(bin_B4)) + "\n")
                global workingPXLs
                workingPXLs += 1
                print("workingPXLs = " + str(workingPXLs))

                # =============================================================
                # The print functions above work, but pycharm can display 300k pixel values.
                #       So we are going to write those to a txt file.
                #       We created/opened a txt file above, and allowed ourselves to write to it.
                #       Everything needs to be a single string.
                #       Include our standard strings
                #       Don't separate standard strings, and variable with a comma here, use a +
                #       We are 'adding' more parts to our single string that is being written to file.

                file.write("\n     ==========================="
                           "\n     x, y = (" + str(x) + ", " + str(y) + ")"
                                                                        "\n\t   R = " + str(R) + "\t\t\tG = " + str(
                    G) + "\t\t\tB = " + str(B) +
                           "\n\t   R = " + str(bin_R4) + "\t\tG = " + str(bin_G4) + "\tB = " + str(bin_B4))
    save_image(newImage, 'StegoPhotos/changed_image.png')

    return newImage