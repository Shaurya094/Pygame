import pygame

# Initialize Pygame

pygame.init()

# Create a window

screen = pygame.display.set_mode((400, 300))

# Flag to control the game loop

done = False

# Game loop

while not done:

 for event in pygame.event.get():

  if event.type == pygame.QUIT: # Use pygame.QUIT (not pygame.quit())

   done = True

# Fill screen with white color (optional, helps avoid trails)

 screen.fill((255, 255, 255))

# Draw a blue rectangle

 pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))

# Update the display

 pygame.display.flip()