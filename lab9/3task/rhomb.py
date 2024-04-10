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
 
def calculate_rect(x1, y1, x2, y2, x3, y3, x4, y4):
    #return ((x1, y1), (x1+x2, y1+y2), (x1+x2+x3, y2))
    return ((x1, y1), (x1+x2, y1+y2), (x1+x3, y1+y2), (x1, y1+y4))
     
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
                prevX = event.pos[0] 
                prevY = event.pos[1] 
                midx = event.pos[0] 
                midy = event.pos[1] 
                mid1x = event.pos[0] 
                mid1y = event.pos[1] 
                currX = event.pos[0] 
                currY = event.pos[1] 
                #pygame.draw.rect(screen, colorRed, calculate_rect(prevX, prevY, currX, currY), Thickness)
                pygame.draw.polygon(screen, colorRed, ((prevX, prevY), (abs(prevX - currX), prevY + currY), (prevX, prevY + currY * 2), (prevX + currX, prevY + currY)), Thickness) 
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: 
            print("LMB released") 
            LMBpressed = False 
            prevX = event.pos[0] 
            prevY = event.pos[1] 
            midx = event.pos[0] 
            midy = event.pos[1] 
            currX = event.pos[0] 
            currY = event.pos[1] 
            pygame.draw.polygon(screen, colorRed, ((prevX, prevY), (abs(prevX - currX), prevY + currY), (prevX, prevY + currY * 2), (prevX + currX, prevY + currY)), Thickness)
            #pygame.draw.rect(screen, colorRed, calculate_rect(prevX, prevY, currX, currY), Thickness)
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