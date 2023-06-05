"""
Module1) Module sa baw zouti pouw fe yon bon graph.
Module2) Module sa permet ou, value_a partir de deux valeurs
que ou bali, jwenn equation yon droite.
"""
# pylint: disable= import-error
import sys
from typing import List, Tuple
from matplotlib import pyplot as plt

# MODULE 1


def graph1(
    param_value, *, start_seq: float = None, stop_seq: float = None
) -> List[float]:
    """
    Fonction sa a manipuler done pou ou, de telles
    sortes keu ou kapab fe yon bon courbe ki approchee
    vrai courbe fonction ou vle graf la.
    """

    # checking the type of the parameter value

    try:
        do1 = isinstance(param_value, int or float)
        do2 = isinstance(param_value, list)
    except TypeError:
        print("Ouppsss... that wasn't a valid entry. Try again later.")
        sys.exit()

    # nap defini pi piti interval ki separe 2 points

    if do1 is True:
        pas = param_value / 10000
        value1 = round(-param_value, 4)
    elif do2 is True:
        param_value = param_value[-1]
        try:
            pas = (param_value[-1] - param_value[0]) / 10000
            value1 = round(-param_value[-1], 4)
        except IndexError:
            print("Ouppsss....your list doesn't have enough elements. Kind of empty!")
            sys.exit()

    # redefining the parameter value

    pas = round(pas, 4)
    abscisse = []

    # nan pati sa nap defini valeur keu liste abscisse
    # la ap gen ladann

    if start_seq is not None and stop_seq is not None:
        value1 = start_seq
        while start_seq <= value1 < stop_seq:
            value1 += pas
            value1 = round(value1, 5)
            abscisse.append(value1)

    elif start_seq is not None and stop_seq is None:
        value1 = start_seq
        abscisse.append(value1)
        while value1 < param_value:
            value1 += pas
            value1 = round(value1, 5)
            abscisse.append(value1)

    elif start_seq is None and stop_seq is not None:
        while value1 < stop_seq:
            value1 += pas
            value1 = round(value1, 5)
            abscisse.append(value1)

    else:
        while value1 < param_value:
            value1 += pas
            value1 = round(value1, 5)
            abscisse.append(value1)

    return abscisse


def graph2(
    arg_a: Tuple[List, List],
    arg_b: Tuple[List, List] = None,
    arg_c: Tuple[List, List] = None,
):
    """
    Fonction sa fe graphe pou ou.
    """

    title = input("Donnez le titre de votre graphique: ")
    label = input("bay non courbe ou a: ")
    x_label = input("Ki tit axe abscisse ou an: ")
    y_label = input("Ki tit axe ordonnee ou an: ")
    clr = ["k-", "b-", "r-", "g-"]

    graph = plt.plot(arg_a[0], arg_a[1], clr[0], lw=2.5, label= label)

    if arg_b is not None:
        subgraph1 = plt.plot(arg_b[0], arg_b[1], clr[1], lw=2.5)

    if arg_c is not None:
        subgraph2 = plt.plot(arg_c[0], arg_c[1], clr[2], lw=2.5)

    plt.title(title)
    plt.rcParams["figure.figsize"] = (8, 8)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid("equal", axis="both", color="k", lw=1)
    plt.show()
    plt.close()

    return graph, subgraph1, subgraph2


# MODULE 2


def find_eq(abscisse: Tuple[int or float], ordonnee: Tuple[int or float]):
    """
    fonction sa permet ou jwenn equation yon droite
    de premye degre seulement
    """

    coef_directeur = (ordonnee[1] - ordonnee[0]) / (abscisse[1] - abscisse[0])

    value_b = ordonnee[0] - coef_directeur * abscisse[0]

    print(
        f"L'equation de votre droite est: equation = {coef_directeur}*iter_x + {value_b}"
    )


def graph_eq(
    value_a: int or float, value_b: int or float, value_c: int or float = None, power:int=1
):
    """
    Fonction sa pemet ou fe graph yon fonction premye ou second degre jus par
    equation droite la...
    """

    list_x = [0, 1, 2, 5, 15, 25]
    iter_x = iter(list_x)
    ordonnee = []

    iter_i = 0

    if power == 1:
        while iter_i < len(list_x):
            equation = value_a * next(iter_x) + value_b
            ordonnee.append(equation)
    elif power == 2:
        while iter_i < len(list_x):
            equation = (
                value_a * (next(iter_x) ** 2)
                + 2 * value_a * value_b * next(iter_x)
                + value_c
            )
            ordonnee.append(equation)
    else:
        print("Ouppss...that wasn't valid entry.")

    abscisse = graph1(list_x)
    courbe = graph2(abscisse, ordonnee)

    return courbe


if __name__ == "__main__":
    __all__ = ["graph1", "graph2"]
