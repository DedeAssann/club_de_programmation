Nom = str(input("inserez votre nom : "))
Prenom = str(input("inserez votre prenom : "))
sexe = str(input("inserez votre sexe : "))
age = str(input("inserez votre age : ") )
Date_de_naissance = str(input("inserez votre date de naissance : "))
Lieu_de_naissance = str(input("inserez votre lieu de naissance : "))
adresse = str(input("inserez votre adresse : "))
Identite = "Je m'appelle {} {}, je suis {}, j'ai {}ans, je suis ne le {}, j'habite {},".format(Nom, Prenom, sexe, age, Lieu_de_naissance, adresse)
print(Identite