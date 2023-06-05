"Fonction sa a kalkule valeur yon nomb juska puissance 3..."


def power(x):
    "Fonction sa a klakule 3 premye degre exposant pou yon nomb ou ba li"
    i = 0
    while i < len(range(1, x + 1)):
        i += 1
        print(f"{x:2d}, {x**2:3d}, {x**3:4d}")


if __name__ == "__main__":
    power()
