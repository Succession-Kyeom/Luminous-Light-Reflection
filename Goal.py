import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, position): #클래스 초기화
        pygame.sprite.Sprite.__init__(self) #스프라이트 초기화
        self.image = pygame.image.load('image/Goal.png') #골 이미지 정의
        self.rect = pygame.Rect(position, (30, 30)) #스프라이트 그리기
        self.image = pygame.transform.scale(self.image, (30, 30))  # 크기 조절

        self.centerx = self.rect.x + 16
        self.centery = self.rect.y + 16
        self.isClick = 0
        self.index = -1

    def click(self, event):
        return