import pygame


# --------------------------------------------------
# DIMENSIONS DE LA FENÊTRE
# --------------------------------------------------

LARGEUR = 1000
HAUTEUR = 650


# --------------------------------------------------
# COULEURS
# --------------------------------------------------

VERT = (0, 120, 0)
VERT_FONCE = (0, 80, 0)

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

GRIS = (200, 200, 200)


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
# POLICES
# --------------------------------------------------

def creer_polices():

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

    return (
        police_titre,
        police_texte,
        police_info
    )


# --------------------------------------------------
# ACTIONS DU CLAVIER
# --------------------------------------------------

def obtenir_action_clavier(touche):

    if touche == pygame.K_d:

        return "distribuer"

    elif touche == pygame.K_t:

        return "tirer"

    elif touche == pygame.K_r:

        return "rester"

    elif touche == pygame.K_s:

        return "split"

    else:

        return None


# --------------------------------------------------
# ACTIONS DE LA SOURIS
# --------------------------------------------------

def obtenir_action_souris(position):

    if bouton_distribuer.collidepoint(
        position
    ):

        return "distribuer"


    elif bouton_tirer.collidepoint(
        position
    ):

        return "tirer"


    elif bouton_rester.collidepoint(
        position
    ):

        return "rester"


    elif bouton_split.collidepoint(
        position
    ):

        return "split"


    else:

        return None


# --------------------------------------------------
# AFFICHAGE D'UN BOUTON
# --------------------------------------------------

def afficher_bouton(
    fenetre,
    bouton,
    texte,
    police
):

    pygame.draw.rect(
        fenetre,
        GRIS,
        bouton
    )


    texte_bouton = police.render(
        texte,
        True,
        NOIR
    )


    fenetre.blit(
        texte_bouton,
        texte_bouton.get_rect(
            center=bouton.center
        )
    )


# --------------------------------------------------
# AFFICHAGE DE L'INTERFACE
# --------------------------------------------------

def dessiner_interface(
    fenetre,
    police_titre,
    police_texte,
    police_info,
    jetons,
    message_info,
    nom_main
):

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
    # ZONE JOUEUR
    # --------------------------------------------------

    pygame.draw.rect(
        fenetre,
        VERT_FONCE,
        zone_joueur,
        3
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
    # ZONE INFORMATIONS
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
    # BOUTONS
    # --------------------------------------------------

    afficher_bouton(
        fenetre,
        bouton_distribuer,
        "DISTRIBUER",
        police_texte
    )


    afficher_bouton(
        fenetre,
        bouton_tirer,
        "TIRER",
        police_texte
    )


    afficher_bouton(
        fenetre,
        bouton_rester,
        "RESTER",
        police_texte
    )


    afficher_bouton(
        fenetre,
        bouton_split,
        "SPLIT",
        police_texte
    )
