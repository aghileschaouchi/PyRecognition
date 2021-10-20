# -*- coding:utf-8 -*-
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
from projet import*

#fonction appeler apres le premier clique
def rect1(event):
    #on capture les coordonées de l'endroit cliquer
    global x1, y1
    x1 = event.x
    y1 = event.y

#fonction appeler apres le relachement du clique
def rect2(event):
    global x2, y2, cadre_top, pil_image, tk_im2, cadre, x1, y1,id
    x2 = event.x
    y2 = event.y
    #en relachant le clique on capture les deuxiempe coorodnnées
    cadre_top.focus_set()
    #on affiche le rectangle selectionner dans la fenetre principale
    cropped = pil_image.crop((x1,y1,x2,y2))
    tk_im2 = ImageTk.PhotoImage(cropped)
    #on appel la fonction de reconnaissance et on affiche le nom de l'image la plus proche
    name = plus_proche_exemple(cropped)

    print(name)

    cadre.create_image(x2, y2, image=tk_im2)

def open_file():
    global id, tk_image, fen, cadre, x1, x2, y1 , y2, pil_image, cadre_top
    my_file = askopenfilename()
    top = Toplevel(master=fen, background='green')
    cadre_top = Canvas(top, width=300, height=300)
    #on ouvre l'image selectionner
    pil_image = Image.open(my_file).convert('L')

    tk_image =  ImageTk.PhotoImage(pil_image)
    id =cadre_top.create_image(0, 0, anchor=NW, image=tk_image)
    x, y = pil_image.size
    cadre_top.config(width=x, height=y)

    cadre_top.focus_set()
    cadre_top.bind("<Button-1>", rect1)
    cadre_top.bind("<ButtonRelease>", rect2)
    cadre_top.pack()

def make_zoning():
    global id, tk_image, fen, cadre, x1, x2, y1, y2, pil_image, cadre_top
    zoning_x(pil_image, 4)

def make_zoning_10():
    global id, tk_image, fen, cadre, x1, x2, y1, y2, pil_image, cadre_top
    zoning_x(pil_image, 10)

def make_zoning_50():
    global id, tk_image, fen, cadre, x1, x2, y1, y2, pil_image, cadre_top
    zoning_x(pil_image, 50)

def fun() :
    global id
    cadre.delete(id)


#Fonction qui affiche les coordonees de la souris sur la fenetre
def affiche_coord(event):
    global cadre,id,label
    touche = event.keysym
    new_text = "%s , %s" % (event.x, event.y)
    label.config(text=new_text)

if __name__ == "__main__":
    fen = Tk()

    mon_menu = Menu(fen)
    fen.config(menu=mon_menu)

    cadre = Canvas(fen, width=300, height=300)
    #en cliquant on affiche un carre noir
    cadre.focus_set()
    cadre.bind("<Motion>", affiche_coord)
    cadre.pack()

    # label pour afficher les coordonees de la souris sur le Canvas
    label = Label(fen, text="0 , 0", bg="green")
    label.pack()

    #menu simple
    mon_menu.add_command(label="Ouvrir", command=open_file)
    mon_menu.add_command(label="Zoning 4x4", command=make_zoning)
    mon_menu.add_command(label="Zoning 10x10", command=make_zoning_10)
    mon_menu.add_command(label="Zoning 50x50", command=make_zoning_50)
    mon_menu.add_command(label="Quitter", command=fen.quit)


    #bouton de suppression
    b_sup = Button(fen, text="Delete", command=fun)

    b_sup.pack()

    fen.mainloop()
