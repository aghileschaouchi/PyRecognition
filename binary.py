# -*- coding:utf-8 -*-
#feuille 2 manipulattion d'images PIL ex2
from tkinter import *
from PIL import Image
from PIL import ImageTk
import os, sys
from traitement_image import *
from interface import *
from projet import *
import math

def convert_from_bin_to_pgm():
    count = 0
    DIR = "/net/cremi/achaouchi/espaces/travail/UNIX/python/data/"
    files = os.listdir(DIR)
    i = 0
    j = 0
    x1 = -28
    y1 = -28
    x2 = 0
    y2 = 0
    x = 0
    y = 0
    first_file = open(DIR+files[0]).read()
    #combien ya d'octets dans les fichiers
    how_much = len(first_file)
    mat_size = math.sqrt(how_much)
    #on alloue une matrice de taille mat_size X mat_size
    mat = creer_tableau_2D(mat_size, mat_size, 0)

    #parcours de tous les fichiers
    for file in files:
        current_file = open(file, 'rb')
        #parcours du fichier courrant
        byte = current_file.read(1)
        while byte != "":
            #traitement
            mat[i][j] = ord(byte)
            j += 1
            byte = current_file.read(1)
            if(j == mat_size):
                i += 1
                j = 0


        for i in range(0, mat_size):
            x1 += 28
            x2 += 28
            for j in range(0, mat_size):
                y1 += 28
                y2 += 28

                pgm_name = "pgm_%d.pgm", count
                pgm_file = open(pgm_name, 'w')
                pgm_file.write("P5\n28 28\n255\n")
                count += 1

                for x in range(x1, y1):
                    for x in range(x2, y2):
                        pgm_file.write(mat[i][j])
                pgm_file.close()
        current_file.close()


    current_file.close()


if __name__ == "__main__":
    #test fonction qui transforme les fichiers bin en fichiers pgm
    convert_from_bin_to_pgm()