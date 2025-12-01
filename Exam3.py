def Rom_convert(m):

    valeurs = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    i = 0

    while i < len(m):

        if i + 1 < len(m) and valeurs[m[i]] < valeurs[m[i + 1]]:
            total += valeurs[m[i + 1]] - valeurs[m[i]]
            i += 2
        else:
            total += valeurs[m[i]]
            i += 1

    return total



m = input("saisis un nombre romain : ").upper()

if all(c in "IVXLCDM" for c in m):
    resultat = Rom_convert(m)
    print(f"La valeur entière {m} est : {resultat}")
else:
    print("Entrée invalide.")
