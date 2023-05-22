def encode(mot, definition):

    i = 1
    nb = 1
    motCode = ""
    defCode = ""
    while i <= len(mot):
        if (i == len(mot)):
            motCode += str(nb) + mot[i - 1]
        elif (mot[i] == mot[i - 1]):
            nb += 1
        else:
            motCode += str(nb) + mot[i - 1]
            nb = 1
        i += 1

    i = 1
    nb = 1

    while i <= len(definition):
        if (i == len(definition)):
            defCode += str(nb) + definition[i - 1]
        elif (definition[i] == definition[i - 1]):
            nb += 1
        else:
            defCode += str(nb) + definition[i - 1]
            nb = 1
        i += 1

    return motCode, defCode
