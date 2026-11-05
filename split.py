# --------------------------------------------------
# GESTION DU SPLIT
# --------------------------------------------------


def split_possible(main):

    # Il faut exactement deux cartes
    if len(main) != 2:
        return False

    # On compare le rang des deux cartes
    # Exemple : 8 et 8, roi et roi, As et As

    if main[0][0] == main[1][0]:
        return True

    return False


def effectuer_split(main, paquet):

    # On vérifie d'abord que le split est possible

    if not split_possible(main):
        return None

    # Première carte = début de la première main
    main_1 = [main[0]]

    # Deuxième carte = début de la deuxième main
    main_2 = [main[1]]

    # On distribue une nouvelle carte à chaque main

    main_1.append(
        paquet.pop()
    )

    main_2.append(
        paquet.pop()
    )

    # On renvoie les deux nouvelles mains

    return [
        main_1,
        main_2
    ]
