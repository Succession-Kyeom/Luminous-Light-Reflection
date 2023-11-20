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
clear = False

#빛 설정
light = Light(position=[700, 800])

light.lightPositionX = 400
light.lightPositionY = 600

lightSprite = pygame.sprite.Group()
lightSprite.add(light)

goal = Goal()
allSprites = pygame.sprite.Group()
allSprites.add(goal)

start = Start(position=[1500, 800])
startSprites = pygame.sprite.Group()
startSprites.add(start)

#핀 생성
pinPositionX = 300
pinPositionY = 500
pin = Button(position=(pinPositionX, pinPositionY))
pinSprites = pygame.sprite.Group()
pinSprites.add(pin)

screen.fill("BLACK")  #화면 채우기

while not done:
    clock.tick(60)  # 프레임 설정

    for event in pygame.event.get(): #유저가 이벤트를 발생 시킬 떄
        if event.type == pygame.QUIT: #종료를 누르면
            done = True  #종료하여 루프 탈출
        else:
            pin.click(event)
            pin.update()
            start.click(event)
            start.update()
            if pin.isClick != 0: #화면 재설정
                screen.fill("BLACK")
            elif start.isClick != 0:
                screen.fill("BLACK")

    #빛이 벽과 충돌할 때
    if light.circle.colliderect(pin):
        if pin.index == 1 or pin.index == 2:
            light.crash(pin.index)

    #빛 골과 충돌할 때
    if light.circle.colliderect(goal):
        clear = True

    #빛 출발 신호 받았을 때
    if start.start == True:
        if light.lightWay == light.vertical:
            light.lightPositionY += light.lightDy
        else:
            light.lightPositionX += light.lightDx

    startSprites.draw(screen)
    allSprites.draw(screen)
    pinSprites.draw(screen)
    screen.blit(light.image, (light.lightPositionX, light.lightPositionY))
    pygame.display.flip() #화면 전체 업데이트

pygame.quit()

# https://velog.io/@whdnjsdyd111/python-library-pygame-1.-%EA%B0%9C%EC%9A%94