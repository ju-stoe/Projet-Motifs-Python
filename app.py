from flask import Flask, render_template, request
import os
from multiprocessing import Process

# création de l'application avec Flask
application = Flask(__name__)

# stockage des images
IMAGE_FOLDER = os.path.join('static', 'images')
os.makedirs(IMAGE_FOLDER, exist_ok=True)  # crée le dossier s'il n'existe pas

# fonction séparée pour dessiner
def dessine(type_motif, cotes, taille, repetitions, angle, couleur, chemin_fichier):
    from motifs import dessiner 
    dessiner(type_motif, cotes, taille, repetitions, angle, couleur, chemin_fichier)

# lance un processus pour dessiner sans bloquer l'application
def lancer_dessin(type_motif, cotes, taille, repetitions, angle, couleur, chemin_fichier):
    process = Process(
        target=dessine,
        args=(type_motif, cotes, taille, repetitions, angle, couleur, chemin_fichier)
    )
    process.start()
    process.join()  # attend la fin du dessin

@application.route('/', methods=['GET', 'POST'])
def index():
    error = None
    image_file = None

    if request.method == 'POST':
        # récupération des valeurs du formulaire
        type_motif = request.form.get('type_motif')
        couleur = request.form.get('couleur', 'black')

        # création du nom du fichier
        nom_brut = request.form.get('nom_fichier', '').strip()
        nom_base = nom_brut if nom_brut else type_motif
        nom_base = ''.join(c for c in nom_base if c.isalnum() or c in ('_', '-'))  

        # gérer les doublons
        counter = 1
        filename = f"{nom_base}.png"
        chemin_fichier = os.path.join(IMAGE_FOLDER, filename)
        while os.path.exists(chemin_fichier):
            filename = f"{nom_base}_{counter}.png"
            chemin_fichier = os.path.join(IMAGE_FOLDER, filename)
            counter += 1

        try:
            if type_motif == 'polygone':
                cotes = int(request.form.get('cotes'))
                taille = int(request.form.get('taille'))
                repetitions = int(request.form.get('repetitions'))
                angle = int(request.form.get('angle'))
                lancer_dessin(type_motif, cotes, taille, repetitions, angle, couleur, chemin_fichier)

            elif type_motif == 'spirale':
                cotes = 0  
                taille = int(request.form.get('taille_spirale'))
                repetitions = int(request.form.get('repetitions_spirale'))
                angle = int(request.form.get('angle_spirale'))
                lancer_dessin(type_motif, cotes, taille, repetitions, angle, couleur, chemin_fichier)

            elif type_motif in ['cercle', 'coeur', 'etoile']:
                cotes = 0 
                taille = int(request.form.get('taille_autres'))
                repetitions = int(request.form.get('repetitions_autres'))
                angle = int(request.form.get('angle_autres'))
                lancer_dessin(type_motif, cotes, taille, repetitions, angle, couleur, chemin_fichier)

            elif type_motif == 'fractale':
                taille = int(request.form.get('taille_fractale'))
                niveau = int(request.form.get('niveau'))
                lancer_dessin(type_motif, 0, taille, niveau, 0, couleur, chemin_fichier)
            else:
                error = "Motif inconnu"
                return render_template('index.html', error=error, image_file=None)

            image_file = filename

        except (ValueError, TypeError):
            error = "Erreur : veuillez remplir correctement tous les champs numériques."

    return render_template('index.html', error=error, image_file=image_file)

# lance l'application
if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()  
    application.run(debug=True)
