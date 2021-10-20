# -*- coding:utf-8 -*-
#feuille 2 manipulattion d'images PIL ex2
from tkinter import *
from PIL import Image
from PIL import ImageTk
import os, sys
from traitement_image import *
from interface import *

#pour les tests : fonction qui affiche les pixels d'une image

def print_image(image):
    width, height = image.size

    for i in range(0,width):
        print("\n")
        for j in range(0,height):
            print(image.getpixel((i,j)))

#fonction qui alloue un vecteur

def creer_tableau_1D(l, val):
    t1 = [val]*l
    return t1

#fonction qui alloue une matrice

def creer_tableau_2D(h, l, val):
    t = creer_tableau_1D(h, None)
    for i in range(0, h):
        t[i] = creer_tableau_1D(l, val)
    return t

#fonction qui calcule le carrer de la distance euclidienne entre deux points
def carre_dis_eucl(t1, t2):
    dist = 0
    for i in range(0, len(t1)):
        dist = dist + (t1[i]-t2[i]) * (t1[i]-t2[i])
    return dist

def profil_horizontal(image):
    width, height = image.size

    t = creer_tableau_1D(width, 0)

    for i in range(0, width):
        for j in range(0, height):
            t[i] = t[i] + image.getpixel((i, j))
            #print(image.getpixel((i,j)))
    return t

def profil_vertical(image):
    width, height = image.size

    t = creer_tableau_1D(height, 0)

    for i in range(0, width):
        for j in range(0, height):
            t[j] = t[j] + image.getpixel((i, j))
    return t

def calculer_caracteristiques(image):
    width, height = image.size
    vec = creer_tableau_1D(width+height, 0)

    t_horizontal = profil_horizontal(image)
    t_vertical = profil_vertical(image)
    vec = t_horizontal + t_vertical
    return vec

def redimensionner(im_source, image_base):
    width_base, height_base = image_base.size
    return im_source.resize((width_base, height_base),Image.NEAREST)

def plus_proche_exemple(im_source):
    DIR = "/net/cremi/achaouchi/espaces/travail/UNIX/python/bases/"
    #tableau contenant tous les fichiers base
    files = os.listdir(DIR)

    #ouvrir la premiere image dans les bases"
    current_im = Image.open(DIR+files[0]).convert('L')

    # le decouper cause des problemes dans les resultats
    im_source = decouper(im_source)

    im_source = augmenter_contraste(im_source)

    im_source = redimensionner(im_source, current_im)

    #vecteur caracteristique de l'image source
    carac_source = calculer_caracteristiques(im_source)

    name = files[0]
    #carac de la premiere image
    carac = calculer_caracteristiques(current_im)
    #distance entre image source et premiere image dans les bases
    my_dist = carre_dis_eucl(carac_source, carac)

    #parcourir tous les fichiers bases
    for file in files:
        #ouvrir le fichier en cours
        current_im = Image.open(DIR+file).convert('L')

        #calculer vecteur caracteristique de l'image en cours
        carac = calculer_caracteristiques(current_im)

        #si distance euclidienne entre image en cours et image source < a la derniere distance calculer
        if(carre_dis_eucl(carac, carac_source) < my_dist):
            my_dist = carre_dis_eucl(carac, carac_source)
            name = file

    return name

def zoning(im_source):
    width, height = im_source.size
    x1 = -4
    y1 = -4
    x2 = 0
    y2 = 0
    for i in range(0,height - height%4, 4):
        x1 += 4
        x2 += 4
        for j in range(0, width - width%4, 4):
            y1 += 4
            y2 += 4
            cropped_now = im_source.crop((x1, y1, x2, y2))
            plus_proche = plus_proche_exemple(cropped_now)
            print ("Le plus proche zone (x1 :",x1 ,") (y1 : ",y1,") (x2 : ",x2,") (y2 : ",y2,") : ", plus_proche)

def zoning_x(im_source, x):
    width, height = im_source.size
    x1 = -x
    y1 = -x
    x2 = 0
    y2 = 0
    for i in range(0,height - height%x, x):
        x1 += x
        x2 += x
        for j in range(0, width - width%x, x):
            y1 += x
            y2 += x
            cropped_now = im_source.crop((x1, y1, x2, y2))
            #cropped_now.show()
            plus_proche = plus_proche_exemple(cropped_now)
            print ("Le plus proche zone avec zoning ",x,"X",x," (x1 :",x1 ,") (y1 : ",y1,") (x2 : ",x2,") (y2 : ",y2,") : ", plus_proche)


if __name__ == "__main__":

    #test sur les fonctions
    #pil_image = Image.open("my_test.jpg").convert('L')
    pil_image = Image.new("L", (3, 3))
    lar, haut = pil_image.size
    i = 1
    for x in range(0, 3):
        for y in range(0, 3):
            pil_image.putpixel((x, y), i)
            i += 1

    #test 1 : distance euclidienne

    t1 = creer_tableau_1D(3, 2)
    t2 = creer_tableau_1D(3, 4)
    dist_eucl = carre_dis_eucl(t1, t2)
    print("eucl : ",dist_eucl)

    #test 2 : profil horizontal
    t_horizontal = profil_horizontal(pil_image)
    print("horizontal : ",t_horizontal)

    #test 3 : profil vertical
    t_vertical = profil_vertical(pil_image)
    print("vertical : ",t_vertical)

    #test 4 : caracteristiques
    carac = calculer_caracteristiques(pil_image)
    print("carac : ",carac)

    #test 5 : plus proche exemple
    pil_image = Image.open("1.tif").convert('L')
    name = plus_proche_exemple(pil_image)
    print("image plus proche : ", name)

    #test 6 : zoning
    """""
    DIR = "/net/cremi/achaouchi/espaces/travail/UNIX/python/projet/"
    im_source = Image.open(DIR+"UMBB_logo.jpg").convert('L')
    zoning_x(im_source,4)
    """""