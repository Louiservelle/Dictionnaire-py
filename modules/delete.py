
from modules.rechercher import recherche


def suppr():
    word = input("Quel mot souhaiter vous supprimer ?\n")
    resultat, dictionnaire = recherche(word)
    if (resultat):
        ligneComplete = dictionnaire['lettre'] + "#" + \
            dictionnaire['mot'] + "#" + dictionnaire['definition'] + "\n"
        with open("dictionnaire.txt", "r") as file:
            contenuFichier = file.readlines()

        with open("dictionnaire.txt", 'w') as file:
            for ligne in contenuFichier:
                if ligne.strip() != ligneComplete.strip():
                    file.write(ligne)
        print("Le mot a été supprimé.")

    else:
        print("Le mot n'existe pas !")
