def longueur(chaine):

    mot = chaine.strip().split()


    if not mot:
        return 0
    return len(mot[-1])


r = "Bonjour, Je suis une fleur coloré  "
long = longueur(r)

print("La longueur du dernier mot est :", long)