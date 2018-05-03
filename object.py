import pygame
import time

class Player():
    def __init__(self, pic, x, y, score):
        self.canvas = pygame.image.load(pic)
        self.canvas.convert()
        self.x = x
        self.y = y
        self.score = score

    def blit_me(self, screen):
        screen.blit(self.canvas, [self.x, self.y])

    def checkUserControl(self, up, down, left, right):
        keys = pygame.key.get_pressed()
        if keys[up]:
            self.y -= 5
        if keys[down]:
            self.y += 5
        if keys[left]:
            self.x -= 5
        if keys[right]:
            self.x += 5

class Object():
    def __init__(self, pic, x, y):
        self.canvas = pygame.image.load(pic)
        self.canvas.convert()
        self.x = x
        self.y = y

    def blit_me(self, screen):
        screen.blit(self.canvas, [self.x, self.y])
