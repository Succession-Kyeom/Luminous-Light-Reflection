import pygame

class Light(pygame.sprite.Sprite):
    def __init__(self, position):  # 클래스 초기화
        #스프라이트 초기화
        pygame.sprite.Sprite.__init__(self)

        #빛 이미지 설정
        self.image = pygame.image.load('image/Light.png')

        #크기 조절
        self.image = pygame.transform.scale(self.image, (10, 10))

        #스프라이트 그리기
        self.rect = self.image.get_rect()

        #빛 좌표
        self.lightPositionX = self.rect.centerx = self.rect.x // 2
        self.lightPositionY = self.rect.centery = self.rect.y // 2

        #빛 속도값
        self.speed = 5
        self.lightDx = self.speed
        self.lightDy = self.speed

        #빛 이동 방향
        self.vertical = True
        self.horizon = False
        self.lightWay = self.horizon

        #벽 충돌 감지
        self.crash = False

        if self.crash == True:
            if self.lightWay == self.vertical:
                self.lightWay = self.horizon

            else:
                self.lightWay = self.vertical

    def crash(self, index):
        if self.lightWay == self.vertical:
            self.lightWay = self.horizon
            if index == 1:  # /과 충돌
                self.lightDx = -1 * self.speed
            elif index == 2:  # \과 충돌
                self.lightDx = self.speed
        else:
            self.lightWay = self.vertical
            if index == 1:  # /과 충돌
                self.lightDy = self.speed
            elif index == 2:  # \과 충돌
                self.lightDy = -1 * self.speed