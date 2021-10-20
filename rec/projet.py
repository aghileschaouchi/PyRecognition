# -*- coding:utf-8 -*-
#feuille 2 manipulattion d'images PIL ex2
from tkinter import *
from PIL import Image
from PIL import ImageTk
import os, sys
from traitement_image import *
from interface import *

#import math
#pour les tests : fonction qui affiche les pixels d'une image

def print_image(image):
    width, height = image.size

    for i in range(0,width):
        print("\n")
        for j in range(0,height):
            print(image.getpixel((i,j)))

def creer_tableau_1D(l, val):
    t1 = [val]*l
    return t1

#fonction qui calcule le carrer de la distance euclidienne entre deux points
def carre_dis_eucl(t1, t2):
    dist = 0
    for i in range(0, len(t1)):
        dist = dist + t1[i]-t2[i] * t1[i]-t2[i]
    return dist

#wacrenier@labri.fr
#for while set shift unix : test programmation shell
def profil_horizontal(image):
    width, height = image.size

    t = creer_tableau_1D(height, 0)

    for i in range(0, width):
        for j in range(0, height):
            t[i] = t[i] + image.getpixel((i, j))
            #print(image.getpixel((i,j)))
    return t

def profil_vertical(image):
    width, height = image.size

    t = creer_tableau_1D(width, 0)

    for i in range(0, width):
        for j in range(0, height):
            t[j] = t[j] + image.getpixel((i, j))
    return t

def calculer_caracteristiques(image):
    #width, height = image.size
    #vec = creer_tableau_1D(width+height, 0)

    t_horizontal = profil_horizontal(image)
    t_vertical = profil_vertical(image)
    vec = t_horizontal + t_vertical
    return vec

def redimensionner(image_base):
    global im_source
    width_base, height_base = image_base.size
    im_source.resize((width_base, height_base),Image.NEAREST)



def plus_proche_exemple(nom_fichier_image):
    global im_source
    DIR = "/net/cremi/achaouchi/espaces/travail/UNIX/python/bases/"
    #il faut convertir les images de rgb en nivG
    # http://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
    #tableau contenant tous les fichiers base
    files = os.listdir(DIR)
    DIR1 = "/net/cremi/achaouchi/espaces/travail/UNIX/python/tif_pic/"
    #ouvrir l'image source
    im_source = Image.open(DIR1+nom_fichier_image).convert('L')
    #vecteur caracteristique de l'image source
    carac_source = calculer_caracteristiques(im_source)
    #ouvrir la premiere image dans les bases"
    current_im = Image.open(DIR+files[0]).convert('L')
    # redimensionner l'image source et augmenter son contraste et traiter ses marges
    decouper(im_source)
    augmenter_contraste(im_source)
    width_source, height_source = im_source.size
    print(width_source,height_source)
    redimensionner(current_im)
    width_source, height_source = im_source.size
    print(width_source, height_source)
    #fin de redimension
    name = files[0]
    #carac de la premiere image
    carac = calculer_caracteristiques(current_im)
    #distance entre image source et premiere image dans les bases
    my_dist = carre_dis_eucl(carac_source, carac)

    #parcourir tous les fichiers bases
    for file in files:
        print(file)
        #ouvrir le fichier en cours
        current_im = Image.open(DIR+file).convert('L')
        decouper(current_im)
        #calculer vecteur caracteristique de l'image en cours
        carac = calculer_caracteristiques(current_im)
        #dist = carre_dis_eucl(carac, my_carac)
        #si distance euclidienne entre image en cours et image source < a la derniere distance calculer
        if(carre_dis_eucl(carac, carac_source) < my_dist):
            my_dist = carre_dis_eucl(carac, carac_source)
            name = file

    return name

#fen = Tk()
#(largeur, hauteur)
"""
pil_image = Image.new("L", (3, 3))
lar, haut = pil_image.size
i = 1
for x in range(0, 3):
    for y in range(0, 3):
        pil_image.putpixel((x,y), i)
        i += 1
pil_image.save("my_image.tif")
"""
#test sur les fonctions
"""
#test 0 : affiche en pixel de l'image
print_image(pil_image)
#test 1 : distance euclidienne
'''
t1 = creer_tableau_1D(3, 2)
t2 = creer_tableau_1D(3, 4)
dist_eucl = carre_dis_eucl(t1, t2)
print("eucl : ",dist_eucl)
'''
#test 2 : profil horizontal
t_horizontal = profil_horizontal(pil_image)
print("horizontal : ",t_horizontal)

#test 3 : profil vertical
t_vertical = profil_vertical(pil_image)
print("vertical : ",t_vertical)

#test 4 : caracteristiques
carac = calculer_caracteristiques(pil_image)
print("carac : ",carac)
"""
#test 5 : plus proche exemple
name = plus_proche_exemple("1.tif")
print("image plus proche : ", name)

#pil_image.save("my_image_invers.pgm")
            #w.pack()
            #fen.mainloop()
