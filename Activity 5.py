import pygame

def main():
    pygame.init()
    width, height = 500, 500
    screen = pygame.display.set_mode(width, height)
    pygame.display.set_caption('color changing sprite')

    colours = {
        'red': pygame.color('red'),
        'green': pygame.color('green'),
        'blue': pygame.color('blue'),
        'white': pygame.color('white'),
        'yellow': pygame.color('yellow')
    }
    crnt = colours['white']
    x, y = 30, 30
    sp_w, sp_h = 60, 60
    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        p = pygame.key.get_pressed()
        if p[pygame.K_LEFT]: x -= 3
        if p[pygame.K_RIGHT]: x += 3
        if p[pygame.K_UP]: y -= 3
        if p[pygame.K_DOWN]: y += 3

        x = min(max(0, x), width - sp_w)
        y = min(max(0, y), height - sp_h)

        if x == 0: crnt = colours['blue']
        elif x == width - sp_w: crnt = colours['yellow']
        elif y == 0: crnt = colours['red']
        elif y == height - sp_h:
            crnt = colours['green']
        else:
            crnt = colours['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, crnt,
                         x, y, sp_w, sp_h)
        pygame.display.flip()
        clock.tick(90)
    
    pygame.quit()

if __name__ == "__main__":
    main()