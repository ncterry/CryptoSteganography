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
          "\n\tpixel[" + str(x) + ", " + str(y) + "] = \t", pix[x, y])


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
def getMessage():

    unsecuredMessage = input("What message do you want to encrypt?")
    return unsecuredMessage


# ==================================================
# ==================================================
# ==================================================
# remember this is the unencrypted message
def turnMessageIntoBinary(message):
    print("")
    '''
    This function works, but does not represent a char in 8 binary digits
    Ex. Space   = 100000
    Ex. A       = 1000001
    
    If we embed this, without 8 digits, we cannot distinguish
    
    '''
    #print("Initial message = ")
    #print(message)

    #binMessage = ' '.join(format(ord(x), 'b') for x in message)
    #print(binMessage)
    #print("Length of binMessage = ")
    #print(str(len(binMessage)))
    #return binMessage
    '''
    What message do you want to encrypt?    nate is nate
    Length of binMessage = 
    93
    
    Print binarty in main:
    1101110 1100001 1110100 1100101 100000 1101001 1110011 100000 1101110 1100001 1110100 1100101
    
    '''
# ==================================================
# ==================================================
# ==================================================
def convertBinarytoDisplay8digits(initialBin):
    '''
    This function turns each char into 8 binary digits
    But we have a char in binary, in an array:

    Nate is
    ['01001110', '01100001', '01110100', '01100101', '00100000', '01101001', '01110011']
    Length of xxx =
    7
    '''
    secondBin = [bin(ord(ch))[2:].zfill(8) for ch in initialBin]
    #print(secondBin)
    #print("Length of xxx = ")
    #print(str(len(secondBin)))
    return secondBin
    # ==================================================
# ==================================================
# ==================================================
def changeANDconvertR(R, bin_R4, lenPoundMessage_eightDigitBinary, eightDigitBinary_lengthPosition, binaryPosition):
    # ---------------------------
    print("\n\ninitial R =  " + str(R))
    print("initial bin_R4[7] = " + str(bin_R4[7]))
    print("bin_R4[7] type is: " + str(type(bin_R4[7])))
    print("lenPoundMessage_eightDigitBinary[eightDigitBinary_lengthPosition][binaryPosition] = " +
          str(lenPoundMessage_eightDigitBinary[eightDigitBinary_lengthPosition][binaryPosition]))
    # bin_R4 represents binary, but is a string ex."01010101"
    # Strings are immutable. It cannot be changed.
    # We need to create a list, based on the bin_R4
    # Change the last value in the bin_R4_list
    # Then we can re-create the bin_R4 string, from that list
    bin_R4_list = list(bin_R4)
    bin_R4_list[7] = str(lenPoundMessage_eightDigitBinary[eightDigitBinary_lengthPosition][binaryPosition])  # for R
    bin_R4 = ''.join(bin_R4_list)
    print("Post bin_R4[7] = " + str(bin_R4[7]))
    R = int(bin_R4, 2)
    print("Post R =  " + str(R))
    return R

# ==================================================
# ==================================================
# ==================================================
def changeANDconvertG(G, bin_G4, lenPoundMessage_eightDigitBinary, eightDigitBinary_lengthPosition, binaryPosition):
    print("\n\ninitial G =  " + str(G))
    print("initial bin_G4[7] = " + str(bin_G4[7]))
    print("bin_G4[7] type is: " + str(type(bin_G4[7])))
    print("lenPoundMessage_eightDigitBinary[eightDigitBinary_lengthPosition][binaryPosition] = " +
          str(lenPoundMessage_eightDigitBinary[eightDigitBinary_lengthPosition][binaryPosition]))
    bin_G4_list = list(bin_G4)
    bin_G4_list[7] = str(lenPoundMessage_eightDigitBinary[eightDigitBinary_lengthPosition][binaryPosition])  # for G
    bin_G4 = ''.join(bin_G4_list)
    print("Post bin_G4[7] = " + str(bin_G4[7]))
    G = int(bin_G4, 2)
    print("Post G =  " + str(G))
    return G
# ==================================================
# ==================================================
# ==================================================
def changeANDconvertB(B, bin_B4, lenPoundMessage_eightDigitBinary, eightDigitBinary_lengthPosition, binaryPosition):
    print("\n\ninitial B =  " + str(B))
    print("initial bin_B4[7] = " + str(bin_B4[7]))
    print("bin_B4[7] type is: " + str(type(bin_B4[7])))
    print("lenPoundMessage_eightDigitBinary[eightDigitBinary_lengthPosition][binaryPosition] = " +
          str(lenPoundMessage_eightDigitBinary[eightDigitBinary_lengthPosition][binaryPosition]))
    bin_B4_list = list(bin_B4)
    bin_B4_list[7] = str(
        lenPoundMessage_eightDigitBinary[eightDigitBinary_lengthPosition][binaryPosition])  # for B
    bin_B4 = ''.join(bin_B4_list)
    print("Post bin_B4[7] = " + str(bin_B4[7]))
    B = int(bin_B4, 2)
    print("Post B =  " + str(B))
    return B
# ==================================================
# ==================================================
# ==================================================
def symmetricEncryptMessage(message):
    # in Terminal:
    # pip3 install Cryptography --> success
    # installed Cryptography here for interpreter
    from cryptography.fernet import Fernet

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
    plain_text = cipher_suite.decrypt(cipher_text)
    #print("cipher_text = " + str(cipher_text))
    #print(plain_text)

# ==================================================
# ==================================================
from Crypto.Cipher import AES
# ==================================================
def pad(s):
    '''
        global key
        key = b'Sixteen byte key' # he made this global

        global message
        message = "this is my super secret message"

        from Crypto.Cipher import AES
        global cipher
        cipher = AES.new(key)
        '''
    # AES only takes 16's
    # This pads with '{' since AES only takes inputs that are divisible by 16.
    return s + ((16-len(s) % 16) * '{')
# ==================================================
# ==================================================
# ==================================================
def encrypt(plaintext):
    # from Terminal:    $ pip3 install pycrypto     --> success
    # place "pycrypto" through our interpreter
    '''
        global key
        key = b'Sixteen byte key' # he made this global

        global message
        message = "this is my super secret message"

        from Crypto.Cipher import AES
        global cipher
        cipher = AES.new(key)
        '''
    from globals import cipher
    return cipher.encrypt(pad(plaintext))

# ==================================================
# ==================================================
# ==================================================
def decrypt(ciphertext):
    '''
        global key
        key = b'Sixteen byte key' # he made this global

        global message
        message = "this is my super secret message"

        from Crypto.Cipher import AES
        global cipher
        cipher = AES.new(key)
        '''
    from globals import cipher
    dec = cipher.decrypt(ciphertext).decode('utf-8')
    leng = dec.count('{')
    return dec[:len(dec) - leng]

# ==================================================
# ==================================================
# ==================================================
def bytesTOstring(byteMessage):

    # utf-8 is used here because it is a very common encoding, but you
    # need to use the encoding your data is actually in.
    print("\n\ninitial byteMessage: ", str(byteMessage))

    #byteTOstring = byteMessage.decode("utf-8")
    #byteTOstring = byteMessage.decode("ascii")
    byteTOstring = byteMessage.decode("latin-1")


    print("byteTOstring post decode: ", byteTOstring)
    return bytesTOstring

# ==================================================
# ==================================================
# ==================================================
def stringTObinary(stringMessage):
    print("stringMessage: ", stringMessage)
    binaryMessage = convertBinarytoDisplay8digits(stringMessage)
    print("binaryMessage: ", str(binaryMessage))

    '''
    Nate is great
    ['01001110', '01100001', '01110100', '01100101', '00100000', '01101001', '01110011', '00100000', '01100111', '01110010', '01100101', '01100001', '01110100']
        Length of eightDigitBinary = 
        13
    '''

# ==================================================
# ==================================================
# ==================================================

# ==================================================
# ==================================================
# ==================================================

# ==================================================
# ==================================================
# ==================================================