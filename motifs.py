import turtle
import os
from PIL import Image   #Pillow converti l'image eps en png

def sauvegarde(fichier_png, fichier_eps="motif.eps"):

    papier = turtle.getcanvas() 
    papier.postscript(file=fichier_eps) #enregistre le dessin en format eps(vectoriel)    

    image = Image.open(fichier_eps) #conversion du eps en png
    image.save(fichier_png, 'png')

    turtle.clearscreen()    #nettoie la fenêtre de dessin
    turtle.bye()

def dessiner(type, cotes, taille, repetitions, angle, couleur, fichier="dessin.png"):
    if type == "polygone":
        polygone(cotes, taille, repetitions, angle, couleur, fichier)
    elif type == "spirale":
        spirale(cotes, taille, repetitions, angle, couleur, fichier)
    elif type == "fractale":
        fractale(taille, repetitions, couleur, fichier)
    elif type == "cercle":
        cercle(taille, repetitions, angle, couleur, fichier)
    elif type == "coeur":
        coeur(taille, repetitions, angle, couleur, fichier)
    elif type == "etoile":
        etoile(taille, repetitions, angle, couleur, fichier)
    else:
        print("Motif inconnu", type)

def polygone(cotes,taille,repetitions,angle,couleur,fichier="dessin.png"):#dessin fonction polygone
    turtle.Screen()._root.withdraw()
    turtle.bgcolor("white")
    turtle.speed(0) #vitesse de dessin au maximum pour être plus rapide
    turtle.hideturtle() #cache la tortue pour ne pas voir le curseur
    turtle.color(couleur)

    for i in range(repetitions): 
        for i in range(cotes):   #dessiner un polygone régulier
            turtle.forward(taille)
            turtle.left(360 / cotes)
        turtle.left(angle)  #tourne la tortue pour former un nouveau motif décalé par rapport au précédent

    sauvegarde(fichier)

def spirale(cotes, taille, repetitions, angle, couleur, fichier="dessin.png"):#dessin fonction spirale
    turtle.Screen()._root.withdraw()
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(couleur)

    distance = 0
    increment = taille / max(repetitions, 1)  # éviter division par zéro

    for i in range(repetitions):
        distance += increment
        turtle.forward(distance)
        turtle.left(angle)

    sauvegarde(fichier)

def fractale(longueur, niveau, couleur, fichier="dessin.png"):#dessin fonction fractale
    turtle.Screen()._root.withdraw()
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(couleur)
    turtle.left(90)  # Orientation vers le haut
    turtle.up()
    turtle.goto(0, -300)  # Position de départ 
    turtle.down()

    def arbre(longueur, niveau):    #fonction dans fractale qui permet de dessiner les "branches" de l'arbre
        if niveau == 0:
            return  #si on a pas de niveau supérieur, la fonction s'arrete ici
        turtle.forward(longueur)
        turtle.left(30)
        arbre(longueur * 0.6, niveau - 1)
        turtle.right(60)
        arbre(longueur * 0.6, niveau - 1)
        turtle.left(30)
        turtle.backward(longueur)

    arbre(longueur, niveau)

    sauvegarde(fichier)

def cercle(rayon, repetitions, angle, couleur, fichier="dessin.png"): #fonction dessin cercle, on remplace cotes par rayon
    turtle.Screen()._root.withdraw()
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(couleur)

    for i in range(repetitions):
        turtle.circle(rayon)
        turtle.left(angle)

    sauvegarde(fichier)

def coeur(taille, repetitions, angle, couleur, fichier="dessin.png"): #fonction dessin coeur
    turtle.Screen()._root.withdraw()
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(couleur)
    
    for i in range(repetitions):
        turtle.begin_fill()
        turtle.left(45)
        turtle.forward(taille)
        turtle.circle(taille / 2, 180)
        turtle.right(90)
        turtle.circle(taille / 2, 180)
        turtle.forward(taille)
        turtle.left(135)
        turtle.end_fill()
        turtle.left(angle)

    sauvegarde(fichier)

def etoile(taille, repetitions, angle, couleur, fichier="dessin.png"): #fonction dessin etoile
    turtle.Screen()._root.withdraw()
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(couleur)

    def dessine_etoile():
        for i in range(5):
            turtle.forward(taille)
            turtle.right(144)

    for i in range(repetitions):
        dessine_etoile()
        turtle.left(angle)

    sauvegarde(fichier)



    
    
