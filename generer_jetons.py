from PIL import Image, ImageDraw, ImageFont
import os
import math


# --------------------------------------------------
# DOSSIER DE SAUVEGARDE
# --------------------------------------------------

dossier = os.path.dirname(
    os.path.abspath(__file__)
)

dossier_jetons = os.path.join(
    dossier,
    "images_jetons"
)

os.makedirs(
    dossier_jetons,
    exist_ok=True
)


# --------------------------------------------------
# DIMENSIONS
# --------------------------------------------------

TAILLE = 500

CENTRE = TAILLE // 2


# --------------------------------------------------
# POLICES
# --------------------------------------------------

try:

    police_valeur = ImageFont.truetype(
        "C:/Windows/Fonts/arial.ttf",
        105
    )

    police_credits = ImageFont.truetype(
        "C:/Windows/Fonts/arial.ttf",
        27
    )

except:

    police_valeur = ImageFont.load_default()

    police_credits = ImageFont.load_default()


# --------------------------------------------------
# LISTE DES JETONS
# --------------------------------------------------

jetons = [

    ("1", (35, 105, 210)),

    ("5", (195, 35, 45)),

    ("10", (30, 30, 35)),

    ("25", (25, 125, 65)),

    ("50", (115, 50, 165)),

    ("100", (215, 155, 30))

]


# --------------------------------------------------
# CRÉATION D'UN JETON
# --------------------------------------------------

def creer_jeton(
    valeur,
    couleur
):

    # Image transparente

    image = Image.new(
        "RGBA",
        (TAILLE, TAILLE),
        (0, 0, 0, 0)
    )


    dessin = ImageDraw.Draw(
        image
    )


    # --------------------------------------------------
    # OMBRE
    # --------------------------------------------------

    dessin.ellipse(
        (50, 55, 460, 465),
        fill=(0, 0, 0, 100)
    )


    # --------------------------------------------------
    # BORDURE EXTÉRIEURE
    # --------------------------------------------------

    dessin.ellipse(
        (35, 30, 455, 450),
        fill=(190, 145, 55)
    )


    # --------------------------------------------------
    # CERCLE PRINCIPAL
    # --------------------------------------------------

    dessin.ellipse(
        (47, 42, 443, 438),
        fill=couleur
    )


    # --------------------------------------------------
    # CERCLE INTÉRIEUR
    # --------------------------------------------------

    dessin.ellipse(
        (75, 70, 415, 410),
        outline=(255, 255, 255),
        width=7
    )


    # --------------------------------------------------
    # MOTIFS BLANCS
    # --------------------------------------------------

    for i in range(12):

        angle = i * (
            math.pi / 6
        )


        x1 = (
            CENTRE
            + math.cos(angle) * 190
        )

        y1 = (
            CENTRE
            + math.sin(angle) * 190
        )


        x2 = (
            CENTRE
            + math.cos(angle) * 155
        )

        y2 = (
            CENTRE
            + math.sin(angle) * 155
        )


        dessin.line(
            (
                x1,
                y1,
                x2,
                y2
            ),
            fill=(255, 255, 255),
            width=16
        )


    # --------------------------------------------------
    # CERCLE CENTRAL
    # --------------------------------------------------

    dessin.ellipse(
        (125, 120, 375, 370),
        fill=couleur,
        outline=(255, 255, 255),
        width=7
    )


    # --------------------------------------------------
    # VALEUR DU JETON
    # --------------------------------------------------

    boite = dessin.textbbox(
        (0, 0),
        valeur,
        font=police_valeur
    )


    largeur = (
        boite[2] - boite[0]
    )

    hauteur = (
        boite[3] - boite[1]
    )


    dessin.text(
        (
            CENTRE - largeur / 2,

            CENTRE
            - hauteur / 2
            - boite[1]
            - 15
        ),

        valeur,

        font=police_valeur,

        fill=(255, 255, 255),

        stroke_width=3,

        stroke_fill=(20, 20, 20)
    )


    # --------------------------------------------------
    # CREDIT / CREDITS
    # --------------------------------------------------

    if valeur == "1":

        texte = "CREDIT"

    else:

        texte = "CREDITS"


    boite = dessin.textbbox(
        (0, 0),
        texte,
        font=police_credits
    )


    largeur = (
        boite[2] - boite[0]
    )


    dessin.text(
        (
            CENTRE - largeur / 2,
            CENTRE + 65
        ),

        texte,

        font=police_credits,

        fill=(255, 255, 255)
    )


    # --------------------------------------------------
    # NOM DU FICHIER
    # --------------------------------------------------

    if valeur == "1":

        nom_fichier = (
            "jeton_1_credit.png"
        )

    else:

        nom_fichier = (
            "jeton_"
            + valeur
            + "_credits.png"
        )


    # --------------------------------------------------
    # SAUVEGARDE
    # --------------------------------------------------

    chemin = os.path.join(
        dossier_jetons,
        nom_fichier
    )


    image.save(
        chemin
    )


# --------------------------------------------------
# CRÉER TOUS LES JETONS
# --------------------------------------------------

for valeur, couleur in jetons:

    creer_jeton(
        valeur,
        couleur
    )


print(
    "Les images des jetons ont été créées."
)
