"""
Module sa baw zouti pou kalkule inverse yon valeur
keu ou bali.
"""

import sys
from graph_function import graph1, graph2


def inverse(value) -> float:
    """
    Fonction sa a kalkule inverse nonb ou ba li an
    """
    inv = 1 / value
    return inv


def inverse1(value):
    """
    Cette fonction permet de calculer toutes les valeurs
    allant de 0 a la valeur donnee en argument.
    """
    inv = []
    i = 1
    while i <= value:
        f_inv = 1 / i
        tip = type(f_inv)
        if tip == float:
            f_inv = round(f_inv, 5)
            inv.append(f_inv)
        else:
            inv.append(f_inv)
        i += 1
    return inv


def inverse2(param_value: int or float):
    """
    Fonksyon sa utilize module pou fe graph, li kalkule
    valeur inverse argument ou ba li a, et li remet ou
    inverse la, ak yon graph appropriye.
    """
    try:
        inv = inverse(param_value)
        print(inv)
    except TypeError:
        print("Oupss...That wasn't valid entry")
        sys.exit()
    else:
        pass

    pas = 1 / 1000
    abscisse1 = []

    abscisse1 = graph1(param_value, stop_seq=-pas)
    abscisse2 = graph1(param_value, start_seq=pas)

    ordonnee1 = [(1 / (value)) for value in abscisse1]
    ordonnee2 = [(1 / (value1)) for value1 in abscisse2]

    courbe = graph2(abscisse1, ordonnee1, abscisse2, ordonnee2)

    return courbe


__all__ = ["inverse", "inverse1", "inverse2"]
