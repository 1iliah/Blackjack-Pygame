import pygame
import os


# --------------------------------------------------
# TAILLE DES JETONS À L'ÉCRAN
# --------------------------------------------------

TAILLE_JETON = 45


# --------------------------------------------------
# VALEURS DES JETONS
# --------------------------------------------------

valeurs_jetons = [

    1,
    5,
    10,
    25,
    50,
    100

]


# --------------------------------------------------
# NOMS DES FICHIERS
# --------------------------------------------------

fichiers_jetons = {

    1: "jeton_1_credit.png",

    5: "jeton_5_credits.png",

    10: "jeton_10_credits.png",

    25: "jeton_25_credits.png",

    50: "jeton_50_credits.png",

    100: "jeton_100_credits.png"

}


# --------------------------------------------------
# ZONES CLIQUABLES
# --------------------------------------------------

zones_jetons = {}


for i, valeur in enumerate(
    valeurs_jetons
):

    x = 20 + i * 55

    y = 20


    zones_jetons[valeur] = pygame.Rect(
        x,
        y,
        TAILLE_JETON,
        TAILLE_JETON
    )


# --------------------------------------------------
# MÉMOIRE DES IMAGES
# --------------------------------------------------

images_jetons = {}


# --------------------------------------------------
# CHARGER UNE IMAGE DE JETON
# --------------------------------------------------

def charger_image_jeton(valeur):

    # Si l'image est déjà chargée

    if valeur in images_jetons:

        return images_jetons[
            valeur
        ]


    dossier = os.path.dirname(
        os.path.abspath(__file__)
    )


    chemin = os.path.join(
        dossier,
        "images_jetons",
        fichiers_jetons[valeur]
    )


    image = pygame.image.load(
        chemin
    ).convert_alpha()


    image = pygame.transform.scale(
        image,
        (
            TAILLE_JETON,
            TAILLE_JETON
        )
    )


    images_jetons[
        valeur
    ] = image


    return image


# --------------------------------------------------
# AFFICHER TOUS LES JETONS
# --------------------------------------------------

def afficher_jetons(fenetre):

    for valeur in valeurs_jetons:

        image = charger_image_jeton(
            valeur
        )


        fenetre.blit(
            image,
            zones_jetons[valeur]
        )


# --------------------------------------------------
# DÉTECTER LE JETON CLIQUÉ
# --------------------------------------------------

def detecter_jeton(position):

    for valeur in valeurs_jetons:

        if zones_jetons[
            valeur
        ].collidepoint(
            position
        ):

            return valeur


    return None
