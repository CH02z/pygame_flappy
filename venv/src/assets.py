import os
import pygame

sprites = {}

def load_sprites():
    path = os.path.join("assets", "graphics")
    print(path)
    for file in os.listdir(path):
        print(file)
        if file.lower().lower().endswith(('.png', '.jpg', '.jpeg')):
            print(os.path.join(path, file))
            sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def get_sprite(name):
    return sprites[name]