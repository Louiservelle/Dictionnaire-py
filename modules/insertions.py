
from modules.rechercher import recherche

caractere_spaces = []

def insert():
    print("Inserting")
    word = input()
    if(word.isdigit()):
        print("Mauvaise saisie")
        word = input()    
    elif(recherche()):
            print("Le mot existe déja dans le dictionnaire")
