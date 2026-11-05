import pygame
import os

from cartes import creer_paquet

from jetons import peut_jouer
from jetons import mettre_a_jour_jetons
from jetons import partie_terminee


# --------------------------------------------------
# INITIALISATION DE PYGAME
# --------------------------------------------------

pygame.init()

LARGEUR = 1000
HAUTEUR = 650

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Table de Blackjack")


# --------------------------------------------------
# COULEURS
# --------------------------------------------------

VERT = (0, 120, 0)
VERT_FONCE = (0, 80, 0)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (200, 200, 200)


# --------------------------------------------------
# POLICES
# --------------------------------------------------

police_titre = pygame.font.Font(None, 40)
police_texte = pygame.font.Font(None, 30)
police_info = pygame.font.Font(None, 22)


# --------------------------------------------------
# FONCTIONS DU JEU
# --------------------------------------------------

def calculer_score(main):

    total = 0
    nombre_as = 0

    for carte in main:

        valeur = carte[2]

        # Si c'est un As
        if isinstance(valeur, list):

            # On commence par considérer l'As comme 11
            total += 11
            nombre_as += 1

        else:

            total += valeur

    # Si on dépasse 21,
    # un As passe de 11 à 1

    while total > 21 and nombre_as > 0:

        total -= 10
        nombre_as -= 1

    return total


def determiner_gagnant(score_joueur, score_croupier):

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
# FONCTIONS POUR LES IMAGES DES CARTES
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
    # on évite de la recharger

    if nom_image in images_cartes:

        return images_cartes[nom_image]

    dossier = os.path.dirname(
        os.path.abspath(__file__)
    )

    chemin = os.path.join(
        dossier,
        "cartes",
        nom_image
    )

    image = pygame.image.load(
        chemin
    ).convert_alpha()

    image = pygame.transform.scale(
        image,
        (90, 126)
    )

    images_cartes[nom_image] = image

    return image


def afficher_carte(carte, x, y):

    image = charger_image_carte(
        carte
    )

    fenetre.blit(
        image,
        (x, y)
    )


# --------------------------------------------------
# DOS DE LA CARTE
# --------------------------------------------------

dossier = os.path.dirname(
    os.path.abspath(__file__)
)

chemin_dos = os.path.join(
    dossier,
    "cartes",
    "dos.png"
)

image_dos = pygame.image.load(
    chemin_dos
).convert_alpha()

image_dos = pygame.transform.scale(
    image_dos,
    (90, 126)
)


def afficher_dos_carte(x, y):

    fenetre.blit(
        image_dos,
        (x, y)
    )


# --------------------------------------------------
# ZONES DU JEU
# --------------------------------------------------

zone_croupier = pygame.Rect(
    100,
    80,
    800,
    180
)

zone_joueur = pygame.Rect(
    100,
    320,
    800,
    180
)

zone_info = pygame.Rect(
    200,
    520,
    600,
    50
)


# --------------------------------------------------
# BOUTONS
# --------------------------------------------------

bouton_distribuer = pygame.Rect(
    70,
    590,
    170,
    50
)

bouton_tirer = pygame.Rect(
    300,
    590,
    150,
    50
)

bouton_rester = pygame.Rect(
    550,
    590,
    150,
    50
)
bouton_split = pygame.Rect(
    775,
    590,
    150,
    50
)

# --------------------------------------------------
# VARIABLES DE LA PARTIE
# --------------------------------------------------

paquet = []

main_joueur = []

main_croupier = []
#variable pour le split
mains_joueur = []
mises_joueur = []
main_actuelle = 0
partie_en_cours = False

croupier_visible = False

message_info = (
    "Appuyez sur D ou DISTRIBUER pour commencer"
)

# Le joueur commence avec 500 jetons

jetons = 500

# Mise actuelle

mise = 100


# --------------------------------------------------
# BOUCLE PRINCIPALE
# --------------------------------------------------

jeu_en_cours = True


while jeu_en_cours:

    action = None


    # --------------------------------------------------
    # GESTION DES ÉVÉNEMENTS
    # --------------------------------------------------

    for evenement in pygame.event.get():

        # Fermer la fenêtre

        if evenement.type == pygame.QUIT:

            jeu_en_cours = False


        # --------------------------------------------------
        # CLAVIER
        # --------------------------------------------------

        if evenement.type == pygame.KEYDOWN:

            if evenement.key == pygame.K_d:

                action = "distribuer"

            elif evenement.key == pygame.K_t:

                action = "tirer"

            elif evenement.key == pygame.K_r:

                action = "rester"
            elif evenement.key == pygame.K_s:

                action = "split"

        # --------------------------------------------------
        # SOURIS
        # --------------------------------------------------

        if evenement.type == pygame.MOUSEBUTTONDOWN:

            if bouton_distribuer.collidepoint(
                evenement.pos
            ):

                action = "distribuer"

            elif bouton_tirer.collidepoint(
                evenement.pos
            ):

                action = "tirer"

            elif bouton_rester.collidepoint(
                evenement.pos
            ):

                action = "rester"
            elif bouton_split.collidepoint(evenement.pos):

                action = "split"


    # --------------------------------------------------
    # DISTRIBUER / NOUVELLE PARTIE
    # --------------------------------------------------

    if action == "distribuer":

        # On vérifie si le joueur possède
        # encore assez de jetons

        if not peut_jouer(jetons):

            message_info = (
                "Vous avez perdu ! "
                "Vous n'avez plus assez de jetons pour jouer."
            )

        elif partie_en_cours:

            message_info = (
                "Terminez d'abord la partie en cours."
            )

        else:

            # Cette fonction vient maintenant
            # directement de cartes.py

            paquet = creer_paquet()

            # Réinitialiser les mains

            main_joueur = []
            main_croupier = []


            # Deux cartes pour le joueur

            main_joueur.append(
                paquet.pop()
            )

            main_joueur.append(
                paquet.pop()
            )


            # Deux cartes pour le croupier

            main_croupier.append(
                paquet.pop()
            )

            main_croupier.append(
                paquet.pop()
            )


            partie_en_cours = True

            croupier_visible = False

            message_info = (
                "À vous : T = tirer une carte | R = rester"
            )


            # Calcul des scores

            score_joueur = calculer_score(
                main_joueur
            )

            score_croupier = calculer_score(
                main_croupier
            )


            # Vérification d'un 21 dès la distribution

            if (
                score_joueur == 21
                or score_croupier == 21
            ):

                croupier_visible = True

                partie_en_cours = False

                resultat, message_info = determiner_gagnant(
                    score_joueur,
                    score_croupier
                )

                jetons = mettre_a_jour_jetons(
                    jetons,
                    mise,
                    resultat
                )

                if partie_terminee(jetons):

                    message_info = (
                        "Vous avez perdu ! "
                        "Vous n'avez plus assez de jetons pour continuer."
                    )


    # --------------------------------------------------
    # TIRER
    # --------------------------------------------------

    elif action == "tirer" and partie_en_cours:

        nouvelle_carte = paquet.pop()

        main_joueur.append(
            nouvelle_carte
        )

        score_joueur = calculer_score(
            main_joueur
        )

        message_info = (
            "Vous avez tiré : "
            + nouvelle_carte[0]
            + " de "
            + nouvelle_carte[1].strip()
        )


        # Joueur dépasse 21

        if score_joueur > 21:

            croupier_visible = True

            partie_en_cours = False

            score_croupier = calculer_score(
                main_croupier
            )

            resultat, message_info = determiner_gagnant(
                score_joueur,
                score_croupier
            )

            jetons = mettre_a_jour_jetons(
                jetons,
                mise,
                resultat
            )

            if partie_terminee(jetons):

                message_info = (
                    "Vous avez perdu ! "
                    "Vous n'avez plus assez de jetons pour continuer."
                )


        # Joueur a exactement 21

        elif score_joueur == 21:

            message_info = (
                "Vous avez 21 ! "
                "Appuyez sur R pour rester."
            )


    # --------------------------------------------------
    # RESTER
    # --------------------------------------------------

    elif action == "rester" and partie_en_cours:

        croupier_visible = True


        # Le croupier tire tant qu'il a moins de 17

        while calculer_score(
            main_croupier
        ) < 17:

            main_croupier.append(
                paquet.pop()
            )


        score_joueur = calculer_score(
            main_joueur
        )

        score_croupier = calculer_score(
            main_croupier
        )


        resultat, message_info = determiner_gagnant(
            score_joueur,
            score_croupier
        )


        jetons = mettre_a_jour_jetons(
            jetons,
            mise,
            resultat
        )


        partie_en_cours = False


        if partie_terminee(jetons):

            message_info = (
                "Vous avez perdu ! "
                "Vous n'avez plus assez de jetons pour continuer."
            )


    # --------------------------------------------------
    # FOND
    # --------------------------------------------------

    fenetre.fill(
        VERT
    )


    # --------------------------------------------------
    # TITRE
    # --------------------------------------------------

    titre = police_titre.render(
        "BLACKJACK",
        True,
        BLANC
    )

    fenetre.blit(
        titre,
        (400, 20)
    )


    # --------------------------------------------------
    # AFFICHAGE DES JETONS
    # --------------------------------------------------

    texte_jetons = police_texte.render(
        "Jetons : " + str(jetons),
        True,
        BLANC
    )

    fenetre.blit(
        texte_jetons,
        (800, 20)
    )


    # --------------------------------------------------
    # ZONE CROUPIER
    # --------------------------------------------------

    pygame.draw.rect(
        fenetre,
        VERT_FONCE,
        zone_croupier,
        3
    )

    texte_croupier = police_texte.render(
        "Cartes du croupier",
        True,
        BLANC
    )

    fenetre.blit(
        texte_croupier,
        (120, 95)
    )


    # --------------------------------------------------
    # AFFICHAGE DES CARTES DU CROUPIER
    # --------------------------------------------------

    for i, carte in enumerate(
        main_croupier
    ):

        x = 150 + i * 105

        y = 125


        if i == 1 and not croupier_visible:

            afficher_dos_carte(
                x,
                y
            )

        else:

            afficher_carte(
                carte,
                x,
                y
            )


    # --------------------------------------------------
    # SCORE DU CROUPIER
    # --------------------------------------------------

    if len(main_croupier) > 0:

        if croupier_visible:

            score_croupier = calculer_score(
                main_croupier
            )

            texte_score_croupier = police_texte.render(
                "Score : " + str(score_croupier),
                True,
                BLANC
            )

        else:

            texte_score_croupier = police_texte.render(
                "Score : ?",
                True,
                BLANC
            )

        fenetre.blit(
            texte_score_croupier,
            (750, 95)
        )


    # --------------------------------------------------
    # ZONE JOUEUR
    # --------------------------------------------------

    pygame.draw.rect(
        fenetre,
        VERT_FONCE,
        zone_joueur,
        3
    )

    texte_joueur = police_texte.render(
        "Cartes du joueur",
        True,
        BLANC
    )

    fenetre.blit(
        texte_joueur,
        (120, 335)
    )


    # --------------------------------------------------
    # AFFICHAGE DES CARTES DU JOUEUR
    # --------------------------------------------------

    for i, carte in enumerate(
        main_joueur
    ):

        x = 150 + i * 105

        y = 365

        afficher_carte(
            carte,
            x,
            y
        )


    # --------------------------------------------------
    # SCORE DU JOUEUR
    # --------------------------------------------------

    if len(main_joueur) > 0:

        score_joueur = calculer_score(
            main_joueur
        )

        texte_score_joueur = police_texte.render(
            "Score : " + str(score_joueur),
            True,
            BLANC
        )

        fenetre.blit(
            texte_score_joueur,
            (750, 335)
        )


    # --------------------------------------------------
    # INFORMATIONS DE LA PARTIE
    # --------------------------------------------------

    pygame.draw.rect(
        fenetre,
        VERT_FONCE,
        zone_info
    )

    texte_infos = police_info.render(
        message_info,
        True,
        BLANC
    )

    position_info = texte_infos.get_rect(
        center=zone_info.center
    )

    fenetre.blit(
        texte_infos,
        position_info
    )


    # --------------------------------------------------
    # BOUTON DISTRIBUER
    # --------------------------------------------------

    pygame.draw.rect(
        fenetre,
        GRIS,
        bouton_distribuer
    )

    texte_distribuer = police_texte.render(
        "DISTRIBUER",
        True,
        NOIR
    )

    fenetre.blit(
        texte_distribuer,
        texte_distribuer.get_rect(
            center=bouton_distribuer.center
        )
    )


    # --------------------------------------------------
    # BOUTON TIRER
    # --------------------------------------------------

    pygame.draw.rect(
        fenetre,
        GRIS,
        bouton_tirer
    )

    texte_tirer = police_texte.render(
        "TIRER",
        True,
        NOIR
    )

    fenetre.blit(
        texte_tirer,
        texte_tirer.get_rect(
            center=bouton_tirer.center
        )
    )


    # --------------------------------------------------
    # BOUTON RESTER
    # --------------------------------------------------

    pygame.draw.rect(
        fenetre,
        GRIS,
        bouton_rester
    )

    texte_rester = police_texte.render(
        "RESTER",
        True,
        NOIR
    )

    fenetre.blit(
        texte_rester,
        texte_rester.get_rect(
            center=bouton_rester.center
        )
    )
# BOUTON SPLIT

pygame.draw.rect(
    fenetre,
    GRIS,
    bouton_split
)

texte_split = police_texte.render(
    "SPLIT",
    True,
    NOIR
)

fenetre.blit(
    texte_split,
    texte_split.get_rect(
        center=bouton_split.center
    )
)

    # --------------------------------------------------
    # ACTUALISER L'ÉCRAN
    # --------------------------------------------------

    pygame.display.update()


# --------------------------------------------------
# FERMER PYGAME
# --------------------------------------------------

pygame.quit()
