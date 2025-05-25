import turtle
import os

def dessiner(nb_cotes,taille,repetitions,angle,couleur,nom_fichier="motif.png"):
    turtle.setup(width=800, height=800)
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(couleur)