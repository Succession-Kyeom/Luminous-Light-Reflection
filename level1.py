import pygame

#드래그 기능 클래스
class DraggableObject(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.is_dragging = False
    def update(self):
        if self.is_dragging:
            self.rect.x, self.rect.y = pygame.mouse.get_pos()
            self.rect.x -= self.rect.width // 2
            self.rect.y -= self.rect.height // 2

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_dragging = False

pygame.init()

size = (1920, 1080) #화면 크기 변수
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Luminous : Light Reflection") #창 이름
clock = pygame.time.Clock() #프레임 설정 변수

done = False #종료 여부 변수

#빛 설정
light = pygame.image.load('image/Light.png')
#빛 속도
lightDx = 5
lightDy = 5
# 빛 좌표
lightXPosition = light.get_size()[0] // 2
lightYPosition = light.get_size()[1] // 2

wall = DraggableObject('image/Wall.png', (200, 600))
allSprites = pygame.sprite.Group()
allSprites.add(wall)

screen.fill("BLACK")  # 화면 채우기

while not done:
    clock.tick(60)  # 프레임 설정

    for event in pygame.event.get(): #유저가 이벤트를 발생 시킬 떄
        if event.type == pygame.QUIT: #종료를 누르면
            done = True  #종료하여 루프 탈출
        else:
            wall.handle_event(event)
            allSprites.update()

    lightXPosition += lightDx
    lightYPosition += lightDy

    if lightXPosition <= 1.5 * light.get_size()[0]:
        lightXPosition = 1.5 * light.get_size()[0]
        lightDx = -lightDx
    elif lightXPosition >= size[0] - 2 * light.get_size()[0]:
        lightXPosition = size[0] - 2 * light.get_size()[0]
        lightDx = -lightDx
    if lightYPosition <= 1.5 * light.get_size()[1]:
        lightYPosition = 1.5 * light.get_size()[1]
        lightDy = -lightDy
    elif lightYPosition >= size[1] - 2 * light.get_size()[1]:
        lightYPosition = size[1] - 2 * light.get_size()[1]
        lightDy = -lightDy

    allSprites.draw(screen)
    screen.blit(light, (lightXPosition, lightYPosition))
    pygame.display.flip() #화면 전체 업데이트

pygame.quit()

# https://velog.io/@whdnjsdyd111/python-library-pygame-1.-%EA%B0%9C%EC%9A%94