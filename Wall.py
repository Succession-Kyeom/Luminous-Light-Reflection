import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, position, size):  # 클래스 초기화
        # 스프라이트 초기화
        pygame.sprite.Sprite.__init__(self)

        # 벽 이미지 설정
        self.image = pygame.image.load('image/Wall.png').convert_alpha()

        # 크기 조절
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)

        # 스프라이트 그리기
        self.rect = self.image.get_rect()

        # 벽 좌표
        self.rect.centerx = position[0]
        self.rect.centery = position[1]