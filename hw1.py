import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game screen")


size = 200
blue = (0, 0, 255)


square_rect = pygame.Rect(0, 0, size, size)
square_rect.center = screen.get_rect().center

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((30, 30, 30))


    pygame.draw.rect(screen, blue, square_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
