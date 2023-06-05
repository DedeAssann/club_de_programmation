r"""
Module sa baw des fonction ki pou kalkule carre nonb,
e fe graph.
"""
# pylint: disable= import-error
import numpy as np
import matplotlib.pyplot as plt
from graph_function import graph1, graph2


def squares(arg_x) -> float:
    """
    fonksyon sa baw yon list de carre tout valeur
    ki inferieur a sa ou ba li a, rive nan saw bay la.
    """
    return arg_x**2


def squares1(arg_x):
    """
    This function calculate the square value of
    any number that u give
    """

    carre = [(i**2) for i in range(arg_x + 1)]
    print(carre)

    abscisse = np.linspace(-arg_x, arg_x, 1000)

    ordonnee = [(i**2) for i in abscisse]

    graph = plt.plot(abscisse, ordonnee, "b-", label="Quadratic", lw=2.5)
    plt.title("Fonction carre")
    plt.xlabel("abscisse")
    plt.ylabel("carre")
    plt.legend()
    plt.show()
    plt.close()


    return graph


def squares2(param) -> dict:
    """
    Fonksyon sa li menm, baw repons yo sou forme
    dictionnaire. Li etabli correspondance ant valeur yo, ak carre yo.
    """
    return {arg_x: arg_x**2 for arg_x in range(param + 1)}


def squares3(param_value):
    """
    Fonksyon sa kalkule carre quelque soit valeur,
    ou liste de valeur keu ou bali.
    Et li remet ou valeur ou liste de carre a ainsi que yon graphe.
    """

    # Verification du type de donnee a l'entree

    try:
        do1 = isinstance(param_value, int or float)
        do2 = isinstance(param_value, list)
    except TypeError:
        print("Ouppsss....that was no valid entry!")

    # Calcul du carre...

    if do1:
        carre = param_value**2
    elif do2:
        carre = [(value**2) for value in param_value]
    else:
        pass
    print(carre)

    # Mise en place du graphe

    abscisse = graph1(param_value[-1])

    ordonnee = [(value**2) for value in abscisse]

    courbe = graph2(abscisse, ordonnee)

    return courbe




def integrale_trap(a:int, b:int, n:int) -> float:
    h = (b-a)/n
    moyenne = 0
    while a < b:
        moyenne = moyenne + h*((squares(a) + squares(a+h))/2)
        a += h
    integrale = round(moyenne, 3)
    return integrale



if __name__ == "__main__":
    __all__ = ["squares", "squares1", "squares2", "squares3"]