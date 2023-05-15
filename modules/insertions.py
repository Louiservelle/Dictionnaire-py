
from modules.rechercher import recherche

caractere_spaces = []

def insert():
    file = open("dictionnaire.txt", "a")
    print("Inserting")
    word = input("Entre le mot à ajouter : \n")
    definitions = input("Ajoute lui une definitions : \n")
    if(word.isdigit()):
        print("Mauvaise saisie !")
        insert()   
    else:
        file.write(f"{word[0]}#{word}#{definitions}\n")

#    elif(recherche()):
#print("Le mot existe déja dans le dictionnaire !")