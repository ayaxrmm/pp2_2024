import pygame
from datetime import datetime

pygame.init()
run = True
clock = pygame.time.Clock()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))

image_clock = pygame.image.load('main-clock.png')
left_hand = pygame.image.load('left-hand.png')
right_hand = pygame.image.load('right-hand.png')
rect = image_clock.get_rect(center=(width//2, height//2))

while run:
    screen.blit(image_clock, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    time = datetime.now().time()

    left_angle = -(time.second *6)
    rotate_left = pygame.transform.rotate(left_hand, left_angle)
    left_rect = rotate_left.get_rect(center = rect.center)
    screen.blit(rotate_left, left_rect.topleft)

    right_angle = -(time.minute * 6)
    rotate_right = pygame.transform.rotate(right_hand, right_angle)
    right_rect = rotate_right.get_rect(center = rect.center)
    screen.blit(rotate_right, right_rect.topleft)
    pygame.display.flip()
    clock.tick(60)