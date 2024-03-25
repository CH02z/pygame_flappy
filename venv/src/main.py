# Example file showing a basic pygame "game loop"
import pygame
import assets

from objects.backround import Backround


#Settings
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
FPS = 60

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

assets.load_sprites()
sprites = pygame.sprite.LayeredUpdates()

Backround(sprites)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("pink")

    sprites.draw(screen)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()