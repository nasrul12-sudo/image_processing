from math import cos, log, sin
from PIL import Image
import numpy as np
    
# Thresholding


def thresholding(input_image, color_depth, val):
    if color_depth != 25:
        input_image = input_image.convert('RGB')
        T = val
        output_image = Image.new(
            'RGB', (input_image.size[0], input_image.size[1]))
        pixels = output_image.load()

    for i in range(output_image.size[0]):
        for j in range(output_image.size[1]):
            r, g, b = input_image.getpixel((i, j))
            if r and g and b < T:
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)

    if color_depth == 1:
        output_image = output_image.convert("1")
    elif color_depth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image

#Negative


def negative(input_image, color_depth):
    if color_depth != 25:
        input_image = input_image.convert("RGB")
    input_pixels = input_image.load()
    output_image = Image.new("RGB", input_image.size)
    output_pixels = output_image.load()

    horizontal_size = output_image.size[0]
    vertical_size = output_image.size[1]

    for x in range(horizontal_size):
        for y in range(vertical_size):
            R = 255 - input_pixels[x, y][0]
            G = 255 - input_pixels[x, y][1]
            B = 255 - input_pixels[x, y][2]
            output_pixels[x, y] = (R, G, B)

    if color_depth == 1:
        output_image = output_image.convert("1")
    elif color_depth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image

#Brightness
def clipping(intensity):
    if intensity < 0:
        return 0
    if intensity > 255:
        return 255
    return intensity


def brightness(input_image, color_depth, enlightenment_value):
    if color_depth != 25:
        input_image = input_image.convert("RGB")
    input_pixels = input_image.load()

    output_image = Image.new("RGB", input_image.size)
    output_pixels = output_image.load()

    horizontal_size = output_image.size[0]
    vertical_size = output_image.size[1]

    for x in range(horizontal_size):
        for y in range(vertical_size):
            R = clipping(input_pixels[x, y][0] + enlightenment_value)
            G = clipping(input_pixels[x, y][1] + enlightenment_value)
            B = clipping(input_pixels[x, y][2] + enlightenment_value)
            output_pixels[x, y] = (R, G, B)

    if color_depth == 1:
        output_image = output_image.convert("1")
    elif color_depth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image


