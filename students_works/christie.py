from deep_translator  import GoogleTranslator


def traducteur(texte, langue_cible, langue_source="auto"):
    translator = GoogleTranslator(source=langue_source, target=langue_cible)
    #GoogleTranslator(source=langue_source, target=langue_cible)
    texte_traduit = translator.translate(texte)
    return texte_traduit

def main():
    texte_a_traduire = input("entrez le texte a traduire : ")
    langue_destination = input("entrez la langue de destination : ")
    if langue_destination == "fr":
        texte_traduit = traducteur(texte_a_traduire, langue_destination, langue_source="fr")
    texte_traduit = traducteur(texte_a_traduire, langue_destination)
    print ("Texte traduit : ", texte_traduit)


if __name__=='__main__':
    main()
