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
    else:
        print("Motif inconnu", type)

def polygone(cotes,taille,repetitions,angle,couleur,fichier="dessin.png"):
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

def spirale(cotes, taille, repetitions, angle, couleur, fichier="dessin.png"):
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(couleur)

    distance = 0
    increment = taille / max(repetitions, 1)  # éviter division par zéro

    for _ in range(repetitions):
        distance += increment
        turtle.forward(distance)
        turtle.left(angle)

    sauvegarde(fichier)

def fractale(longueur, niveau, couleur, fichier="dessin.png"):
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

def cercle(rayon, repetitions, angle, couleur, fichier="dessin.png"):
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(couleur)

    for _ in range(repetitions):
        turtle.circle(rayon)
        turtle.left(angle)

    sauvegarde(fichier)

def main(): #interactions avec l'utilisateur
    print("Générateur de motifs géométriques")
    utilisateur = input("Entrez un type de motif(polygone, spirale, fractale): ").strip().lower()
    if utilisateur in ["polygone", "spirale"]:
        cotes = int(input("Entrez le nombre de côtés: "))
        taille = int(input("Entrez la taille de base: "))
        repetitions = int(input("Combien de répétitions?: "))
        angle = int(input("Quel angle entre chaque motif?: "))
        couleur = input("Entrez la couleur: ").strip().lower()
        dessiner(utilisateur, cotes, taille, repetitions, angle, couleur)
    elif utilisateur == "fractale":
        taille = int(input("Longueur initiale: "))
        niveau = int(input("Niveau de récursion: "))
        couleur = input("Couleur: ").strip().lower()
        dessiner(utilisateur, 0, taille, niveau, 0, couleur)  # cotes, repetitions et angle inutiles ici
    
    else:
        print("Motif inconnu, veuillez réessayer")

    print("Motif sauvegardé dans 'dessin.png'")

if __name__ == "__main__":
    if os.path.exists("motif.eps"):
        os.remove("motif.eps")
    main()
    