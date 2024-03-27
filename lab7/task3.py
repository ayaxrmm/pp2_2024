import pygame, sys

pygame.init()
run = True
clock = pygame.time.Clock()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))

x = 400
y = 400

while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:                
            if event.key == pygame.K_RIGHT and x+25 < width:
                x+=20
            elif event.key == pygame.K_LEFT and x-25 > 0:
                x-=20
            elif event.key == pygame.K_UP and y+20 < height:
                y-=20
            elif event.key == pygame.K_DOWN and y-20 > 0:
                y+=20
        
    screen.fill((255, 255, 255))
    circle = pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

