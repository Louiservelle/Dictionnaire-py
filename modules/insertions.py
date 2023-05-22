
from modules.rechercher import recherche

caractere_spaces = []


def insert():
    file = open("dictionnaire.txt", "a")
    print("Inserting")
    word = input("Entre le mot à ajouter : \n")
    definitions = input("Ajoute lui une definitions : \n")
    if (word.isdigit()):  # on verifie si le mot est valide
        print("Mauvaise saisie !")
        insert()
    elif (recherche(word)):  # on verrifie si le mot existe
        print("Le mot existe déja dans le dictionnaire !")
    else:
        # si toute les condition sont respecter alors on peut l'ajouter dans le dictionnaire
        file.write(f"{word[0]}#{word}#{definitions}\n")
