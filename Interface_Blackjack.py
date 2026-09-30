import pygame #this just imports pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
LARGEUR = 1000
HAUTEUR = 650
#i can modify this just by changing the numbers

# Création de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

# Titre de la fenêtre
pygame.display.set_caption("Table de Blackjack")

# colours in my program that i will call throughout 
VERT = (0, 120, 0)
VERT_FONCE = (0, 80, 0)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (200, 200, 200)
#google colour codes to know which colour

# POLICES
police_titre = pygame.font.Font(None, 40)
police_texte = pygame.font.Font(None, 30)

#and now we create the different zones of the background
#rect creates a rectangle
#the four numbers represent x, y, largeur, hauteur

zone_croupier = pygame.Rect(100, 80, 800, 180)
zone_joueur = pygame.Rect(100, 320, 800, 180)
zone_info = pygame.Rect(350, 520, 300, 50)


#these are to create our buttons
bouton_tirer = pygame.Rect(300, 600, 150, 50)

bouton_rester = pygame.Rect(550, 600, 150, 50)



# Variable qui permet de garder la fenêtre ouverte
jeu_en_cours = True

"""This creates a variable called jeu_en_cours.
At the beginning, it is set to: True
which means:
Yes, the game is still running.
"""
    

"""A while loop means:
Repeat this code again and again as long as the condition is true.
"""
while jeu_en_cours:
   
    # Gestion des événements -- Pygame constantly checks if the user has done something.
    for evenement in pygame.event.get():

        # Si l'utilisateur clique sur la croix
        if evenement.type == pygame.QUIT:
            jeu_en_cours = False

    # Remplir la fenêtre avec la couleur verte
    fenetre.fill(VERT)
    titre = police_titre.render("BLACKJACK", True, BLANC)
    fenetre.blit(titre, (400, 20))
    
    
    # ZONE DU CROUPIER
    pygame.draw.rect(fenetre,VERT_FONCE,zone_croupier,3)

    texte_croupier = police_texte.render("Cartes du croupier",True,BLANC)

    fenetre.blit(texte_croupier,(120, 95))
    
    # ZONE DU JOUEUR
    pygame.draw.rect(fenetre,VERT_FONCE,zone_joueur,3)

    texte_joueur = police_texte.render("Cartes du joueur",True,BLANC)

    fenetre.blit(texte_joueur,(120, 335))


    # INFORMATIONS DE LA PARTIE
    pygame.draw.rect(fenetre,VERT_FONCE,zone_info)

    texte_infos = police_texte.render("Informations de la partie",True,BLANC)

    fenetre.blit(texte_infos,(370, 535))


    # BOUTON TIRER
    pygame.draw.rect(fenetre,GRIS,bouton_tirer)

    texte_tirer = police_texte.render("TIRER",True,NOIR)

    fenetre.blit(texte_tirer,(340, 615))


    # BOUTON RESTER
    pygame.draw.rect(fenetre,GRIS,bouton_rester)

    texte_rester = police_texte.render("RESTER",True,NOIR)

    fenetre.blit(texte_rester,(580, 615))
    
    
    
    # Mettre à jour l'affichage
    pygame.display.update()

# Fermer correctement Pygame
pygame.quit()

