#taken from a previous project
from turtle import Screen
import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Project")

BG = pygame.image.load("WildWest.png")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 150

PLAYER_VEL = 5

def draw(sprite, x, y): 

    WIN.blit(sprite, (x, y))


     
def main():
    run = True

    player = pygame.image.load("Clint.png")
    player_x = 425
    player_y = HEIGHT-PLAYER_HEIGHT
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:

           player_x -= PLAYER_VEL

        if keys[pygame.K_RIGHT]:
           player_x += PLAYER_VEL

        if keys[pygame.K_UP]:
            player_y -= PLAYER_VEL
            
        if keys[pygame.K_DOWN]:
            player_y += PLAYER_VEL
        draw(sprite=BG, x=0, y=0)
        draw(sprite=player, x=player_x, y=player_y)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()