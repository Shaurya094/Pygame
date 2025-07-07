import pygame

pygame.init()
width, height = 500, 500

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Adding image and background image")

bg = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (width, height))
penguin = pygame.transform.scale(
    pygame.image.load('hello penguin.png').convert_alpha(), (200, 200))
penguin_rect = penguin.get_rect(center = (width // 2, 
                                          height // 2 - 30))
text = pygame.font.Font(None, 36).render('Hello World ', True, 
                                         pygame.Color('black'))
text_rect = text.get_rect(center = (width // 2, height //2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.quit():
              running = False

    display.blit(bg, (0,0))
    display.blit(penguin, penguin_rect)
    display.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()

if __name__ == '__main__':
 game_loop()