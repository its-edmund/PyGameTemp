import pygame
import sys

WIDTH = 800
HEIGHT = 600

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

class Player(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Bit Attack')
clock = pygame.time.Clock()

killed = False

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while not killed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            killed = True

        print(event)

    # update
    # all_sprites.update()

    # draw
    screen.fill((255,0,0))
    # all_sprites.draw(screen)

    # update display
    pygame.display.update()

    # tick time
    clock.tick(60)


pygame.quit()
quit()
