import pygame

pygame.init()

WHIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WHIDTH, HEIGHT))
base_layer = pygame.Surface((WHIDTH, HEIGHT))

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

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

done = False

while not done:
    for event in pygame.event.get():
        if LMBpressed: #for filling with black 
            screen.blit(base_layer, (0, 0)) 
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            print("position of mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                pygame.draw.rect(screen, colorRed, calculate_rect(prevX, prevY, currX, currY), Thickness)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            pygame.draw.rect(screen, colorRed, calculate_rect(prevX, prevY, currX, currY), Thickness)
            base_layer.blit(screen, (0,0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                Thickness +=1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                Thickness -=1
    
    pygame.display.flip()
    clock.tick(60)

    
