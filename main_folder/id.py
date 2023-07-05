"""

Ecrire un programme qui demande chacune de ces informations, et les garde dans des variables appropriées.

"""
import pycountry as p
import 

def identite():
    "..."
    nom = str(input("Nom : "))
    prenom = str(input("Prenom : "))
    date_de_naissance = int(input("Annee de naissance : "))
    adresse = str(input("Votre adresse actuelle : "))
    #pays_de_naissance = str(input("Pays de naissance : "))
    sexe = str(input("Sexe (M: Masculin/F: Feminin/N: Non identifie): "))
    
    pays_de_naissance = str(input("Pays de naissance : "))
    while p.countries.get(name=pays_de_naissance.title()) is None:
        print("Pays de Naissance Invalide! Essayez une autre entree.")
        pays_de_naissance = str(input("Pays de naissance : "))
    
    
    
if __name__ == "main":
    identite()