import random
def get_user_choice():
    while True:
        user_choice = input("choisissez : roche, papier, ou ciseaux : ").lower()
        if user_choice in ['roche', 'papier', 'ciseaux']:
            return user_choice 
        else:
            print ("choix invalide. Veuillez choisir parmi roche") 