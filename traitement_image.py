# -*- coding:utf-8 -*-
# feuille 2 manipulattion d'images PIL ex2
from tkinter import *
from PIL import Image
from PIL import ImageTk
import os,sys

#fonction qui calcule le minimum d'une image en niveau de gris
def min_nvg(image):
    width, height = image.size
    min = image.getpixel((0, 0))
    for i in range(0, width):
        for j in range(0, height):
            pixel = image.getpixel((i, j))
            if (pixel < min):
                min = pixel
    return min

def max_nvg(image):
    width, height = image.size
    max = image.getpixel((0, 0))
    for i in range(0, width):
        for j in range(0, height):
            pixel = image.getpixel((i, j))
            if (pixel > max):
                max = pixel
    return max


def augmenter_contraste(im_source):
    width, height = im_source.size
    a = min_nvg(im_source)
    b = min_nvg(im_source)
    if (a != b):
        for i in range(0, width):
            for j in range(0, height):
                im_source.putpixel((i, j), im_source.getpixel((i, j)) - a * 256 / (b - a))
    return im_source


def parcours_vertical(image, direction):
    width, height = image.size
    if direction == "left":
        rang = range(0, width)
    else:
        rang = range(width - 1, -1, -1);

    for x in rang:
        for y in range(0, height):
            pixel = image.getpixel((x, y))
            if pixel < 200:
                return x;

    return 0;


def parcours_horizontal(image, direction):
    width, height = image.size
    if direction == "top":
        rang = range(0, height)
    else:
        rang = range(height - 1, -1, -1);

    for y in rang:
        for x in range(0, width):
            pixel = image.getpixel((x, y))
            if pixel < 200:
                return y;

    return 0;


def decouper(im_source):
    width, height = im_source.size
    top = -1
    bot = -1
    left = -1
    right = -1

    left = parcours_vertical(im_source, "left")
    right = parcours_vertical(im_source, "right")
    top = parcours_horizontal(im_source, "top")
    bot = parcours_horizontal(im_source, "bot")

    box = (left, top, right, bot)
    im_source = im_source.crop(box)
    return im_source


if __name__ == "__main__":
    """""
    #test 0: sur decouper
    pil_image = Image.open("my_test.jpg").convert('L')
    pil_image = decouper(pil_image)
    pil_image.show()
    """""
    """""
    # test 1: sur augmenter contraste
    pil_image = Image.open("my_test.jpg").convert('L')
    pil_image = augmenter_contraste(pil_image)
    pil_image.show()
    """""
