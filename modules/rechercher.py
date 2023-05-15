#version pas opti
def recherche(dictionnaire):
    mot = input("Entrez un mot : ")
    
    file = open(dictionnaire, 'r')
    for line in file:
        firstletter, word, definition = line.strip().split("#")
        if word == mot:
            print("Définition du mot '{}' : {}\n".format(word, definition))
            return
    
    print("Le mot '{}' n'a pas été trouvé dans le dictionnaire.\n".format(mot))
