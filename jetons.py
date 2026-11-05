MISE_MINIMUM = 100


def peut_jouer(jetons):
    return jetons >= MISE_MINIMUM


def mettre_a_jour_jetons(jetons, mise, resultat):

    if resultat == "victoire":
        jetons += mise

    elif resultat == "defaite":
        jetons -= mise

    return jetons


def partie_terminee(jetons):
    return jetons < MISE_MINIMUM
