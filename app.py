from flask import Flask, render_template, request
import os
from multiprocessing import Process

from motifs import dessiner

application = Flask(__name__)

IMAGE_FOLDER = os.path.join('static', 'images') 
os.makedirs(IMAGE_FOLDER, exist_ok=True)

def dessiner_process(type, cotes, taille, repetitions, angle, couleur, fichier):
    from motifs import dessiner
    dessiner(type, cotes, taille, repetitions, angle, couleur, fichier)

def lancer_dessin(type, cotes, taille, repetitions, angle, couleur, fichier):
    p = Process(target=dessiner_process, args=(type, cotes, taille, repetitions, angle, couleur, fichier))
    p.start()
    p.join()

@application.route('/', methods=['GET', 'POST'])
def index():
    error = None
    image_file = None

    if request.method == 'POST':
        type_motif = request.form.get('type_motif')
        couleur = request.form.get('couleur', 'black')

        try:
            if type_motif in ['polygone', 'spirale']:
                cotes = int(request.form.get('cotes'))
                taille = int(request.form.get('taille'))
                repetitions = int(request.form.get('repetitions'))
                angle = int(request.form.get('angle'))

                filename = f"{type_motif}.png"
                fichier = os.path.join(IMAGE_FOLDER, filename)
                lancer_dessin(type_motif, cotes, taille, repetitions, angle, couleur, fichier)
                image_file = filename

            elif type_motif == 'fractale':
                taille = int(request.form.get('taille_fractale'))
                niveau = int(request.form.get('niveau'))
                filename = "fractale.png"
                fichier = os.path.join(IMAGE_FOLDER, filename)
                lancer_dessin(type_motif, 0, taille, niveau, 0, couleur, fichier)
                image_file = filename

            else:
                error = "Motif inconnu"

        except (ValueError, TypeError):
            error = "Erreur d'entrée"

    return render_template('index.html', error=error, image_file=image_file)

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    application.run(debug=True)