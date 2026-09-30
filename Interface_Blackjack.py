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

# Couleur de fond : vert
VERT = (0, 120, 0)
#google colour codes to know which colour


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

    # Mettre à jour l'affichage
    pygame.display.update()

# Fermer correctement Pygame
pygame.quit()
