import pygame
from Button import Button
from Light import Light
from Goal import Goal
from Start import Start

pygame.init() #pygame 초기화

size = (1920, 1080) #화면 크기 변수
screen = pygame.display.set_mode(size) #창 크기 설정
pygame.display.set_caption("Luminous : Light Reflection") #창 이름
clock = pygame.time.Clock() #프레임 설정 변수

done = False #종료 여부 변수
clear = False #클리어 여부

blocks = 10

#빛 생성
light = Light(position=[125, 1060])

lightSprite = pygame.sprite.Group()
lightSprite.add(light)

#시작 생성
start = Start(position=[1500, 800])

startSprites = pygame.sprite.Group()
startSprites.add(start)

#핀 생성
pin = []
pinSprites = pygame.sprite.Group()
pinPositionX = 100
pinPositionY = 100
index = 0
for y in range(10):
    pinPositionX = 100
    for x in range(10):
        if x == 9 and y == 2:
            pin.append(Goal(position=(pinPositionX, pinPositionY)))
        else:
            pin.append(Button(position=(pinPositionX, pinPositionY)))
        pinSprites.add(pin[index])
        pinPositionX += 100
        index += 1
    pinPositionY += 100

screen.fill("BLACK")  #화면 채우기

def init():
    index = 0
    pinPositionY = 100
    for y in range(10):
        pinPositionX = 100
        for x in range(10):
            pin[index].__init__([pinPositionX, pinPositionY])
            pinPositionX += 100
            index += 1
        pinPositionY += 100
    light.__init__([125, 1060])
    start.__init__([1500, 800])
    screen.fill("BLACK")

while not done:
    clock.tick(60)  # 프레임 설정

    for event in pygame.event.get(): #유저가 이벤트를 발생 시킬 떄
        if event.type == pygame.QUIT: #종료를 누르면
            done = True  #종료하여 루프 탈출
        else:
            for x in range(len(pin)):
                pin[x].click(event)
                pin[x].update()

                light.update()
                if pin[x].isClick != 0:  # 화면 재설정
                    screen.fill("BLACK")
            start.click(event)
            start.update()
            if start.isClick != 0:
                screen.fill("BLACK")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                init()

    lightRect = light.image.get_rect()

    #빛이 벽과 충돌할 때
    for x in range(len(pin)):
        if pygame.sprite.collide_rect(light, pin[x]):
            if pin[x].index == 1 or pin[x].index == 2:
                print(pin[x].index)
                light.crash(pin[x].index)
                break

    #빛 출발 신호 받았을 때
    if start.start == True:
        if light.lightWay == light.vertical:
            light.lightPositionY += light.lightDy
        else:
            light.lightPositionX += light.lightDx

    pinSprites.draw(screen)
    startSprites.draw(screen)
    screen.blit(light.image, (light.lightPositionX, light.lightPositionY))
    pygame.display.flip() #화면 전체 업데이트

pygame.quit()

# https://velog.io/@whdnjsdyd111/python-library-pygame-1.-%EA%B0%9C%EC%9A%94