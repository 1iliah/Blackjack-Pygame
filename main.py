import pygame
import os

from cartes import creer_paquet

from jetons import peut_jouer
from jetons import mettre_a_jour_jetons
from jetons import partie_terminee

from split import split_possible
from split import effectuer_split


# --------------------------------------------------
# INITIALISATION DE PYGAME
# --------------------------------------------------

pygame.init()

LARGEUR = 1000
HAUTEUR = 650

fenetre = pygame.display.set_mode(
    (LARGEUR, HAUTEUR)
)

pygame.display.set_caption(
    "Table de Blackjack"
)


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

police_titre = pygame.font.Font(
    None,
    40
)

police_texte = pygame.font.Font(
    None,
    30
)

police_info = pygame.font.Font(
    None,
    22
)


# --------------------------------------------------
# FONCTIONS DU JEU
# --------------------------------------------------

def calculer_score(main):

    total = 0
    nombre_as = 0

    for carte in main:

        valeur = carte[2]

        if isinstance(valeur, list):

            total += 11
            nombre_as += 1

        else:

            total += valeur

    while total > 21 and nombre_as > 0:

        total -= 10
        nombre_as -= 1

    return total


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

    # Si au moins une main n'a pas dépassé 21,
    # le croupier doit jouer.

    joueur_encore_en_jeu = False

    for main in mains:

        if calculer_score(main) <= 21:

            joueur_encore_en_jeu = True


    if joueur_encore_en_jeu:

        while calculer_score(
            main_croupier
        ) < 17:

            main_croupier.append(
                paquet.pop()
            )


    score_croupier = calculer_score(
        main_croupier
    )


    messages = []


    # On calcule le résultat de chaque main

    for i in range(len(mains)):

        score_joueur = calculer_score(
            mains[i]
        )

        resultat, message = determiner_gagnant(
            score_joueur,
            score_croupier
        )

        jetons = mettre_a_jour_jetons(
            jetons,
            mises[i],
            resultat
        )


        if len(mains) == 1:

            messages.append(
                message
            )

        else:

            messages.append(
                "Main "
                + str(i + 1)
                + " : "
                + message
            )


    message_final = " | ".join(
        messages
    )


    return jetons, message_final


# --------------------------------------------------
# FONCTIONS POUR LES IMAGES
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


    if nom_image in images_cartes:

        return images_cartes[
            nom_image
        ]


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


    images_cartes[
        nom_image
    ] = image


    return image


def afficher_carte(
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


def afficher_dos_carte(
    x,
    y
):

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
    150,
    520,
    700,
    50
)


# --------------------------------------------------
# BOUTONS
# --------------------------------------------------

bouton_distribuer = pygame.Rect(
    40,
    590,
    170,
    50
)

bouton_tirer = pygame.Rect(
    260,
    590,
    150,
    50
)

bouton_rester = pygame.Rect(
    470,
    590,
    150,
    50
)

bouton_split = pygame.Rect(
    680,
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


# En temps normal, cette liste contient
# seulement main_joueur.
#
# Après un split, elle contiendra :
# [main_1, main_2]

mains_joueur = []


# Même principe pour les mises.

mises_joueur = []


# Permet de savoir quelle main
# est actuellement jouée.

main_actuelle = 0


# False = pas de split
# True = le joueur joue deux mains

split_actif = False


partie_en_cours = False

croupier_visible = False


message_info = (
    "Appuyez sur D ou DISTRIBUER pour commencer"
)


# --------------------------------------------------
# JETONS
# --------------------------------------------------

jetons = 500

mise = 100


# --------------------------------------------------
# BOUCLE PRINCIPALE
# --------------------------------------------------

jeu_en_cours = True


while jeu_en_cours:

    action = None


    # --------------------------------------------------
    # ÉVÉNEMENTS
    # --------------------------------------------------

    for evenement in pygame.event.get():

        if evenement.type == pygame.QUIT:

            jeu_en_cours = False


        # CLAVIER

        if evenement.type == pygame.KEYDOWN:

            if evenement.key == pygame.K_d:

                action = "distribuer"


            elif evenement.key == pygame.K_t:

                action = "tirer"


            elif evenement.key == pygame.K_r:

                action = "rester"


            elif evenement.key == pygame.K_s:

                action = "split"


        # SOURIS

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


            elif bouton_split.collidepoint(
                evenement.pos
            ):

                action = "split"


    # --------------------------------------------------
    # DISTRIBUER
    # --------------------------------------------------

    if action == "distribuer":

        if not peut_jouer(
            jetons
        ):

            message_info = (
                "Vous avez perdu ! "
                "Vous n'avez plus assez de jetons."
            )


        elif partie_en_cours:

            message_info = (
                "Terminez d'abord la partie en cours."
            )


        else:

            paquet = creer_paquet()


            main_joueur = []

            main_croupier = []


            # Deux cartes joueur

            main_joueur.append(
                paquet.pop()
            )

            main_joueur.append(
                paquet.pop()
            )


            # Deux cartes croupier

            main_croupier.append(
                paquet.pop()
            )

            main_croupier.append(
                paquet.pop()
            )


            # Initialement il n'y a
            # qu'une seule main joueur

            mains_joueur = [
                main_joueur
            ]

            mises_joueur = [
                mise
            ]

            main_actuelle = 0

            split_actif = False


            partie_en_cours = True

            croupier_visible = False


            message_info = (
                "À vous : T = tirer | R = rester | S = split"
            )


            score_joueur = calculer_score(
                main_joueur
            )

            score_croupier = calculer_score(
                main_croupier
            )


            # Blackjack dès le départ

            if (
                score_joueur == 21
                or score_croupier == 21
            ):

                croupier_visible = True

                partie_en_cours = False


                jetons, message_info = terminer_manche(
                    paquet,
                    main_croupier,
                    mains_joueur,
                    mises_joueur,
                    jetons
                )


                if partie_terminee(
                    jetons
                ):

                    message_info = (
                        "Vous avez perdu ! "
                        "Vous n'avez plus assez de jetons."
                    )


    # --------------------------------------------------
    # SPLIT
    # --------------------------------------------------

    elif (
        action == "split"
        and partie_en_cours
    ):

        # Un seul split autorisé pour l'instant

        if split_actif:

            message_info = (
                "Vous avez déjà effectué un split."
            )


        # Vérifier les deux cartes

        elif not split_possible(
            main_joueur
        ):

            message_info = (
                "Split impossible : "
                "les deux cartes doivent être identiques."
            )


        # Un split représente deux mises de 100.
        # Il faut donc pouvoir risquer 200 jetons.

        elif jetons < mise * 2:

            message_info = (
                "Vous n'avez pas assez de jetons "
                "pour effectuer un split."
            )


        else:

            mains_joueur = effectuer_split(
                main_joueur,
                paquet
            )


            mises_joueur = [
                mise,
                mise
            ]


            split_actif = True

            main_actuelle = 0


            # On commence par jouer
            # la première main.

            main_joueur = mains_joueur[
                main_actuelle
            ]


            message_info = (
                "Split effectué ! "
                "Vous jouez la main 1."
            )


    # --------------------------------------------------
    # TIRER
    # --------------------------------------------------

    elif (
        action == "tirer"
        and partie_en_cours
    ):

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


        # ----------------------------------------------
        # DÉPASSEMENT DE 21
        # ----------------------------------------------

        if score_joueur > 21:


            # Si on joue la première main du split,
            # on passe simplement à la deuxième.

            if (
                split_actif
                and main_actuelle == 0
            ):

                main_actuelle = 1

                main_joueur = mains_joueur[
                    main_actuelle
                ]


                message_info = (
                    "Main 1 dépasse 21. "
                    "Vous jouez maintenant la main 2."
                )


            else:

                # Toutes les mains ont été jouées.

                croupier_visible = True

                partie_en_cours = False


                jetons, message_info = terminer_manche(
                    paquet,
                    main_croupier,
                    mains_joueur,
                    mises_joueur,
                    jetons
                )


                if partie_terminee(
                    jetons
                ):

                    message_info = (
                        "Vous avez perdu ! "
                        "Vous n'avez plus assez de jetons."
                    )


        # ----------------------------------------------
        # SCORE = 21
        # ----------------------------------------------

        elif score_joueur == 21:

            message_info = (
                "Vous avez 21 ! "
                "Appuyez sur R pour rester."
            )


    # --------------------------------------------------
    # RESTER
    # --------------------------------------------------

    elif (
        action == "rester"
        and partie_en_cours
    ):


        # Si nous avons fait un split
        # et que nous sommes sur Main 1...

        if (
            split_actif
            and main_actuelle == 0
        ):

            main_actuelle = 1


            main_joueur = mains_joueur[
                main_actuelle
            ]


            message_info = (
                "Main 1 terminée. "
                "Vous jouez maintenant la main 2."
            )


        else:

            # Plus aucune main à jouer :
            # le croupier peut jouer.

            croupier_visible = True

            partie_en_cours = False


            jetons, message_info = terminer_manche(
                paquet,
                main_croupier,
                mains_joueur,
                mises_joueur,
                jetons
            )


            if partie_terminee(
                jetons
            ):

                message_info = (
                    "Vous avez perdu ! "
                    "Vous n'avez plus assez de jetons."
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
    # JETONS
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
    # CARTES CROUPIER
    # --------------------------------------------------

    for i, carte in enumerate(
        main_croupier
    ):

        x = 150 + i * 105

        y = 125


        if (
            i == 1
            and not croupier_visible
        ):

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
    # SCORE CROUPIER
    # --------------------------------------------------

    if len(
        main_croupier
    ) > 0:

        if croupier_visible:

            score_croupier = calculer_score(
                main_croupier
            )

            texte_score_croupier = police_texte.render(
                "Score : "
                + str(score_croupier),
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


    if split_actif:

        nom_main = (
            "Cartes du joueur - Main "
            + str(main_actuelle + 1)
        )

    else:

        nom_main = (
            "Cartes du joueur"
        )


    texte_joueur = police_texte.render(
        nom_main,
        True,
        BLANC
    )


    fenetre.blit(
        texte_joueur,
        (120, 335)
    )


    # --------------------------------------------------
    # CARTES JOUEUR
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
    # SCORE JOUEUR
    # --------------------------------------------------

    if len(
        main_joueur
    ) > 0:

        score_joueur = calculer_score(
            main_joueur
        )


        texte_score_joueur = police_texte.render(
            "Score : "
            + str(score_joueur),
            True,
            BLANC
        )


        fenetre.blit(
            texte_score_joueur,
            (750, 335)
        )


    # --------------------------------------------------
    # INFORMATIONS
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


    # --------------------------------------------------
    # BOUTON SPLIT
    # --------------------------------------------------

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
