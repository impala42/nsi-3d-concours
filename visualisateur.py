import pygame
from calcul import *

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visu3d")

# Charger les donnees (pour plus tard : faire un menu où on selectionne le fichier)
data = charger_donnee("data.csv")

# Boucle principale
continuer = True
clock = pygame.time.Clock()
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    
    # On calcule et on affiche
    points = calculer_pos_points(data)
    for point in points:
        pygame.draw.rect(screen, point[2], (point[0]*100, point[1], 10, 10))

    # Met à jour l'écran
    pygame.display.flip()
    clock.tick(30)  # Limite à 30 FPS

pygame.quit()
