import pygame
from Button import Button

"""
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
"""


class Goal(pygame.sprite.Sprite):
    def __init__(self): #클래스 초기화
        pygame.sprite.Sprite.__init__(self) #스프라이트 초기화
        self.image = pygame.image.load('image/Goal.png') #골 이미지 정의
        self.image = pygame.transform.scale(self.image, (100, 100)) #크기 조절
        self.rect = self.image.get_rect() #스프라이트 그리기
        self.rect.centerx = goalPositionX
        self.rect.centery = goalPositionY

class Wall(pygame.sprite.Sprite):
    def __init__(self): #클래스 초기화
        pygame.sprite.Sprite.__init__(self) #스프라이트 초기화
        self.image = pygame.image.load('image/wall.png') #골 이미지 정의
        self.image = pygame.transform.scale(self.image, (10, 60)) #크기 조절
        self.rect = self.image.get_rect() #스프라이트 그리기
        self.rect.centerx = wallPositionX
        self.rect.centery = wallPositionY
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

class Light(pygame.sprite.Sprite):
    def __init__(self):  # 클래스 초기화
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.image.load('image/Light.png')  # 골 이미지 정의
        self.image = pygame.transform.scale(self.image, (10, 10))  # 크기 조절
        self.rect = self.image.get_rect()  # 스프라이트 그리기
        self.rect.centerx = lightPositionX
        self.rect.centery = lightPositionY


pygame.init()

size = (1920, 1080) #화면 크기 변수
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Luminous : Light Reflection") #창 이름
clock = pygame.time.Clock() #프레임 설정 변수

done = False #종료 여부 변수
crash = False #충돌 여부 변수

#빛 설정
light = pygame.image.load('image/Light.png')
#빛 속도
lightDx = 5
lightDy = 5
# 빛 좌표
lightPositionX = light.get_size()[0] // 2
lightPositionY = light.get_size()[1] // 2
#빛 이동 방향
vertical = True
horizon = False
lightWay = horizon

goalPositionX = 10
goalPositionY = 20

wallPositionX = 100
wallPositionY = 800

wall = Wall()
wallSprites = pygame.sprite.Group()
wallSprites.add(wall)

goal = Goal()
wallSprites.add(goal)

screen.fill("BLACK")  # 화면 채우기

#핀 생성
pinPositionX = 300
pinPositionY = 500
pin = Button(position=(pinPositionX, pinPositionY))
pinSprites = pygame.sprite.Group()
pinSprites.add(pin)

while not done:
    clock.tick(60)  # 프레임 설정

    for event in pygame.event.get(): #유저가 이벤트를 발생 시킬 떄
        if event.type == pygame.QUIT: #종료를 누르면
            done = True  #종료하여 루프 탈출
        else:
            wall.handle_event(event)
            pin.click(event)
            wallSprites.update()
            pin.update()
            screen.fill("BLACK")

        if event.type == pygame.KEYDOWN: #키를 눌렀을 때
            if event.key == pygame.K_SPACE: #스페이스 바이면
                screen.fill("BLACK")



    if lightWay == vertical:
        lightPositionY += lightDy
    else:
        lightPositionX += lightDx

    if pygame.sprite.collide_rect(wall, goal):
        crash = True

    if crash == True:
        done = True



    if lightPositionX <= 1.5 * light.get_size()[0]:
        lightPositionX = 1.5 * light.get_size()[0]
        lightDx = -lightDx
    elif lightPositionX >= size[0] - 2 * light.get_size()[0]:
        lightPositionX = size[0] - 2 * light.get_size()[0]
        lightDx = -lightDx
    if lightPositionY <= 1.5 * light.get_size()[1]:
        lightPositionY = 1.5 * light.get_size()[1]
        lightDy = -lightDy
    elif lightPositionY >= size[1] - 2 * light.get_size()[1]:
        lightPositionY = size[1] - 2 * light.get_size()[1]
        lightDy = -lightDy

    wallSprites.draw(screen)
    pinSprites.draw(screen)
    screen.blit(light, (lightPositionX, lightPositionY))
    pygame.display.flip() #화면 전체 업데이트

pygame.quit()

# https://velog.io/@whdnjsdyd111/python-library-pygame-1.-%EA%B0%9C%EC%9A%94