import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blue Square with Text")

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

size = 200
square_rect = pygame.Rect(0, 0, size, size)
square_rect.center = screen.get_rect().center

pygame.font.init()
font = pygame.font.SysFont(None, 48) 

text_surf = font.render("Hello!", True, WHITE)
text_rect = text_surf.get_rect(center=square_rect.center)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, BLUE, square_rect)

    screen.blit(text_surf, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()