import pygame

pygame.init()
screen = pygame.display.set_mode((700, 361))
clock = pygame.time.Clock()
background_image = pygame.image.load("background.png")

while True:
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)