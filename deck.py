import random
import os
from PIL import Image, ImageDraw, ImageFont


# GESTION DU PAQUET

def melanger_paquet(paquet):
    random.shuffle(paquet)

def tirer_carte(paquet):
    return paquet.pop()

def cartes_restantes(paquet):
    return len(paquet)


# RÈGLES DU BLACKJACK

def calculer_score(main):
    score = 0
    nombre_as = 0

    for carte in main:
        valeur = carte

        if valeur in ["J", "Q", "K"]:
            score += 10
        elif valeur == "A":
            score += 11
            nombre_as += 1
        else:
            score += int(valeur)

    while score > 21 and nombre_as > 0:
        score -= 10
        nombre_as -= 1

    return score


def est_blackjack(main):
    if len(main) == 2 and calculer_score(main) == 21:
        return True
    else:
        return False


def joueur_depasse_21(score_joueur):
    return score_joueur > 21


def croupier_depasse_21(score_croupier):
    return score_croupier > 21


def croupier_doit_tirer(score_croupier):
    if score_croupier < 17:
        return True
    else:
        return False


def resultat_partie(score_joueur, score_croupier,
                    blackjack_joueur=False,
                    blackjack_croupier=False):

    if blackjack_joueur and not blackjack_croupier:
        return "Blackjack : victoire du joueur."
    elif blackjack_croupier and not blackjack_joueur:
        return "Blackjack : victoire du croupier."
    elif score_joueur > 21:
        return "Défaite : le joueur a dépassé 21."
    elif score_croupier > 21:
        return "Victoire : le croupier a dépassé 21."
    elif score_joueur > score_croupier:
        return "Victoire : le joueur gagne."
    elif score_joueur < score_croupier:
        return "Défaite : le croupier gagne."
    else:
        return "Égalité."


# CHEMIN DE L'IMAGE D'UNE CARTE

def chemin_image_carte(carte):
    valeur = carte[0]
    symbole = carte[1]

    dossier = os.path.dirname(os.path.abspath(__file__))

    chemin = os.path.join(
        dossier,
        "cartes",
        valeur + "_" + symbole + ".png"
    )

    return chemin


# CRÉATION DES CARTES

dossier = os.path.dirname(os.path.abspath(__file__))
cartes = os.path.join(dossier, "cartes")
os.makedirs(cartes, exist_ok=True)

valeurs = [
    "A", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "J", "Q", "K"
]

symboles = [
    ("coeur", "♥", "red"),
    ("carreau", "♦", "red"),
    ("trefle", "♣", "black"),
    ("pique", "♠", "black")
]

police = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 42
)

police_symbole = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 70
)

police_symbole_cote = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 45
)

grande_police = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 90
)


def centrer(dessin, texte, x, y, police, couleur):
    boite = dessin.textbbox((0, 0), texte, font=police)
    largeur = boite[2] - boite[0]
    hauteur = boite[3] - boite[1]

    dessin.text(
        (x - largeur / 2, y - hauteur / 2),
        texte,
        font=police,
        fill=couleur
    )


positions = {
    "A": [(150, 180)],
    "2": [(150, 110), (150, 250)],
    "3": [(150, 85), (150, 180), (150, 275)],
    "4": [(105, 110), (195, 110), (105, 250), (195, 250)],
    "5": [(105, 100), (195, 100), (150, 180), (105, 260), (195, 260)],
    "6": [(105, 85), (195, 85), (105, 180), (195, 180),
          (105, 275), (195, 275)],
    "7": [(105, 70), (195, 70), (150, 120), (105, 180),
          (195, 180), (105, 290), (195, 290)],
    "8": [(105, 60), (195, 60), (105, 115), (195, 115),
          (105, 245), (195, 245), (105, 300), (195, 300)],
    "9": [(105, 55), (195, 55), (105, 110), (195, 110),
          (150, 180), (105, 250), (195, 250), (105, 305), (195, 305)],
    "10": [(105, 50), (195, 50), (105, 150), (195, 150),
           (105, 220), (195, 220), (105, 320), (195, 320),
           (150, 100), (150, 270)]
}


for nom, symbole, couleur in symboles:

    for valeur in valeurs:

        carte = Image.new("RGBA", (300, 420), (0, 0, 0, 0))
        dessin = ImageDraw.Draw(carte)

        dessin.rounded_rectangle(
            (5, 5, 295, 415),
            radius=25,
            fill="white",
            outline="black",
            width=4
        )

        dessin.rounded_rectangle(
            (12, 12, 288, 408),
            radius=20,
            outline="lightgray",
            width=1
        )

        dessin.text(
            (20, 12),
            valeur,
            font=police,
            fill=couleur
        )

        dessin.text(
            (15, 50),
            symbole,
            font=police_symbole_cote,
            fill=couleur
        )

        dessin.text(
            (240, 315),
            symbole,
            font=police_symbole_cote,
            fill=couleur
        )

        dessin.text(
            (237, 360),
            valeur,
            font=police,
            fill=couleur
        )

        if valeur in positions:

            for x, y in positions[valeur]:
                centrer(
                    dessin,
                    symbole,
                    x,
                    y,
                    police_symbole,
                    couleur
                )

        else:

            centrer(
                dessin,
                valeur,
                150,
                135,
                grande_police,
                couleur
            )

            centrer(
                dessin,
                symbole,
                150,
                225,
                police_symbole,
                couleur
            )

        carte.save(
            os.path.join(
                cartes,
                valeur + "_" + nom + ".png"
            )
        )


# DOS DE LA CARTE

dos = Image.new("RGBA", (300, 420), (0, 0, 0, 0))
dessin = ImageDraw.Draw(dos)

dessin.rounded_rectangle(
    (5, 5, 295, 415),
    radius=25,
    fill="#123524",
    outline="#D4AF37",
    width=6
)

dessin.rounded_rectangle(
    (18, 18, 282, 402),
    radius=18,
    outline="white",
    width=3
)

dessin.rounded_rectangle(
    (30, 30, 270, 390),
    radius=14,
    outline="#D4AF37",
    width=2
)

dessin.polygon(
    [(150, 70), (240, 210), (150, 350), (60, 210)],
    outline="#D4AF37",
    width=3
)

dessin.polygon(
    [(150, 105), (205, 210), (150, 315), (95, 210)],
    outline="white",
    width=2
)

centrer(
    dessin,
    "♠",
    150,
    210,
    grande_police,
    "white"
)

dos.save(os.path.join(cartes, "dos.png"))
