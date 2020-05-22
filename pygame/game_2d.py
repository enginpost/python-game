""" Game in 2D """
import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.display.flip()

pygame.quit()
# game ends here -sm
