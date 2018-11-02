# CryptoSteganography
Encrypted messaged that is embedded in a photo using the Least Significant Bit in the RBG-pixels

Initially:
The program basics are run through the getPixel.py file. 
We open an original image (currently just set to the fox.jpg)
We convert to read the pixels in RBG format
Get the image details. Example for fox.jpg

    img.size =      (474, 675)          How many pixels (width, height)
    img.format =      None              Should read.....
    pix[x,y] =      (255, 255, 255)     Reading the pixel [3,4]


    width =  474    # So there are  474  pixels from left to right.
    height =  675   # So there are  675  pixels from top to bottom.

#### So there are  319950  pixels total in this image.
#### Color Pixels have the RBG sets, so we have  959850
#### We need 8-bits per char, and each RBG is 8-bits, so we get 1-bit from each RBG
#### So we have  959850  bytes from pixles that are RBG sets. 
#### 1-bit from each, up to 8-bits for each char.
#### Divide total bytes by 8 to see how many characters we can fit in this image. 
#### RBG Pixels divided by 8 =  119981.25 
#### but remember this is all of the pixels, not just the color ones we will use.
