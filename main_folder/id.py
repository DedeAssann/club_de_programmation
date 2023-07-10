"""
Ecrire un programme qui demande chacune de ces informations, et les garde dans des variables appropriées.
"""

from datetime import date
import pycountry as p
import time


def identite():
    "..."
    nom = str(input("Nom : "))
    prenom = str(input("Prenom : "))
    while not nom.isalpha() or not prenom.isalpha():
        print("Nom ou Prenom Invalide! Veuillez essayer une autre entree.")
        nom = str(input("Nom : "))
        prenom = str(input("Prenom : "))
    # Date de Naissance
    jour, mois, annee = (input("Date de naissance (Format JJ-MM-AAAA) : ")).split("-")
    date_de_naissance = date(int(annee), int(mois), int(jour))
    mois_de_lannee = {
        1: "Janvier",
        2: "Fevrier",
        3: "Mars",
        4: "Avril",
        5: "Mai",
        6: "Juin",
        7: "Juillet",
        8: "Aout",
        9: "Septembre",
        10: "Octobre",
        11: "Novembre",
        12: "Decembre",
    }
    mois = mois_de_lannee[int(mois)]
    delta = date.today() - date_de_naissance
    age = int(delta.days / 365.25)
    if age >= 18:
        legalite = "Majeur"
    else:
        legalite = "Mineur"
    # Sexe et titre
    sexe = str(input("Sexe (M: Masculin/F: Feminin/N: Non identifie): "))
    while sexe.capitalize() not in ("M", "F", "N"):
        print("Mauvaise entree!")
        sexe = str(input("Sexe (M: Masculin/F: Feminin/N: Non identifie): "))
    if sexe == "M":
        civilite = "Mr."
    elif sexe == "F":
        civilite = "Mme."
    else:
        civilite = "Mr./Mme"
    pays_de_naissance = str(input("Pays de naissance : "))
    while p.countries.get(name=pays_de_naissance.title()) is None:
        print("Pays de Naissance Invalide! Essayez une autre entree.")
        pays_de_naissance = str(input("Pays de naissance : "))
    adresse = str(input("Votre adresse actuelle : "))  # .isalphanum()

    time.sleep(2)
    print("\n\nVeuillez patienter...")
    time.sleep(4)

    id = """\n\n\n
    Recapitulatif de l'identite de {0} {1}.
        Nom          :   {1}
        Prenom       :   {2}
        Sexe         :   {3}
        Date de Naissance: {4} {5} {6}
        Age          :   {7}
        Legalite     :   {8}
        Adresse      :   {9}
    """.format(
        civilite,
        nom,
        prenom,
        sexe,
        jour,
        mois,
        annee,
        age,
        legalite,
        adresse,
    )
    print(id)
    time.sleep(2)


if __name__ == "__main__":
    identite()
