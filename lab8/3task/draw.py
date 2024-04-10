import pygame

pygame.init()

WHIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WHIDTH, HEIGHT))

colorRed = (255, 0 ,0)
colorBlue = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False #left mose button is/isn't pressed
Thickness = 5

prevX = 0
prevY = 0

currX = 0
currY = 0
done = False

while not done:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed")
            LMBpressed = True
            currX = event.pos[0]
            currY = event.pos[0]
            prevX = event.pos[0]
            prevY = event.pos[0]
        if event.type == pygame.MOUSEMOTION:
            print("position of mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released")
            LMBpressed = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                Thickness +=1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                Thickness -=1
    pygame.draw.line(screen, colorRed, (prevX, prevY), (currX, currY), Thickness)

    prevX = currX
    prevY = currY
    
    pygame.display.flip()
    clock.tick(60)