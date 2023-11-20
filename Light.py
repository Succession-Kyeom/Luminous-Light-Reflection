import pygame

class Light(pygame.sprite.Sprite):
    def __init__(self, position):  # 클래스 초기화
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.image.load('image/Light.png')  # 골 이미지 정의
        self.image = pygame.transform.scale(self.image, (10, 10))  # 크기 조절
        self.rect = self.image.get_rect()  # 스프라이트 그리기
        self.rect.centerx = self.get_size()[0] // 2
        self.rect.centery = self.get_size()[1] // 2
        #lightPositionX = self.get_size()[0] // 2
        #lightPositionY = self.get_size()[1] // 2