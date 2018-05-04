import pygame
import time

class Player():
    def __init__(self, pic, x, y, score):
        self.canvas = pygame.image.load(pic)
        self.canvas.convert()
        # 依據圖片創建rect(hitbox)
        self.rect = self.canvas.get_rect()
        self.mask = pygame.mask.from_surface(self.canvas)
        #為 rect 設定座標，便於操控上下左右
        self.rect.left, self.rect.top = x,y
        self.score = score

    def blit_me(self, screen):
        screen.blit(self.canvas, [self.rect.left, self.rect.top])

    def checkUserControl(self, up, down, left, right):
        keys = pygame.key.get_pressed()
        if keys[up]:
            self.rect.top -= 5
        if keys[down]:
            self.rect.top += 5
        if keys[left]:
            self.rect.left -= 5
        if keys[right]:
            self.rect.left += 5 
    def checkCollisionCoin(self,other) :
        if pygame.sprite.collide_mask(self, other):
            print("Collision occurred")
class Object():
    def __init__(self, pic, x, y):
        self.canvas = pygame.image.load(pic)
        self.canvas.convert()
        self.rect = self.canvas.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.mask = pygame.mask.from_surface(self.canvas)
    def blit_me(self, screen):
        screen.blit(self.canvas, [self.rect.left, self.rect.top])
