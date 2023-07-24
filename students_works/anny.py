""""
Je vais ecrire un programme qui cree des dossiers d'etudiants et qui reconnait le dossier
lorsque le nom de celui-ci apparait
Les dossiers contiennent les coordonnees de bases des etudiants tels que :
le nom complet, l'age, le numero de telephone, l'adresse et l'email 

Les dossiers sont nombreux alors pour permettre une meilleure gestion, ce programme les stock de tel sorte 
qu'au momemt ou l'un d'eux est requis, c'est a dire lorsque le nom du dossier apparait, Python l'ouvre 
"""

import json 

def dossier1():
    with open("anny.json") as f:
        json.dump(Surin_Ann_Debby, f)