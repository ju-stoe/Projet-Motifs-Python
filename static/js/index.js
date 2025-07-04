// met à jour le formulaire en fonction du type de motif (change si fractale)
function updateForm() {
            const type = document.getElementById('type_motif').value;
            document.getElementById('params_polygone').style.display = 'none';
            document.getElementById('params_fractale').style.display = 'none';
            document.getElementById('params_spirale').style.display = 'none';
            document.getElementById('params_autres').style.display = 'none';

            if (type == 'polygone') {
                document.getElementById('params_polygone').style.display = 'block';
            } else if (type == 'spirale'){
                document.getElementById('params_spirale').style.display = 'block';
            } else if (type == 'fractale') {
                document.getElementById('params_fractale').style.display = 'block';
            } else if (['cercle','coeur','etoile'].includes(type)){
                document.getElementById('params_autres').style.display = 'block';
            }
        }

        window.onload = updateForm; // Appelle la fonction updateForm automatiquement au chargement de la page