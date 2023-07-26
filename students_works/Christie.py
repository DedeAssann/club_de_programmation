from googletrans import Translator
def translate_text(texte, langue_destination):
    traducteur = Translator()
    traduction = traducteur.translate(texte, dest=langue_destination)
    return traduction.text

if __name__ == "__main__":
    texte = input("Entrez le texte a traduire : ")
    langue_destination = input("Entrez la langue de destination : ")
    translate_text(texte, langue_destination)