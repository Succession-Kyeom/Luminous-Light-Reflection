import pygame

pygame.init()

size = [960, 540] #화면 크기 변수
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Luminous : Light Reflection") #창 이름

done = False #종료 여부 변수

clock = pygame.time.Clock() #프레임 설정 변수

while not done:
    clock.tick(60)  # 프레임 설정

    for event in pygame.event.get(): #유저가 이벤트를 발생 시킬 떄
        if event.type == pygame.QUIT: #종료를 누르면
            done = True  #종료하여 루프 탈출

    screen.fill("WHITE")  #화면 채우기

    pygame.display.flip() #화면 업데이트

pygame.quit()