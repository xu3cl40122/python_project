import pygame


class Horse():
    def __init__(self, pic, x, y, bg_size):
        self.canvas = pygame.image.load(pic)
        self.canvas.convert()
        # 依據圖片創建rect(hitbox)
        self.rect = self.canvas.get_rect()
        self.mask = pygame.mask.from_surface(self.canvas)
        #為 rect 設定座標，便於操控上下左右
        self.rect.left, self.rect.top = x, y
        #設定背景寬度 後面用來確保腳色不會跑到地圖外
        self.bgWidth, self.bgHeight = bg_size[0], bg_size[1]
        self.speed = 10

    def blit_me(self, screen):
        screen.blit(self.canvas, [self.rect.left, self.rect.top])


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
