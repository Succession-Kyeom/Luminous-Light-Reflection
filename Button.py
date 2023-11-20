import pygame

#image = []

class Button(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Button, self).__init__()

        #이미지들 리스트로 저장
        images = [] #이미지 [o, /, \]
        images.append(pygame.image.load('image/Pin.png'))
        images.append(pygame.image.load('image/Wall1.png'))
        images.append(pygame.image.load('image/Wall2.png'))

        #사이즈 설정
        size = (100, 100)

        #사각형에 이미지 삽입
        self.rect = pygame.Rect(position, size)

        #Rect와 image 크기 맞추기
        self.images = [pygame.transform.scale(image, size) for image in images]

        self.index = 0
        self.image = images[self.index]

        #버튼 중심 좌표
        self.centerx = self.rect.x
        self.centery = self.rect.y

        self.isClick = 0 #0: 클릭X / 1: 좌클릭 / -1: 우클릭

    def update(self):
        if self.isClick == 1: #좌클릭 시
            self.index += 1 #인덱스 증가
            if self.index >= len(self.images): #인덱스 초과 시
                self.index %= len(self.images) #범윈 내 값 재설정

        elif self.isClick == -1: #우클릭 시
            self.index -= 1 #인덱스 감소
            if self.index <= -1: #인덱스 초과 시
                self.index += len(self.images) #범위 내로 값 재설정

        self.image = self.images[self.index] #이미지 재설정

    def click(self, event):
        mouseButton = pygame.mouse.get_pressed() #마우스 클릭 리스트 [좌클릭, 휠, 우클릭]
        if event.type != pygame.MOUSEMOTION: #마우스 움직임 틱 방지
            if event.type == pygame.MOUSEBUTTONDOWN: #마우스 클릭
                if self.rect.collidepoint(event.pos): #마우스 버튼 충돌 시
                    if mouseButton[0]: #좌클릭
                        self.isClick = 1
                    elif mouseButton[2]: #우클릭
                        self.isClick = -1
            elif event.type == pygame.MOUSEBUTTONUP: #마우스 클릭 해제
                self.isClick = 0
        else:
            self.isClick = 0