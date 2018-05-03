import pygame
import time
import random
from object import*

pygame.init()
screen = pygame.display.set_mode([400, 240])
pygame.display.set_caption("mySecondGame")
clock = pygame.time.Clock()

bg = Object('./Asset1_ball/bg.png',0,0)
coin = Object('./Asset1_ball/coin.png', 200, 50)
p1 = Player('./Asset1_ball/sprite1.png',100,150,0)

running = True
while running:
    clock.tick(30)
    bg.blit_me(screen)
    coin.blit_me(screen)
    p1.checkUserControl(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    p1.blit_me(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()


