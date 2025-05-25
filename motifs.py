import turtle
import os

def dessiner(nb_cotes,taille,repetitions,angle,couleur,nom_fichier="motif.png"):
    turtle.setup(width=800, height=800)
    turtle.bgcolor("white")
    turtle.speed(0) #vitesse de dessin au maximum
    turtle.hideturtle() #cache le stylo pour ne pas le voir pendant le dessin
    turtle.color(couleur)

    for _ in range(repetitions):
        for _ in range(nb_cotes):   #dessine un polygone régulier
            turtle.forward(taille)
            turtle.left(360 / nb_cotes)
        turtle.left(angle)