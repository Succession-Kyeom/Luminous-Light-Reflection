import pygame

class MySprite(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def check_collision(sprite1, sprite2):
        return pygame.sprite.collide_rect(sprite1, sprite2)