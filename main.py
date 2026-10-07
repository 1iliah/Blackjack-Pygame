import pygame
import random

# INITIALISATION DE PYGAME

pygame.init()

# Dimensions de la fenêtre
LARGEUR = 1000
HAUTEUR = 650

# Création de la fenêtre et titre de la fenetre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Table de Blackjack")


# COULEURS - these get called later in the project when we need to use colors 

VERT = (0, 120, 0)
VERT_FONCE = (0, 80, 0)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (200, 200, 200)


# POLICESn- again get called later in the project when needed 

police_titre = pygame.font.Font(None, 40)
police_texte = pygame.font.Font(None, 30)
police_info = pygame.font.Font(None, 22)


# CARTES RAFIK IMPORT 

cartes = [

    # Piques
    ("As", "Pique", [1, 11]),
    ("2", "Pique", 2),
    ("3", "Pique", 3),
    ("4", "Pique", 4),
    ("5", "Pique", 5),
    ("6", "Pique", 6),
    ("7", "Pique", 7),
    ("8", "Pique", 8),
    ("9", "Pique", 9),
    ("10", "Pique", 10),
    ("valet", "Pique", 10),
    ("dame", "Pique", 10),
    ("roi", "Pique", 10),

    # Coeurs
    ("As", "coeur", [1, 11]),
    ("2", "coeur", 2),
    ("3", "coeur", 3),
    ("4", "coeur", 4),
    ("5", "coeur", 5),
    ("6", "coeur", 6),
    ("7", "coeur", 7),
    ("8", "coeur", 8),
    ("9", "coeur", 9),
    ("10", "coeur", 10),
    ("valet", "coeur", 10),
    ("dame", "coeur", 10),
    ("roi", "coeur", 10),

    # Carreaux
    ("As", "carreau", [1, 11]),
    ("2", "carreau", 2),
    ("3", "carreau", 3),
    ("4", "carreau", 4),
    ("5", "carreau", 5),
    ("6", "carreau", 6),
    ("7", "carreau", 7),
    ("8", "carreau", 8),
    ("9", "carreau", 9),
    ("10", "carreau", 10),
    ("valet", "carreau", 10),
    ("dame", "carreau", 10),
    ("roi", "carreau", 10),

    # Trèfles
    ("As", "Trèfle", [1, 11]),
    ("2", "Trèfle", 2),
    ("3", "Trèfle", 3),
    ("4", "Trèfle", 4),
    ("5", "Trèfle", 5),
    ("6", "Trèfle", 6),
    ("7", "Trèfle", 7),
    ("8", "Trèfle", 8),
    ("9", "Trèfle", 9),
    ("10", "Trèfle", 10),
    ("valet", "Trèfle", 10),
    ("dame", "Trèfle", 10),
    ("roi", "Trèfle", 10)
]


# FONCTIONS DU JEU

"""
Pendant la partie, on enlève des cartes du paquet avec pop().
Si je n’avais pas fait de copie, je modifierais directement la liste originale de Rafik.
Avec copy(), je peux utiliser et vider le paquet pendant une partie,
puis recréer un nouveau paquet complet pour la partie suivante.


pop() sert à retirer un élément d’une liste et à le récupérer en même temps.

"""

def creer_paquet():

    # Copie les 52 cartes de Rafik
    paquet = cartes.copy()

    # On mélange le paquet
    random.shuffle(paquet)

    return paquet


"""
Add up all the cards.
Count Aces as 11 first.
If that makes the score go over 21, change an As from 11 to 1.
"""

def calculer_score(main):

    total = 0
    nombre_as = 0

    for carte in main:

        valeur = carte[2]
        # remember it starts counting from 0, so 2 is actually the third element 

        # Si c'est un As
        if isinstance(valeur, list): #if this card has a list as its value, then it must be an As, so handle it differently

            # On commence par considérer l'As comme 11
            total += 11
            nombre_as += 1

        else:
            total += valeur

    # Si on dépasse 21, un As passe de 11 à 1
    while total > 21 and nombre_as > 0:

        total -= 10
        nombre_as -= 1

    return total


def determiner_gagnant(score_joueur, score_croupier):

    if score_joueur > 21:
        return "Vous avez dépassé 21 : le croupier gagne !"

    elif score_croupier > 21:
        return "Le croupier dépasse 21 : vous gagnez !"

    elif score_joueur > score_croupier:
        return "Vous gagnez !"

    elif score_croupier > score_joueur:
        return "Le croupier gagne !"

    else:
        return "Égalité !"


# ZONES DU JEU

zone_croupier = pygame.Rect(100, 80, 800, 180)
zone_joueur = pygame.Rect(100, 320, 800, 180)

zone_info = pygame.Rect(200, 520, 600, 50)


# BOUTONS

bouton_distribuer = pygame.Rect(70, 590, 170, 50)

bouton_tirer = pygame.Rect(300, 590, 150, 50)

bouton_rester = pygame.Rect(550, 590, 150, 50)


# VARIABLES DE LA PARTIE

paquet = []

main_joueur = []

main_croupier = []

partie_en_cours = False

croupier_visible = False

message_info = "Appuyez sur D ou DISTRIBUER pour commencer"


# BOUCLE PRINCIPALE

jeu_en_cours = True


while jeu_en_cours:

    action = None


    # GESTION DES ÉVÉNEMENTS

    for evenement in pygame.event.get():

        # Fermer la fenêtre
        if evenement.type == pygame.QUIT:
            jeu_en_cours = False


        # CLAVIER

        if evenement.type == pygame.KEYDOWN:

            if evenement.key == pygame.K_d:#when D pressed then
                action = "distribuer"

            elif evenement.key == pygame.K_t:#when T pressed then
                action = "tirer"

            elif evenement.key == pygame.K_r: #when R pressed then
                action = "rester"


        # SOURIS

        if evenement.type == pygame.MOUSEBUTTONDOWN:

            if bouton_distribuer.collidepoint(evenement.pos):
                action = "distribuer"

            elif bouton_tirer.collidepoint(evenement.pos):
                action = "tirer"

            elif bouton_rester.collidepoint(evenement.pos):
                action = "rester"


    # DISTRIBUER / NOUVELLE PARTIE

    if action == "distribuer":

        paquet = creer_paquet()

        main_joueur = []
        main_croupier = []

        # Deux cartes pour le joueur
        main_joueur.append(paquet.pop())
        main_joueur.append(paquet.pop())

        # Deux cartes pour le croupier
        main_croupier.append(paquet.pop())
        main_croupier.append(paquet.pop())

        partie_en_cours = True
        croupier_visible = False

        message_info = "À vous : T = tirer une carte | R = rester"


        # Vérification d'un 21 dès la distribution
        score_joueur = calculer_score(main_joueur)
        score_croupier = calculer_score(main_croupier)

        if score_joueur == 21 or score_croupier == 21:

            croupier_visible = True
            partie_en_cours = False

            message_info = determiner_gagnant(
                score_joueur,
                score_croupier
            )


    # TIRER

    elif action == "tirer" and partie_en_cours:

        nouvelle_carte = paquet.pop()

        main_joueur.append(nouvelle_carte)

        score_joueur = calculer_score(main_joueur)

        message_info = (
            "Vous avez tiré : "
            + nouvelle_carte[0]
            + " de "
            + nouvelle_carte[1].strip()
        )


        # Si le joueur dépasse 21
        if score_joueur > 21:

            croupier_visible = True
            partie_en_cours = False

            score_croupier = calculer_score(
                main_croupier
            )

            message_info = determiner_gagnant(
                score_joueur,
                score_croupier
            )

        elif score_joueur == 21:

            message_info = "Vous avez 21 ! Appuyez sur R pour rester."


    # RESTER

    elif action == "rester" and partie_en_cours:

        croupier_visible = True

        # Le croupier doit tirer jusqu'à 17 minimum
        while calculer_score(main_croupier) < 17:

            main_croupier.append(
                paquet.pop()
            )

        score_joueur = calculer_score(
            main_joueur
        )

        score_croupier = calculer_score(
            main_croupier
        )

        message_info = determiner_gagnant(
            score_joueur,
            score_croupier
        )

        partie_en_cours = False


    # FOND

    fenetre.fill(VERT)


    # TITRE

    titre = police_titre.render(
        "BLACKJACK",
        True,
        BLANC
    )

    fenetre.blit(
        titre,
        (400, 20)
    )


    # ZONE CROUPIER

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


    # AFFICHAGE DES CARTES DU CROUPIER EN TEXTE

    texte_main_croupier = ""

    if len(main_croupier) > 0:

        # Si le croupier doit montrer toutes ses cartes
        if croupier_visible:

            for carte in main_croupier:

                texte_main_croupier += (
                    carte[0]
                    + " de "
                    + carte[1].strip()
                    + "   "
                )

        # Sinon on montre seulement la première carte
        else:

            carte_visible = main_croupier[0]

            texte_main_croupier = (
                carte_visible[0]
                + " de "
                + carte_visible[1].strip()
                + "   |   CARTE CACHEE"
            )


    texte_cartes_croupier = police_info.render(
        texte_main_croupier,
        True,
        BLANC
    )

    fenetre.blit(
        texte_cartes_croupier,
        (150, 160)
    )


    # SCORE DU CROUPIER

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


    # ZONE JOUEUR

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


    # AFFICHAGE DES CARTES DU JOUEUR EN TEXTE

    texte_main_joueur = ""

    for carte in main_joueur:

        texte_main_joueur += (
            carte[0]
            + " de "
            + carte[1].strip()
            + "   "
        )


    texte_cartes_joueur = police_info.render(
        texte_main_joueur,
        True,
        BLANC
    )

    fenetre.blit(
        texte_cartes_joueur,
        (150, 400)
    )


    # SCORE DU JOUEUR

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


    # INFORMATIONS

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


    # BOUTON DISTRIBUER

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


    # BOUTON TIRER

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


    # BOUTON RESTER

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


    # ACTUALISER L'ÉCRAN

    pygame.display.update()


pygame.quit()
