import pywhatkit as pt

pt.image_to_ascii_art("Flower.avif")

#more method

import colorama
from ascii_magic import AsciiArt

my_art = AsciiArt.from_image('moon.jpg')     #enter path here
colorama.init()
my_art.to_terminal()