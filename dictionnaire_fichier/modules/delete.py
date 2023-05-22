from modules.rechercher import recherche
from modules.encode import encode


def suppr():
    word = input("Quel mot souhaiter vous supprimer ?\n")
    # On appele la fonction recherche pour rechercher si le mot existe
    resultat, dictionnaire = recherche(word)
    if (resultat):
        mot, definition = encode(
            dictionnaire['mot'], dictionnaire['definition'])
        ligneComplete = dictionnaire['lettre'] + "#" + \
            mot + "#" + definition + \
            "\n"  # on convertis le mot qu'on obtient au flrmat du fichier texte
        with open("dictionnaire.txt", "r") as file:
            contenuFichier = file.readlines()

        with open("dictionnaire.txt", 'w') as file:
            for ligne in contenuFichier:
                if ligne.strip() != ligneComplete.strip():
                    file.write(ligne)  # On suprime la ligne
        print("Le mot a été supprimé.")

    else:
        print("Le mot n'existe pas !")
