""""
Je vais ecrire un programme qui cree des dossiers d'etudiants et qui reconnait le dossier
lorsque le nom de celui-ci apparait
Les dossiers contiennent les coordonnees de bases des etudiants tels que :
le nom complet, l'age, le numero de telephone, l'adresse et l'email 

Les dossiers sont nombreux alors pour permettre une meilleure gestion, ce programme les stock de tel sorte 
qu'au momemt ou l'un d'eux est requis, c'est a dire lorsque le nom du dossier apparait, Python l'ouvre 
"""


with open("Surin Ann Debby", "w") as file:
    file.write("nom = Surin\n") 
    file.write("prenom = Ann Debby\n")
    file.write("age = 15 ans\n")
    file.write("numero_de_telephone = +50934462817\n")
    file.write("adresse = Delmas 95\n")
    file.write("email = anniesurin9@gmail.com\n")


