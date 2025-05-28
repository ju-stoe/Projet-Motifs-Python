import turtle
import os
from PIL import Image   #importe Pillow pour convertir l'image .eps en png

def enregistrement(fichier_png, fichier_eps="motif.eps"):

    canvas = turtle.getcanvas() #création de la surface de dessin
    canvas.postscript(file=fichier_eps) #enregistre le dessin en format eps(vectoriel)    

    img = Image.open(fichier_eps)
    img.save(fichier_png, 'png')

    turtle.clearscreen()    #nettoie la fenêtre
    os.remove(fichier_eps)  #supprime le fichier eps

def dessiner(type, cotes, taille, repetitions, angle, couleur, fichier="dessin.png"):
    if type == "rosace":
        rosace_polygonale(cotes, taille, repetitions, angle, couleur, fichier)
    elif type == "spirale":
        spirale_polygonale(cotes, taille, repetitions, angle, couleur, fichier)
    else:
        print("Ce motif n'est pas reconnu.", type)

def rosace_polygonale(cotes,taille,repetitions,angle,couleur,fichier="dessin.png"):
    turtle.setup(width=800, height=800)
    turtle.bgcolor("white")
    turtle.speed(0) #vitesse de dessin au maximum
    turtle.hideturtle() #cache le stylo pour ne pas le voir pendant le dessin
    turtle.color(couleur)

    for _ in range(repetitions):
        for _ in range(cotes):   #dessine un polygone régulier
            turtle.forward(taille)
            turtle.left(360 / cotes)
        turtle.left(angle)  #tourne la tortue pour former un nouveau motif

    enregistrement(fichier)

def spirale_polygonale(cotes, taille, repetitions, angle, couleur, fichier="dessin.png"):
    turtle.setup(width=800, height=800)
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(couleur)

    agrandissement = taille #augmente la taille a chaque répétitions

    for _ in range(repetitions):
        for _ in range(cotes):
            turtle.forward(taille)
            turtle.left(360 / cotes)
        turtle.left(angle)
        agrandissement += 5 

    enregistrement(fichier)
