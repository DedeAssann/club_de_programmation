"""
La mwen tap ekri yon code ki tap pran enfomasyon nan men yon utilisateur, epi pou li ranje yo tankou yon kat identite.
"""
def id():
    Nom = str(input("inserez votre nom : "))
    Prenom = str(input("inserez votre prenom : "))
    sexe = str(input("inserez votre sexe : "))
    age = str(input("inserez votre age : ") )
    Date_de_naissance = str(input("inserez votre date de naissance : "))
    Lieu_de_naissance = str(input("inserez votre lieu de naissance : "))
    adresse = str(input("inserez votre adresse : "))
    Identite = "Je m'appelle {} {}, je suis {}, j'ai {}ans, je suis ne le {}, j'habite {},".format(Nom, Prenom, sexe, age, Lieu_de_naissance, adresse)
    print(Identite)



def zamboum():
    """
    la mwen pral ekri yon fonksyon ki pemet mw crer on liste epi mete valeurs nan liste lan
    """
    fruits = []
    zimzim = "watermelon", "bananas", "strawberry", "ananas", "cherry", "perry"
    for index in range(6):
        fruits.append(zimzim[index])
    print('Voici la liste des fruits : ', fruits)


def boom():
    Classe_de_1ere = []
    eleves = "Debby", "Emilie", "Ira", "Roseline"
    for bimboom in range (4):
        Classe_de_1ere.append(eleves[bimboom])
    print("Les eleves de 1ere sont : ", Classe_de_1ere)


def combinaison():
    """
    done 
    """

    Zamzam = ["Debby", "Ira", "Rosy"]
    Bambam = ["Surin", "Borgella", "Charles Pierre"]
    combined = Zamzam + Bambam
    print(combined)
    
    aller = ["bonjour, Zimbamboom"]
    for wtv in aller :
        print(aller)
    

if __name__ == "__main__":
    combinaison()