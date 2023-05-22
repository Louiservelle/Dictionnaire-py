from modules.rechercher import recherche
from modules.encode import encode


def suppr(dictionnaireGlobal):
    word = input("Quel mot souhaiter vous supprimer ?\n")
    # On appele la fonction recherche pour rechercher si le mot existe
    resultat, dictionnaire = recherche(word, dictionnaireGlobal)
    if (resultat):
        for i in range(len(dictionnaireGlobal)):
            if (dictionnaire == dictionnaireGlobal[i]):  # On suprime la ligne
                dictionnaireGlobal.pop(i)
                print("Le mot a été supprimé.")

    else:
        print("Le mot n'existe pas !")
