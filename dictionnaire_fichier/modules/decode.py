def decode(mot, definition):
    i = 0
    motDecode = ""
    definitionDecode = ""
    while (i <= len(mot)):
        if (i <= len(mot)-1):
            motDecode += int(mot[i]) * mot[i + 1]
            i += 2
        else:
            i = 0
            break

    while (i <= len(definition)):
        if (i <= len(definition)-1):
            definitionDecode += int(definition[i]) * definition[i + 1]
            i += 2
        else:
            return motDecode, definitionDecode
