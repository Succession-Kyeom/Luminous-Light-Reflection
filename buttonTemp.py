import pygame

#image = []

class Button(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Button, self).__init__()

        #이미지들 리스트로 저장
        images = []
        images.append(pygame.image.load('image/Pin.png'))
        images.append(pygame.image.load('image/Wall1.png'))
        images.append(pygame.image.load('image/Wall2.png'))

        size = (100, 100)

        self.rect = pygame.Rect(position, size)

        #Rect와 image 크기 맞추기
        self.images = [pygame.transform.scale(image, size) for image in images]

        self.index = 0
        self.image = images[self.index]

        self.centerx = self.rect.x
        self.centery = self.rect.y

        self.isClick = 0 #0: 클릭X / 1: 좌클릭 / -1: 우클릭

    def update(self):
        if self.isClick == 1:
            self.index += 1

            if self.index >= len(self.images):
                self.index %= len(self.images)
        elif self.isClick == -1:
            self.index -= 1

            if self.index <= -1:
                self.index += len(self.images)
        self.image = self.images[self.index]

    def click(self, event):

        mouseButton = pygame.mouse.get_pressed()
        if event.type != pygame.MOUSEMOTION:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseButton[0]: #좌클릭
                    self.isClick = 1
                elif mouseButton[2]: #우클릭
                    self.isClick = -1
            elif event.type == pygame.MOUSEBUTTONUP:
                self.isClick = 0
        else:
            self.isClick = 0