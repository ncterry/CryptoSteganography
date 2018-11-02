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

So there are  319950  pixels total in this image. <br/>
<br/>Color Pixels have the RBG sets, so we have  959850
<br/>We need 8-bits per char, and each RBG is 8-bits, so we get 1-bit from each RBG
<br/>So we have  959850  bytes from pixles that are RBG sets. 
<br/>1-bit from each, up to 8-bits for each char.
<br/>Divide total bytes by 8 to see how many characters we can fit in this image. 
<br/>RBG Pixels divided by 8 =  119981.25 
<br/>---but remember this is all of the pixels, not just the color ones we will use.

<br/><br/> We open up the text file, originalPixels.txt
<br/> We will be writing the details of the pixels from the original photo:
<br/><br/><br/>x, y = (317, 203)
<br/><br/><br/>R = 251            G = 251            B = 251
<br/><br/><br/>R = 11111011        G = 11111011    B = 11111011
