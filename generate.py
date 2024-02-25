from PIL import Image
import json
from to_hex import rgb_to_hex
from copy import copy, deepcopy
from get_face import get_face
from generate_function import generate_function

# Define constants
PIXEL = 0.0625 # of a block
NORTH = (32, 0)
BOTTOM = (0, 16)
WEST = (16, 16)
TOP = (32, 16)
EAST = (48, 16)
SOUTH = (32, 32)
SIZE = 16

f = open("colour_list.json")
colour_dict = json.load(f)

#print(colour_dict)

print("Welcome to .png2Block :3\nPlease input file location")
png_location = input("PNG location: ")

img = Image.open(png_location)

#print(img)

pixels = list(img.getdata())
width, height = img.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

##for line in pixels:
##    print(line)
##    print("\n\n\n\n\n")

hex_pixels = copy(pixels)

for y, row in enumerate(pixels):
    for x, value in enumerate(row):
        hex_of_val = rgb_to_hex(value)
        hex_pixels[y][x] = hex_of_val
        ##print(value, hex_of_val)

block_dict = {
         "north": (get_face(hex_pixels,"north")),
         "bottom": (get_face(hex_pixels,"bottom")),
         "west": (get_face(hex_pixels,"west")),
         "top": (get_face(hex_pixels,"top")),
         "east": (get_face(hex_pixels,"east")),
         "south": (get_face(hex_pixels,"south"))
         }

#print(block_dict["south"])


tag = input("Please provide a tag to give each entity in the block (e.g., meow_block): ")

print(generate_function(block_dict, tag, colour_dict))

input("Enter to close")
