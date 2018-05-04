import pygame
import time
import random
class Player():
    def __init__(self, pic, x, y, score,bg_size):
        self.canvas = pygame.image.load(pic)
        self.canvas.convert()
        # 依據圖片創建rect(hitbox)
        self.rect = self.canvas.get_rect()
        self.mask = pygame.mask.from_surface(self.canvas)
        #為 rect 設定座標，便於操控上下左右
        self.rect.left, self.rect.top = x,y
        #設定背景寬度 後面用來確保腳色不會跑到地圖外
        self.bgWidth, self.bgHeight = bg_size[0], bg_size[1]
        self.score = score
        self.speed = 10


    def blit_me(self, screen):
        screen.blit(self.canvas, [self.rect.left, self.rect.top])

    def checkUserControl(self, up, down, left, right):
        keys = pygame.key.get_pressed()
        if keys[up]:
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else: 
                self.rect.top = 0 #確保不會跑到地圖外
        if keys[down]:
            if self.rect.top < self.bgHeight:
                self.rect.top += self.speed
            else : 
                self.rect.top = self.bgHeight
        if keys[left]:
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.rect.left = 0
        if keys[right]:
            if self.rect.left < self.bgWidth:
                self.rect.left += self.speed
            else: 
                self.rect.left = self.bgWidth
    def checkCollisionCoin(self,coin) :
        if pygame.sprite.collide_mask(self, coin):
            self.score += 1
            coin.rect.left = random.randrange(0,self.bgWidth)
            coin.rect.top = random.randrange(0,self.bgHeight)
            time.sleep(1)
    def checkCollideOther(self,other):
        if pygame.sprite.collide_mask(self, other):
            xDiff = self.rect.left - other.rect.left
            yDiff = self.rect.top - other.rect.top
            self.rect.left += xDiff*2
            self.rect.top += yDiff*2
            other.rect.left -= xDiff*2
            other.rect.top -= yDiff*2
    def checkCollideRock(self,other):
        if pygame.sprite.collide_mask(self, other):
            self.score -=1
            xDiff = self.rect.left - other.rect.left
            yDiff = self.rect.top - other.rect.top
            self.rect.left += xDiff*1
            self.rect.top += yDiff*1
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

class Rock():
    def __init__(self, pic, x, y, move_size):
        self.canvas = pygame.image.load(pic)
        self.canvas.convert()
        self.rect = self.canvas.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.mask = pygame.mask.from_surface(self.canvas)
        self.speed = [random.randrange(-10,10,3),random.randrange(-10,10,3)]
        self.bgWidth, self.bgHeight = move_size[0], move_size[1]
    def blit_me(self, screen):
        screen.blit(self.canvas, [self.rect.left, self.rect.top])

    def move(self):
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]
        if self.rect.top < -100 : 
            self.rect.top = self.bgHeight
            self.resetSpeed()
        if self.rect.top > self.bgHeight:
            self.rect.top = -100
            self.resetSpeed()
        if self.rect.left < -100 :
            self.rect.left = self.bgHeight
            self.resetSpeed()
        if self.rect.left > self.bgWidth:
            self.rect.left = -100
            self.resetSpeed()

    def resetSpeed(self):
        self.speed = [random.randrange(-10,10,3),random.randrange(-10,10,3)]
