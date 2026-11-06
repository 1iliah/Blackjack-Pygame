# --------------------------------------------------
# GESTION DES JETONS ET DES MISES
# --------------------------------------------------


MISE_MINIMUM = 25


# --------------------------------------------------
# AJOUTER UN JETON À LA MISE
# --------------------------------------------------

def ajouter_a_mise(
    jetons,
    mise,
    valeur
):

    # Le joueur doit avoir suffisamment
    # de jetons disponibles.

    if valeur > jetons:

        return jetons, mise


    # Le montant est retiré du solde
    # et ajouté à la mise.

    jetons -= valeur

    mise += valeur


    return jetons, mise


# --------------------------------------------------
# VÉRIFIER SI LA MISE EST SUFFISANTE
# --------------------------------------------------

def mise_valide(mise):

    return mise >= MISE_MINIMUM


# --------------------------------------------------
# METTRE À JOUR LES JETONS APRÈS LA MANCHE
# --------------------------------------------------

def mettre_a_jour_jetons(
    jetons,
    mise,
    resultat
):

    # La mise a déjà été retirée
    # du solde avant la partie.


    # Victoire :
    # récupération de la mise
    # + gain équivalent.

    if resultat == "victoire":

        jetons += mise * 2


    # Égalité :
    # récupération de la mise.

    elif resultat == "egalite":

        jetons += mise


    # Défaite :
    # la mise est perdue.

    elif resultat == "defaite":

        jetons = jetons


    return jetons


# --------------------------------------------------
# VÉRIFIER SI LE JOUEUR PEUT ENCORE JOUER
# --------------------------------------------------

def partie_terminee(jetons):

    return jetons < MISE_MINIMUM
