from jetons import mettre_a_jour_jetons


# --------------------------------------------------
# CALCUL DU SCORE
# --------------------------------------------------

def calculer_score(main):

    total = 0
    nombre_as = 0

    for carte in main:

        valeur = carte[2]

        # Si la carte est un As
        if isinstance(valeur, list):

            # On commence par compter l'As comme 11
            total += 11
            nombre_as += 1

        else:

            total += valeur


    # Si le score dépasse 21,
    # on transforme un As de 11 en 1

    while total > 21 and nombre_as > 0:

        total -= 10
        nombre_as -= 1


    return total


# --------------------------------------------------
# DÉTERMINER LE GAGNANT
# --------------------------------------------------

def determiner_gagnant(
    score_joueur,
    score_croupier
):

    if score_joueur > 21:

        return (
            "defaite",
            "Vous avez dépassé 21 : le croupier gagne !"
        )


    elif score_croupier > 21:

        return (
            "victoire",
            "Le croupier dépasse 21 : vous gagnez !"
        )


    elif score_joueur > score_croupier:

        return (
            "victoire",
            "Vous gagnez !"
        )


    elif score_croupier > score_joueur:

        return (
            "defaite",
            "Le croupier gagne !"
        )


    else:

        return (
            "egalite",
            "Égalité !"
        )


# --------------------------------------------------
# TERMINER UNE MANCHE
# --------------------------------------------------

def terminer_manche(
    paquet,
    main_croupier,
    mains,
    mises,
    jetons
):

    # On vérifie si au moins une main du joueur
    # n'a pas dépassé 21

    joueur_encore_en_jeu = False


    for main in mains:

        if calculer_score(main) <= 21:

            joueur_encore_en_jeu = True


    # Si le joueur a encore au moins une main valide,
    # le croupier joue

    if joueur_encore_en_jeu:

        while calculer_score(
            main_croupier
        ) < 17:

            main_croupier.append(
                paquet.pop()
            )


    # Score final du croupier

    score_croupier = calculer_score(
        main_croupier
    )


    messages = []


    # On regarde le résultat de chaque main du joueur

    for i in range(len(mains)):

        score_joueur = calculer_score(
            mains[i]
        )


        resultat, message = determiner_gagnant(
            score_joueur,
            score_croupier
        )


        # Mise à jour des jetons
        # grâce à la fonction de jetons.py

        jetons = mettre_a_jour_jetons(
            jetons,
            mises[i],
            resultat
        )


        # S'il n'y a qu'une main

        if len(mains) == 1:

            messages.append(
                message
            )


        # S'il y a eu un split

        else:

            messages.append(
                "Main "
                + str(i + 1)
                + " : "
                + message
            )


    # Regrouper les messages des deux mains

    message_final = " | ".join(
        messages
    )


    return jetons, message_final

