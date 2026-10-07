import pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
LARGEUR = 1000
HAUTEUR = 650

# Création de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

# Titre de la fenêtre
pygame.display.set_caption("Table de Blackjack")


# COULEURS
VERT = (0, 120, 0)
VERT_FONCE = (0, 80, 0)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (200, 200, 200)


# POLICES
police_titre = pygame.font.Font(None, 40)
police_texte = pygame.font.Font(None, 30)
police_info = pygame.font.Font(None, 24)


# ZONES
zone_croupier = pygame.Rect(100, 80, 800, 180)
zone_joueur = pygame.Rect(100, 320, 800, 180)

zone_info = pygame.Rect(200, 520, 600, 50)


# BOUTONS
bouton_tirer = pygame.Rect(300, 600, 150, 50)
bouton_rester = pygame.Rect(550, 600, 150, 50)


# Variable qui permet de garder la fenêtre ouverte
jeu_en_cours = True


# Message affiché au départ
message_info = "Appuyez sur T pour TIRER ou R pour RESTER"


# BOUCLE PRINCIPALE
while jeu_en_cours:

    # Gestion des événements
    for evenement in pygame.event.get():

        # Fermer la fenêtre
        if evenement.type == pygame.QUIT:
            jeu_en_cours = False

        # Si une touche du clavier est pressée
        if evenement.type == pygame.KEYDOWN:

            # T = Tirer
            if evenement.key == pygame.K_t:
                message_info = "Vous avez choisi de TIRER une carte"

            # R = Rester
            if evenement.key == pygame.K_r:
                message_info = "Vous avez choisi de RESTER"


    # Fond vert
    fenetre.fill(VERT)


    # TITRE
    titre = police_titre.render(
        "BLACKJACK",
        True,
        BLANC
    )

    fenetre.blit(titre, (400, 20))


    # ZONE DU CROUPIER
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


    # ZONE DU JOUEUR
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


    # INFORMATIONS DE LA PARTIE
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

    fenetre.blit(
        texte_infos,
        (220, 536)
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
        (340, 615)
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
        (580, 615)
    )


    # Mise à jour de l'écran
    pygame.display.update()


# Fermer Pygame
pygame.quit()

