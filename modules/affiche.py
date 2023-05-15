
def affichage():
    dictionnaire = []
    print("affichage")
    file = open("dictionnaire.txt", "r")  #j'ouvre le fichier en mode lecture
    for ligne in file: #je parcours toute les lignes de mon documents
        firstletter, word, definition= ligne.strip().split("#") #je sépare chaque infos séparer d'une #
        dictionnaire.append({"firstletter": firstletter,"word": word, "definition": definition})
    print(dictionnaire) #je fait un dictionnaire clef valeurs via mais input
    dictionnaire = sorted(dictionnaire, key=lambda dictionnaire: dictionnaire["firstletter"])
    for dictionnaire in dictionnaire:
        nbwords = len(dictionnaire)
        print(f"{dictionnaire['word']} {dictionnaire['definition']}")
    print(f"Il y a actuellement :{nbwords}")
    file.close()