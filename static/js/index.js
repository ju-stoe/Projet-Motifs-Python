function updateForm() {
            const type = document.getElementById('type_motif').value;
            document.getElementById('params_polygone_spirale').style.display = 'none';
            document.getElementById('params_fractale').style.display = 'none';

            if (type === 'polygone' || type === 'spirale' || type === 'cercle' || type === 'coeur' || type === 'etoile') {
                document.getElementById('params_polygone_spirale').style.display = 'block';
            } else if (type === 'fractale') {
                document.getElementById('params_fractale').style.display = 'block';
            }
        }

        window.onload = updateForm;