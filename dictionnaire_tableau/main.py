from modules.affiche import affichage
from modules.delete import suppr
from modules.insertions import insert
from modules.rechercher import recherche


dictionnaire = []

menu_options = {
    1: "Ajout d'un mot",
    2: "Suppression d'un mot",
    3: "Recherche d'un mot",
    4: "Affichage de tout le dictionnaire",
    0: "Fin du programme"
}


def print_menu():
    for key in menu_options.keys():
        print(key, '-', menu_options[key])


choix = 1
while choix != 0:
    print_menu()
    choix = int(input("Entre ton choix :"))
    match choix:
        case 1:
            NewLigne = insert(dictionnaire)
            dictionnaire.append(NewLigne)
        case 2:
            suppr(dictionnaire)
        case 3:
            mot = input("Entrez un mot : ")
            # on verrifie si le mot est valide
            resultat, dictionnaireLigne = recherche(mot, dictionnaire)
            if (resultat):  # si le mot est valide on l'affiche
                affichage(dictionnaire, dictionnaireLigne)
            else:
                print("mot inexistant !")
        case 4:
            affichage(dictionnaire)
        case 0:
            break
