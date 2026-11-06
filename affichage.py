import pygame
import os


# --------------------------------------------------
# CONVERSION DES NOMS DE CARTES
# --------------------------------------------------

def convertir_valeur_image(valeur):

    if valeur == "As":
        return "A"

    elif valeur == "valet":
        return "J"

    elif valeur == "dame":
        return "Q"

    elif valeur == "roi":
        return "K"

    else:
        return valeur


def convertir_symbole_image(symbole):

    symbole = symbole.strip().lower()

    if symbole == "trèfle":
        return "trefle"

    else:
        return symbole


# --------------------------------------------------
# IMAGES DES CARTES
# --------------------------------------------------

# On garde en mémoire les images
# qui ont déjà été chargées.

images_cartes = {}


def charger_image_carte(carte):

    valeur = convertir_valeur_image(
        carte[0]
    )

    symbole = convertir_symbole_image(
        carte[1]
    )

    nom_image = (
        valeur
        + "_"
        + symbole
        + ".png"
    )


    # Si l'image a déjà été chargée,
    # on la récupère directement.

    if nom_image in images_cartes:

        return images_cartes[
            nom_image
        ]


    # Dossier où se trouve affichage.py

    dossier = os.path.dirname(
        os.path.abspath(__file__)
    )


    # Chemin vers l'image

    chemin = os.path.join(
        dossier,
        "cartes",
        nom_image
    )


    # Charger l'image

    image = pygame.image.load(
        chemin
    ).convert_alpha()


    # Redimensionner

    image = pygame.transform.scale(
        image,
        (90, 126)
    )


    # Garder l'image en mémoire

    images_cartes[
        nom_image
    ] = image


    return image


# --------------------------------------------------
# AFFICHER UNE CARTE
# --------------------------------------------------

def afficher_carte(
    fenetre,
    carte,
    x,
    y
):

    image = charger_image_carte(
        carte
    )

    fenetre.blit(
        image,
        (x, y)
    )


# --------------------------------------------------
# DOS DE CARTE
# --------------------------------------------------

def charger_dos_carte():

    dossier = os.path.dirname(
        os.path.abspath(__file__)
    )

    chemin_dos = os.path.join(
        dossier,
        "cartes",
        "dos.png"
    )


    image = pygame.image.load(
        chemin_dos
    ).convert_alpha()


    image = pygame.transform.scale(
        image,
        (90, 126)
    )


    return image


# IMPORTANT :
# On ne charge PAS l'image maintenant.
#
# Quand affichage.py est importé,
# la fenêtre Pygame n'existe pas encore.
#
# On attend donc le premier affichage.

image_dos = None


def afficher_dos_carte(
    fenetre,
    x,
    y
):

    global image_dos


    # Charger le dos seulement
    # lors de la première utilisation.

    if image_dos is None:

        image_dos = charger_dos_carte()


    fenetre.blit(
        image_dos,
        (x, y)
    )
