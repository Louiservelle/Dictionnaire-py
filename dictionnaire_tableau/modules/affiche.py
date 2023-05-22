from modules.decode import decode


def affichage(dictionnaire, dictionnaireTrue=None):
    nbwords = len(dictionnaire)

    print("affichage")
    dictionnaire = sorted(
        dictionnaire, key=lambda dictionnaire: dictionnaire["lettre"])

    if dictionnaireTrue is not None:  # lors de l'appele de la fonction, si un argument et pas null on va donc afficher le mot en fonction de cet argument
        mot, definition = decode(
            dictionnaireTrue['mot'], dictionnaireTrue['definition'])
        print(
            f"Mot: {mot} || Definition: {definition}\n")

    else:  # sinon alors cela signifie que l'appele de la fonction ce fait lors du choix, ou l'on a besoin d'afficher tout les mots avec leurs definitions
        for dictionnaire in dictionnaire:
            mot, definition = decode(
                dictionnaire['mot'], dictionnaire['definition'])
            print(
                f"Mot: {mot} || Definition: {definition}\n")
        print(
            f"Il y a actuellement : {nbwords} mots inscrit dans le dictionnaire\n")
