# Importation des modules
import os
from operator import itemgetter

# Paramètres
chemin=os.path.abspath(".")
contenu_dossier=os.listdir(chemin)

# Fonction pour récupérer le nom + la taille des fichiers contenus dans le dossier
def infos_fichiers(contenu_dossier):
    # Cette fonction sera un tableau
    tableau=[]
    # Boucle parcourant les fichiers contenus dans le dossier
    for x in contenu_dossier:
        # Ajout des éléments à récupérer par la boucle
        taille=os.path.getsize(x)
        # Conversion + arrondi
        if taille < 1000:
            taille=(round(taille/1000, 2))
        if taille > 1000:
            taille=(round(taille/1000000, 2))
        if taille > 1000000:
            taille=(round(taille/1000000000, 2))
        # Ajout de ces éléments dans le tableau
        tableau.append((x,taille))
    # Clôture de la boucle
    return (tableau)

# Association de la fonction à la variable "Résultats"
resultats=infos_fichiers(contenu_dossier)
# Tri des résultats par taille
tri_resultats=sorted(resultats, key=itemgetter(1), reverse=True)

# Gestion de l'erreur + Affichage des résultats
if len(tri_resultats) < 3:
    print("Pas assez de fichiers. Il en faut trois minimum dans le dossier analysé.")
else:
    print("Voici les trois premiers fichiers de votre dossier, triés par taille (en Mb) dans l'ordre décroissant :")
    print("Fichier 1/3")
    print(*tri_resultats[0], sep=" : ")
    print("Fichier 2/3")
    print(*tri_resultats[1], sep=" : ")
    print("Fichier 3/3")
    print(*tri_resultats[2], sep=" : ")
