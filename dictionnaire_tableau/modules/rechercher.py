from modules.decode import decode


def recherche(motTest, dictionnaire):
    # je recuperer la premiere lettre du mot passée en argument
    premiereLettre = motTest[0]
    # cette liste vite va permettre de stocker un dictionaire de chaque mot qui commance par la meme lettre que le mot a rechercher.
    getGroupe = []

    dictionnaire = sorted(
        dictionnaire, key=lambda dictionnaire: dictionnaire["lettre"])  # on trie les lignes en fonction des lettre donc par ordre alphabetique

    for i in range(len(dictionnaire)):
        # on dit que si la lettre du mot correspond a celle du mot a rechercher, on va le stocker le dictionaire dans le quelle il ce trouve dans notre variable getGroupe.
        if dictionnaire[i].get("lettre") == premiereLettre:
            getGroupe.append(dictionnaire[i])

    min = 0
    max = len(getGroupe) - 1

    while min <= max:  # boucle pour la recherche dicotomique
        milieu = (min + max) // 2
        # on stock le dictionaire, en fonction de l'index de la recherche dicotomique, dans une variable listeTestMot
        listeTestMot = getGroupe[milieu]

        # si le mot corespond a la valeur de mot dans le dictionaire
        if motTest == listeTestMot['mot']:
            # on va renvoyer un boolean true et l'index de ou ce mot ce trouve dans la liste
            return True, getGroupe[milieu]
        # sinon on va reeseiler la recherche jusqu'a soit trouver le mot soit renvoyer un boolean false et une valeur d'index a none
        elif motTest < listeTestMot['mot']:
            max = milieu - 1
        else:
            min = milieu + 1

    return False, None
