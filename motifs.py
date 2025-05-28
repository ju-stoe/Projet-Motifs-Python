import turtle
import os
from PIL import Image   #importe Pillow pour convertir l'image .eps en png

def enregistrement(fichier_png, fichier_eps="motif.eps"):

    canvas = turtle.getcanvas() #création de la surface de dessin
    canvas.postscript(file=fichier_eps) #enregistre le dessin en format eps(vectoriel)    

    img = Image.open(fichier_eps)
    img.save(fichier_png, 'png')

    turtle.clearscreen()    #nettoie la fenêtre

def dessiner(type, cotes, taille, repetitions, angle, couleur, fichier="dessin.png"):
    if type == "rosace":
        polygone(cotes, taille, repetitions, angle, couleur, fichier)
    elif type == "spirale":
        spirale(cotes, taille, repetitions, angle, couleur, fichier)
    elif type == "fractale":
        fractale(taille, repetitions, couleur, fichier)
    else:
        print("Ce motif n'est pas reconnu.", type)

def polygone(cotes,taille,repetitions,angle,couleur,fichier="dessin.png"):
    turtle.setup(width=800, height=800)
    turtle.bgcolor("white")
    turtle.speed(0) #vitesse de dessin au maximum
    turtle.hideturtle() #cache le stylo pour ne pas le voir pendant le dessin
    turtle.color(couleur)

    for i in range(repetitions):
        for i in range(cotes):   #dessine un polygone régulier
            turtle.forward(taille)
            turtle.left(360 / cotes)
        turtle.left(angle)  #tourne la tortue pour former un nouveau motif

    enregistrement(fichier)

def spirale(cotes, taille, repetitions, angle, couleur, fichier="dessin.png"):
    turtle.setup(width=800, height=800)
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(couleur)

    agrandissement = taille #augmente la taille a chaque répétitions

    for i in range(repetitions):
        for i in range(cotes):
            turtle.forward(taille)
            turtle.left(360 / cotes)
        turtle.left(angle)
        agrandissement += 5 

    enregistrement(fichier)

def fractale(longueur, niveau, couleur, fichier="dessin.png"):
    turtle.setup(width=800, height=800)
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(couleur)
    turtle.left(90)  # Orientation vers le haut
    turtle.up()
    turtle.goto(0, -300)  # Position de départ bas de la fenêtre
    turtle.down()

    def arbre(longueur, niveau):
        if niveau == 0:
            return
        turtle.forward(longueur)
        turtle.left(30)
        arbre(longueur * 0.6, niveau - 1)
        turtle.right(60)
        arbre(longueur * 0.6, niveau - 1)
        turtle.left(30)
        turtle.backward(longueur)

    arbre(longueur, niveau)

    enregistrement(fichier)

def main(): #interactions avec l'utilisateur
    print("Générateur de motif géométrique")
    type_motif = input("Type (rosace, spirale, fractale): ").strip().lower()
    if type_motif in ["rosace", "spirale"]:
        cotes = int(input("Nombre de côtés: "))
        taille = int(input("Taille: "))
        repetitions = int(input("Nombre de répétitions: "))
        angle = int(input("Angle entre chaque motif: "))
        couleur = input("Couleur: ").strip().lower()
        dessiner(type_motif, cotes, taille, repetitions, angle, couleur)
    elif type_motif == "fractale":
        taille = int(input("Longueur initiale: "))
        niveau = int(input("Niveau de récursion: "))
        couleur = input("Couleur: ").strip().lower()
        dessiner(type_motif, 0, taille, niveau, 0, couleur)  # cotes, repetitions, angle inutiles ici
    else:
        print("Motif non reconnu.")

    print("Motif généré et enregistré sous 'dessin.png'")

if __name__ == "__main__":  #test
    main()

os.remove("motif.eps")  #supprime le fichier eps
