from flask import Flask, render_template, request, redirect, url_for #modules de Flask
import os
from motifs import dessiner 

app = Flask(__name__) #création de l'application

IMAGE_FOLDER = 'librairie/images' 
os.makedirs(IMAGE_FOLDER, exist_ok=True)    #endroit où sont stockées les images 

@app.route('/', methods=['GET', 'POST']) #définit la route de l'app(GET affiche la page, POST envoie le formulaire)
def index():
    error = None    #stock un message d"erreur si besoin
    image_file = None

    if request.method == 'POST': #récupération des données entrées par l'utilisateur
        type_motif = request.form.get('type_motif')
        couleur = request.form.get('couleur', 'black')

        try:
            if type_motif in['rosace', 'polygone']:
                cotes = int(request.form.get('cotes'))
                taille = int(request.form.get('taille'))
                repetitions = int(request.form.get('repetitions'))
                angle = int(request.form.get('angle'))
                
                filename = f"{type_motif}.png"
                fichier = os.path.join(IMAGE_FOLDER, filename)
                dessiner(type_motif, cotes, taille, repetitions, angle, couleur, fichier)
                image_file = filename
            
            elif type_motif == 'fractale':
                taille = int(request.form.get('taille'))
                niveau = int(request.form.get('niveau'))
                filename = "fractale.png"
                fichier = os.path.join(IMAGE_FOLDER, filename)
                dessiner(type_motif, 0, taille, niveau, 0, couleur, fichier)
                image_file = filename

            else:
                error = "Motif non reconnu."

        except (ValueError, TypeError):
            error = "Erreur d'entrée."


