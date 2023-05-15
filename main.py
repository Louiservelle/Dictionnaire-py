from modules.affiche import affichage
from modules.delete import suppr
from modules.insertions import insert
from modules.rechercher import recherche


dictionnaire = {}

menu_options = {
    1: "Ajout d'un mot",
    2: "Suppression d'un mot",
    3: "Recherche d'un mot",
    4: "Affichage de tout le dictionnaire",
    0: "Fin du programme"
}

def print_menu():
    for key in menu_options.keys():
        print (key, '-', menu_options[key] )


while True:
    print_menu()
    choix = int(input("Entre ton choix :"))
    match choix:
        case 1:
            insert()
            print_menu()
            break
        case 2:
            suppr()
            break
        case 3:
            recherche()
            break
        case 4:
            affichage()
            break
        case 0:
            break

