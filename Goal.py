import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, position): #클래스 초기화
        pygame.sprite.Sprite.__init__(self) #스프라이트 초기화
        self.image = pygame.image.load('image/Goal.png') #골 이미지 정의
        self.rect = pygame.Rect(position, (40, 40)) #스프라이트 그리기
        self.image = pygame.transform.scale(self.image, (40, 40))  # 크기 조절

        self.rect.centerx = self.rect.x + 20
        self.rect.centery = self.rect.y + 20
        self.isClick = 0
        self.index = -1

    def click(self, event):
        return