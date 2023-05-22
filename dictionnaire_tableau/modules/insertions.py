from modules.rechercher import recherche
from modules.encode import encode

caractere_spaces = []


def insert(dictionnaire):
    print("Inserting")
    word = input("Entre le mot à ajouter : \n")
    word = word.strip()
    definitions = input("Ajoute lui une definitions : \n")
    resultat, dictionnaireVal = recherche(word, dictionnaire)
    if (word.isdigit()):  # on verifie si le mot est valide
        print("Mauvaise saisie !")
        insert()

    elif (resultat):  # on verrifie si le mot existe
        print("Le mot existe déja dans le dictionnaire !")

    else:
        # si toute les condition sont respecter alors on peut l'ajouter dans le dictionnaire
        word, definitions = encode(word, definitions)
        print("Le mot est enrregistré dans le dictionnaire !")
        return {"lettre": word[1], 'mot': word, "definition": definitions}
