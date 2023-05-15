#version pas opti
def recherche(dictionnaire):
    mot = input("Entrez un mot : ")
    
    with open(dictionnaire, 'r') as file:
        for line in file:
            firstletter, word, definition = line.strip().split("#")
            if word == mot:
                print("Définition du mot '{}' : {}".format(word, definition))
                return
    
    print("Le mot '{}' n'a pas été trouvé dans le dictionnaire.".format(mot))
