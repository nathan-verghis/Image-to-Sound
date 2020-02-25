"""This program is used to generate a database of sounds from images
By default, the sounds generated will always be 5 seconds long to preserve
uniqueness amongst images with the exact same pixels with different arrangements
To map the 2-d images to a 1-d axis to be translated to sound, the pixels will
be rearranged according to a pseudo-Hilbert's curve. A helper function will be
created to handle the processing of that. This program works for one picture at
a time."""


from hilbertcurve.hilbertcurve import HilbertCurve
from PIL import Image
# import ColourPermutations


image = Image.open('Colourful512.png', 'r')
pixel_list = list(image.getdata())
pixel_arr = [[(0, 0, 0) for x in range(512)] for y in range(512)]
pix_count = 0

for i in range(512):
    for j in range(512):
        pixel_arr[i][j] = pixel_list[pix_count]
        pix_count += 1


class Pixel:
    """A pixel is a single pixel of an image
    It has a frequency value which represents the specific colour of the image's
    pixel."""
    def __init__(self, colour):
        self.colour = colour

i = 0
j = 0
for pixel in pixel_list:
    pixel1 = Pixel(pixel_list[0])

p = 9
N = 2
hilbert_curve = HilbertCurve(p, N)
for coords in [[0, 0], [0, 1], [1, 1], [1, 0]]:
    dist = hilbert_curve.distance_from_coordinates(coords)
    print(f'distance(x={coords}) = {dist}')

print(pixel1.colour)
# 16,777,216 colours
# Frequencies from 2,388 - 18,388 Hz

freq = (pixel1.colour[0] * 1000000) + \
       (pixel1.colour[1] * 1000) + \
       (pixel1.colour[2])

# 256256256 must be = 18388 Hz
# 0 must be = 0 Hz

# freq can range from 0 - 16,843,008
