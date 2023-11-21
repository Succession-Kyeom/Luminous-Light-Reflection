import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, position): #클래스 초기화
        pygame.sprite.Sprite.__init__(self) #스프라이트 초기화
        self.image = pygame.image.load('image/Goal.png') #골 이미지 정의
        self.image = pygame.transform.scale(self.image, (100, 100)) #크기 조절
        self.rect = self.image.get_rect() #스프라이트 그리기

        self.goalPositionX = self.rect.centerx = self.rect.x // 2
        self.goalPositionY = self.rect.centery = self.rect.y // 2