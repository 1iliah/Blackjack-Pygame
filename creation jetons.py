from PIL import Image, ImageDraw, ImageFont
import os
import math

# Dossier de sauvegarde
dossier = os.path.dirname(os.path.abspath(__file__))
dossier_jetons = os.path.join(dossier, "jetons")

os.makedirs(dossier_jetons, exist_ok=True)

# Dimensions des images
TAILLE = 500
CENTRE = TAILLE // 2

# Polices
try:
    police_valeur = ImageFont.truetype("arial.ttf", 105)
    police_credits = ImageFont.truetype("arial.ttf", 27)
except:
    police_valeur = ImageFont.load_default()
    police_credits = ImageFont.load_default()

# Liste des jetons
jetons = [
    ("1", (35, 105, 210)),
    ("5", (195, 35, 45)),
    ("10", (30, 30, 35)),
    ("25", (25, 125, 65)),
    ("50", (115, 50, 165)),
    ("100", (215, 155, 30))
]


# Fonction de création d'un jeton
def creer_jeton(valeur, couleur):

    # Image avec fond transparent
    image = Image.new(
        "RGBA",
        (TAILLE, TAILLE),
        (0, 0, 0, 0)
    )

    dessin = ImageDraw.Draw(image)

    # Ombre
    dessin.ellipse(
        (50, 55, 460, 465),
        fill=(0, 0, 0, 100)
    )

    # Bordure extérieure dorée
    dessin.ellipse(
        (35, 30, 455, 450),
        fill=(190, 145, 55)
    )

    # Cercle principal
    dessin.ellipse(
        (47, 42, 443, 438),
        fill=couleur
    )

    # Cercle intérieur
    dessin.ellipse(
        (75, 70, 415, 410),
        outline=(255, 255, 255),
        width=7
    )

    # Motifs blancs autour du jeton
    for i in range(12):

        angle = i * (math.pi / 6)

        x1 = CENTRE + math.cos(angle) * 190
        y1 = CENTRE + math.sin(angle) * 190

        x2 = CENTRE + math.cos(angle) * 155
        y2 = CENTRE + math.sin(angle) * 155

        dessin.line(
            (x1, y1, x2, y2),
            fill=(255, 255, 255),
            width=16
        )

    # Cercle central
    dessin.ellipse(
        (125, 120, 375, 370),
        fill=couleur,
        outline=(255, 255, 255),
        width=7
    )

    # Valeur du jeton
    boite = dessin.textbbox(
        (0, 0),
        valeur,
        font=police_valeur
    )

    largeur = boite[2] - boite[0]
    hauteur = boite[3] - boite[1]

    dessin.text(
        (
            CENTRE - largeur / 2,
            CENTRE - hauteur / 2 - boite[1] - 15
        ),
        valeur,
        font=police_valeur,
        fill=(255, 255, 255),
        stroke_width=3,
        stroke_fill=(20, 20, 20)
    )

    # Texte indiquant la mise
    texte = "CREDIT" if valeur == "1" else "CREDITS"

    boite = dessin.textbbox(
        (0, 0),
        texte,
        font=police_credits
    )

    largeur = boite[2] - boite[0]

    dessin.text(
        (
            CENTRE - largeur / 2,
            CENTRE + 65
        ),
        texte,
        font=police_credits,
        fill=(255, 255, 255)
    )

    # Nom du fichier selon la mise
    if valeur == "1":
        nom_fichier = "jeton_1_credit.png"
    else:
        nom_fichier = "jeton_" + valeur + "_credits.png"

    # Sauvegarde
    chemin = os.path.join(
        dossier_jetons,
        nom_fichier
    )

    image.save(chemin)

   
# Création de tous les jetons
for valeur, couleur in jetons:

    creer_jeton(valeur, couleur)
