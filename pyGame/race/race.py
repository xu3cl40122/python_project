import pygame
import time
from horse import *

pygame.init()
bg_size = [600, 400]
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("mySecondGame")
clock = pygame.time.Clock()
bg = Object('./src/green.png', 0, 0)
horse = Horse("./src/horse_1.png",200,200,bg_size)

running = True
while running:
    clock.tick(30)
    bg.blit_me(screen)
    horse.blit_me(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
