import pygame

def afficher(points):
    # Initialisation de Pygame
    pygame.init()

    # Taille de la fenêtre
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Visu3d")

    # Boucle principale
    continuer = True
    clock = pygame.time.Clock()

    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
        
        for point in points:
            pygame.draw.rect(screen, point[2], (point[0]*100, point[1], 10, 10))


        # Met à jour l'écran
        pygame.display.flip()
        clock.tick(30)  # Limite à 30 FPS

    pygame.quit()
