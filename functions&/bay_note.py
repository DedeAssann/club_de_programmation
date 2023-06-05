"""
Module sa pemet ou bay not aleatoirement.
"""

import random as rdm


def bay_note(list_non):
    """
    Fonksyon sa bay moun note au hasard
    """
    counter = 0
    note = []
    while counter <= len(list_non):
        note_elev = rdm.randint(0, 21)
        counter += 1
        note.append(note_elev)
    resultat = zip(list_non, note)
    return resultat
