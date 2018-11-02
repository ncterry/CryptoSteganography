from subFunctions import create_image, get_pixel


# Create a Grayscale version of the image
def convert_grayscale(image):
    # Get size
    width, height = image.size
    print("width = ", width)
    print("height = ", height)

    #image.show()

    # Create new Image and a Pixel Map
    new = create_image(width, height)
    pixels = new.load()

  # Transform to grayscale
    for i in range(width):
        for j in range(height):
            # Get Pixel
            pixel = get_pixel(image, i, j)

            # Get R, G, B values (This are int from 0 to 255)
            red =   pixel[0]
            green = pixel[1]
            blue =  pixel[2]

            # Transform to grayscale
            #gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)
            gray = (red * 0.999) + (green * 0.887) + (blue * 0.914)

            # Set Pixel in new image
            pixels[i, j] = (int(gray), int(gray), int(gray))

    new.show()
    # Return new image
    return new
