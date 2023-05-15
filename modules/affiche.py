
def affichage():
    dictionnaire = []
    print("affichage")
    file = open("dictionnaire.txt", "r")  #j'ouvre le fichier en mode lecture
    for ligne in file: #je parcours toute les lignes de mon documents
        firstletter, word, definition = ligne.strip().split("#")
        dictionnaire.append({"firstletter": firstletter,"word": word, "definition": definition})
    dictionnaire = sorted(dictionnaire, key=lambda dictionnaire: dictionnaire["firstletter"])
    for dictionnaire in dictionnaire:
        nbwords = len(dictionnaire)
        print(f"Mot: {dictionnaire['word']} || Definition: {dictionnaire['definition']}")
    print(f"Il y a actuellement : {nbwords} mots inscrit dans le dictionnaire\n")
    file.close()