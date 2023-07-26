"""
_summary_

Let's try something

_extended_summary_
"""


def analyse_des_dossiers(file_path: str) -> list[dict]:
    "..."
    peoples_infos: list[dict] = []
    with open(file_path, "r", encoding="utf-8") as file:
        peoples_data = file.read().strip().split("\n\n")
        for person in peoples_data:
            person_data = {}
            lines = person.strip().split("\n")
            for line in lines:
                key, value = line.split(":")
                person_data[key] = value
            peoples_infos.append({person_data["Nom"]: person_data})
    return peoples_infos


def remise_de_dossiers(nom_a_chercher: str, filepath: str):
    "..."
    peoples_infos = analyse_des_dossiers(filepath)
    for _, value in enumerate(peoples_infos):
        # print("Value : ", value)
        for key in value:
            # print(key)
            if key.strip() == nom_a_chercher.strip():
                print("Dossier Trouve!", key)
                person = value[key]
                print(f"Dossier de  mr/me : {nom_a_chercher.upper()}\n\n\n")
                for key in person:
                    print(key, ": ", person[key])


if __name__ == "__main__":
    filepath = input("Entrez le chemin vers le fichier dans lequel chercher : ")
    nom = input(
        "Entrez le nom de la personne correspondant au dossier que vous recherchez : "
    )
    remise_de_dossiers(nom, filepath)
