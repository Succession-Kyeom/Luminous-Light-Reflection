import pygame

class Clear(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Clear, self).__init__()

        # 클리어 이미지 설정
        self.image = pygame.image.load('image/Clear.png').convert_alpha()

        # 크기 조절
        self.image = pygame.transform.scale(self.image, (320, 180))

        # 스프라이트 그리기
        self.rect = self.image.get_rect()

        #버튼 중심 좌표
        self.centerx = self.rect.x
        self.centery = self.rect.y

        self.isClick = False

    def click(self, event):
        mouseButton = pygame.mouse.get_pressed()  # 마우스 클릭 리스트 [좌클릭, 휠, 우클릭]
        if event.type != pygame.MOUSEMOTION:  # 마우스 움직임 틱 방지
            if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭
                if self.rect.collidepoint(event.pos):  # 마우스 버튼 충돌 시
                    if mouseButton[0]:  # 클릭 시
                        self.isClick = True

            elif event.type == pygame.MOUSEBUTTONUP:  # 마우스 클릭 해제
                self.isClick = False
        else:
            self.isClick = False