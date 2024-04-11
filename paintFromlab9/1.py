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

 
def calculate_et(x1, y1, x2, y2, x3, y3):
    return ((x1, y1), (x1+x2, y1+y2), (x1+x2+x3, y2))
def calculate_rt(x1, y1, x2, y2, x3, y3):
    minx = min(x1, x2, x3)
    miny = min(y1, y2, y3)
    if minx == x1 and miny == y1:
        return ((x1, y1), (x1, y1+y2), (x1 + x3, y1 + y2))
    elif x2 == minx and y2 == miny:
        return ((x1, y1+y2), (x1, y1), (x1 + x3, y1 + y2))
    else:
        return ((x1 + x3, y1 + y2), (x1, y1+y2), (x1, y1))
def calculate_square(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1-x2), abs(x1-x2))

drawshape = "rhomb"  
done = False 
 
while not done: 
    font = pygame.font.SysFont("Verdana", 20)
    text = font.render("if you click r - draw rhomb,", True, colorWHITE)
    text1 = font.render("s - draw square,", True, colorWHITE)
    text2 = font.render("t - draw right triangle,", True, colorWHITE)
    text3 = font.render("e - draw equilateral triangle", True, colorWHITE)
    screen.blit(text, (20, 30))
    screen.blit(text1, (40, 50))
    screen.blit(text2, (60, 70))
    screen.blit(text3, (80, 90))
    for event in pygame.event.get(): 
        if LMBpressed: #for filling with black  
            screen.blit(base_layer, (0, 0))  
        if event.type == pygame.QUIT: 
            done = True 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                drawshape = "rhomb"
            if event.key == pygame.K_s:
                drawshape = "square"
            if event.key == pygame.K_t:
                drawshape = "right_triangle"
            if event.key == pygame.K_e:
                drawshape = "equi_triangle"
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
                currX = event.pos[0] 
                currY = event.pos[1] 
                if drawshape == "equi_triangle":
                    pygame.draw.polygon(screen, colorRed, calculate_et(prevX, prevY, midx, midy, currX, currY), Thickness)
                if drawshape == "right_triangle":
                    pygame.draw.polygon(screen, colorRed, calculate_rt(prevX, prevY, midx, midy, currX, currY), Thickness)
                if drawshape == "square":
                    pygame.draw.rect(screen, colorRed, calculate_square(prevX, prevY, currX, currY), Thickness)
                if drawshape == "rhomb":
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
            if drawshape == "equi_triangle":
                pygame.draw.polygon(screen, colorRed, calculate_et(prevX, prevY, midx, midy, currX, currY), Thickness)
            if drawshape == "right_triangle":
                pygame.draw.polygon(screen, colorRed, calculate_rt(prevX, prevY, midx, midy, currX, currY), Thickness)
            if drawshape == "square":
                pygame.draw.rect(screen, colorRed, calculate_square(prevX, prevY, currX, currY), Thickness)
            if drawshape == "rhomb":
                pygame.draw.polygon(screen, colorRed, ((prevX, prevY), (abs(prevX - currX), prevY + currY), (prevX, prevY + currY * 2), (prevX + currX, prevY + currY)), Thickness)
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