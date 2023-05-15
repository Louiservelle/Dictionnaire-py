
from modules.rechercher import recherche


def suppr():
    word = input("Quel mot souhaiter vous supprimer ?\n")
    if(recherche()):
        print(f"Le mot {word} à était supprimer")
    else:
        print("Le mot n'existe pas !")