from flask import Flask, render_template, request
import os
import time  # Pour générer un nom unique si aucun n’est fourni
from motifs import dessiner

application = Flask(__name__)

IMAGE_FOLDER = os.path.join('static', 'images')
os.makedirs(IMAGE_FOLDER, exist_ok=True)

@application.route('/', methods=['GET', 'POST'])
def index():
    error = None
    image_file = None

    if request.method == 'POST':
        type_motif = request.form.get('type_motif')
        couleur = request.form.get('couleur', 'black')
        nom_fichier = request.form.get('nom_fichier', '').strip()

        # Génère un nom de fichier unique si aucun n'est fourni
        if not nom_fichier:
            nom_fichier = f"{type_motif}_{int(time.time())}"

        filename = f"{nom_fichier}.png"
        fichier = os.path.join(IMAGE_FOLDER, filename)

        try:
            if type_motif in ['polygone', 'spirale']:
                cotes = int(request.form.get('cotes'))
                taille = int(request.form.get('taille'))
                repetitions = int(request.form.get('repetitions'))
                angle = int(request.form.get('angle'))

                dessiner(type_motif, cotes, taille, repetitions, angle, couleur, fichier)
                image_file = filename

            elif type_motif == 'fractale':
                taille = int(request.form.get('taille_fractale'))
                niveau = int(request.form.get('niveau'))

                dessiner(type_motif, 0, taille, niveau, 0, couleur, fichier)
                image_file = filename

            else:
                error = "Motif inconnu"

        except (ValueError, TypeError):
            error = "Erreur d'entrée"

    return render_template('index.html', error=error, image_file=image_file)

if __name__ == '__main__':
    application.run(debug=True)
