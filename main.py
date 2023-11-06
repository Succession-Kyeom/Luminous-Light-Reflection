import pygame

pygame.init()

size = (1920, 1080) #화면 크기 변수
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Luminous : Light Reflection") #창 이름
clock = pygame.time.Clock() #프레임 설정 변수

done = False #종료 여부 변수

startReflection = pygame.image.load("image/StartReflection.png")
#startReflection = pygame.transform.scale(startReflection, (396, 87))

quit = pygame.image.load("image/Quit.png")

while not done:
    clock.tick(60)  # 프레임 설정

    for event in pygame.event.get(): #유저가 이벤트를 발생 시킬 떄
        if event.type == pygame.QUIT: #종료를 누르면
            done = True  #종료하여 루프 탈출

    screen.fill("DARK GRAY")  #화면 채우기

    #start = pygame.Rect(startReflection.get_rect())

    screen.blit(startReflection, (size[0] // 2, size[1] // 2))
    screen.blit(quit, ())

    pygame.display.flip() #화면 전체 업데이트

pygame.quit()

# https://velog.io/@whdnjsdyd111/python-library-pygame-1.-%EA%B0%9C%EC%9A%94