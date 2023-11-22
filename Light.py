import pygame


class Light(pygame.sprite.Sprite):
    def __init__(self, position):  # 클래스 초기화
        # 스프라이트 초기화
        pygame.sprite.Sprite.__init__(self)

        # 빛 이미지 설정
        self.image = pygame.image.load('image/Light.png').convert_alpha()

        # 크기 조절
        self.image = pygame.transform.scale(self.image, (10, 10))

        # 스프라이트 그리기
        self.rect = self.image.get_rect()

        # 빛 좌표
        self.lightPositionX = self.rect.centerx = position[0]
        self.lightPositionY = self.rect.centery = position[1]

        # 빛 속도값
        self.speed = 1
        self.lightDx = self.speed
        self.lightDy = -1 * self.speed

        # 빛 이동 방향
        self.vertical = True
        self.horizon = False
        self.lightWay = self.vertical

        # 거울 충돌 감지
        self.isCrash = False

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.centerx = self.lightPositionX
        self.rect.centery = self.lightPositionY

        if self.isCrash == True:
            if self.lightWay == self.vertical:
                self.lightWay = self.horizon

            else:
                self.lightWay = self.vertical

    def crash(self, index):
        if self.lightWay == self.vertical:
            self.lightWay = self.horizon
            if index == 1:  # /과 충돌
                if self.lightDy > 0:
                    self.lightDx = -1 * self.speed
                else:
                    self.lightDx = self.speed
            elif index == 2:  # \과 충돌
                if self.lightDy > 0:
                    self.lightDx = self.speed
                else:
                    self.lightDx = -1 * self.speed
            self.lightDy = 0

        else:
            self.lightWay = self.vertical
            if index == 1:  # /과 충돌
                if self.lightDx > 0:
                    self.lightDy = -1 * self.speed
                else:
                    self.lightDy = self.speed
            elif index == 2:  # \과 충돌
                if self.lightDx > 0:
                    self.lightDy = self.speed
                else:
                    self.lightDy = -1 * self.speed
            self.lightDx = 0