import pygame
import time
import random
from object import*

pygame.init()
bg_size = [800, 600]
move_size = [770,570]
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("mySecondGame")
clock = pygame.time.Clock()

bg = Object('./Asset1_ball/space800_800.jpg',0,0)
coin = Object('./Asset1_ball/coin.png', 400, 300)
p1 = Player('./Asset1_ball/sprite1.png',100,150,0,move_size)
p2 = Player('./Asset1_ball/sprite2.png',300,150,0,move_size)
rock_list = []
for i in range(0,8):
    rock = Rock('./Asset1_ball/rock.png', 60,60,[bg_size[0]+100,bg_size[1]+100])
    rock_list.append(rock)
running = True
while running:
    clock.tick(30)
    bg.blit_me(screen)
    coin.blit_me(screen)
    p1.checkUserControl(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    p2.checkUserControl(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    p1.checkCollisionCoin(coin)
    p2.checkCollisionCoin(coin)
    p1.checkCollideOther(p2)
    for t in range(len(rock_list)):
        p1.checkCollideRock(rock_list[t])
        p2.checkCollideRock(rock_list[t])
    for  j in range(len(rock_list)):
        rock_list[j].move()
        rock_list[j].blit_me(screen)
    p1.blit_me(screen)
    p2.blit_me(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()


