NeoMatrix.py - a class to manage a matrix of, well, neopixels

NeoMatrixDemo.py - the demonstration code

colorsys.py - blatant steal from the python 3.x libs, used by NeoMatrix.py


Note. Colors are always rgb tuples (r,g,b) where r,g and b range from 0 to 255 to
match the color scheme used by the NeoPixel library which this work is based on 

useage:-

# create the NeoMatrix
# Pin is  like , gor example, 4 which neoPixel uses in a call to machine.Pin(4)
# so you don't need to do that
# width and height will affect the amount of memory gobbled up (not investigated) 

import NeoMatrix
nm=NeoMatrix.neoMatrix(Pin,width,height)

# set all pixels to one color
nm.setAll((r,g,b))

# set a pixel at x,y to color (r,g,b)
nm.setPixel(x,y,(r,g,b))

# sets the matrix pixels to a brightness ranging 0 to 100%
# the human eye has a square law response
nm.setMatrixPerceivedBrightness(brightness)

# set the brightness based on the range 0-100
# NOTE 50% is not what the ey would see, use setMatrixPerceivedBrightness()
nm.setMatrixBrightnessPercent(brightness)

# set the brightness based on the range 0-255
nm.setMatrixBrightness(brightness)

# Similar to the above brightness settings we also have 
# with the same ranges as above
nm.setPixelPerceivedBrightness(x,y,brightness)
nm.setPixelBrightnessPercent(x,y,brightness)
nm.setPixelBrightness(x,y,brightness)

# clear the pixels to black
nm.clear()

# send the pixel array to the matrix
# until this is called the changes are not visible
nm.display()
