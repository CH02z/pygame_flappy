from assets import get_sprite
import pygame

class Backround(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = get_sprite("backround_complete")
        self.rect = self.image.get_rect(topleft=(0, 0))

        super().__init__(*groups)