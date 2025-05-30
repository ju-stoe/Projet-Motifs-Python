from flask import Flask, render_template, request, redirect, url_for
import os
from motifs import dessiner  # Ton module avec les fonctions turtle

application = Flask(__name__)

# Dossier où seront stockées les images générées
IMAGE_FOLDER = os.path.join('static', 'images')
os.makedirs(IMAGE_FOLDER, exist_ok=True)

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        error = None
        image_file = None
        type_motif = request.form.get('type_motif')
        couleur = request.form.get('couleur', 'black')

        try:
            if type_motif in ['polygone', 'spirale']:
                cotes = int(request.form.get('cotes'))
                taille = int(request.form.get('taille'))
                repetitions = int(request.form.get('repetitions'))
                angle = int(request.form.get('angle'))

                filename = f"{type_motif}.png"
                filepath = os.path.join(IMAGE_FOLDER, filename)
                dessiner(type_motif, cotes, taille, repetitions, angle, couleur, filepath)
                return render_template('index.html', image_file=filename, request=request)

            elif type_motif == 'fractale':
                taille = int(request.form.get('taille_fractale'))
                niveau = int(request.form.get('niveau'))

                filename = "fractale.png"
                filepath = os.path.join(IMAGE_FOLDER, filename)
                dessiner(type_motif, 0, taille, niveau, 0, couleur, filepath)
                return render_template('index.html', image_file=filename, request=request)


            else:
                error = "Motif inconnu"

        except (ValueError, TypeError):
            error = "Erreur d'entrée"

        # Si erreur, on affiche directement la page sans redirection
        return render_template('index.html', error=error)

    # Méthode GET – récupération du résultat via paramètre d’URL
    image_file = request.args.get('image_file')
    return render_template('index.html', image_file=image_file)

if __name__ == '__main__':
    application.run(debug=True)
