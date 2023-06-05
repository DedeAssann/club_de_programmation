"""
Module systeme mecanique
"""

from energie_mecanique import *


def systeme_mecanique():
    """
    Command line interface for a mecanical system
    """
    chwa = input(
        """
        Eske ou vle:
        1) kalkule yon eneji mekanik
        2) etudye yon sistem mekanik
        q) femen program la
        ?
        """
    )
    while chwa not in ("1", "2", "q"):
        chwa = input(
            """
            Opsyon yo se 1, 2 ou q!
            Eske ou vle:
            1) kalkule yon eneji mekanik
            2) etudye yon sistem mekanik
            q) femen program la
            ?
            """
        )
    if chwa == "q":
        print("Oke! Map femen program la.")
        sys.exit()
    if chwa == "1":
        # fok li kalkule eneji mekanik lan
        tip_eneji, kantite_eneji = energie_mecanique()
        print(f"L'{tip_eneji} du systeme est {kantite_eneji} joules.")
    elif chwa == "2":
        # fok li ofri enteraksyon pou konprann yon sistem mekanik
        non_dokuman_an = input("Banm non dokuman ki gen done sou sistem lan: ")
        if non_dokuman_an not in glob("*"):
            print("Dokuman ou a pa la, map jete m!")
            sys.exit()
        done_sistem = li_dokuman(non_dokuman_an)
    else:
        pass
